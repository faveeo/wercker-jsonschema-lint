# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import contextlib
import json
import logging
import sys
import urllib
from argparse import ArgumentParser

import fnmatch
import os

from jsonschema import validate, FormatChecker

logger = logging.getLogger('jsonschema-lint')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

parser = ArgumentParser(description='Validates JSON files based on a schema.')
parser.add_argument(
    '--path', '-p',
    type=unicode,
    help='path of folder to validate recursively',
    required=True
)
parser.add_argument(
    '--filepattern', '-f',
    type=unicode,
    help='Glob pattern of files to validate',
    default='*.json'
)
parser.add_argument(
    '--schema', '-s',
    type=unicode,
    help='URL of a default schema to be used for validation, if JSON does not specify one. Default: %(default)s',
    default='http://json-schema.org/draft-03/hyper-schema'
)

schemas = {}


def determine_validation_schema(document, default):
    doc_schema = document.get('$schema', default)

    if doc_schema not in schemas:
        logger.info('Loading schema at "%s"...', doc_schema)
        with contextlib.closing(urllib.urlopen(doc_schema)) as schema_content:
            schema = json.load(schema_content)
            schemas[doc_schema] = schema
            logger.info('Schema loaded')

    return schemas[doc_schema]


def lint(include, pattern, schema):
    logger.info('Validating files in %s with pattern "%s"...', include, pattern)

    for root, dirnames, filenames in os.walk(include):
        for filename in fnmatch.filter(filenames, pattern):
            file = os.path.join(root, filename)
            logger.info('Validating file "%s".', file)
            with open(file, 'rb') as f:
                try:
                    document = json.load(f)
                except ValueError as error:
                    print 'invalid json:', file, error
                    raise

                validation_schema = determine_validation_schema(document, schema)
                validate(document, validation_schema, format_checker=FormatChecker())

    logger.info('All files validated.')


if __name__ == '__main__':
    args = parser.parse_args()

    lint(args.path, args.filepattern, args.schema)
