# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import contextlib
import json
import logging
import sys
import urllib
from argparse import ArgumentParser
from glob import iglob

from jsonschema import validate, FormatChecker

logger = logging.getLogger('jsonschema-lint')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)

parser = ArgumentParser(description='Validates JSON files based on a schema.')
parser.add_argument(
    '--include', '-i',
    type=unicode,
    help='Glob pattern of files to validate',
    required=True
)
parser.add_argument(
    '--schema', '-s',
    type=unicode,
    help='URL of a default schema to be used for validation, if JSON does not specify one. Default: %(default)s',
    default='http://json-schema.org/schema'
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


def lint(include, schema):
    logger.info('Validating files with pattern "%s"...', include)
    for path in iglob(include):
        logger.info('Validating file "%s".', path)
        with open(path, 'rb') as f:
            document = json.load(f)
            validation_schema = determine_validation_schema(document, schema)
            validate(document, validation_schema, format_checker=FormatChecker())

    logger.info('All files validated.')


if __name__ == '__main__':
    args = parser.parse_args()
    lint(args.include, args.schema)
