# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    help='URL of the schema to be used for validation',
    required=True
)


def lint(include, schema):
    logger.info('Loading schema at "%s"...', schema)
    json_schema_file = urllib.urlopen(schema).read()
    schema = json.loads(json_schema_file)

    logger.info('Schema loaded')
    logger.info('Validating files with pattern "%s"...', include)

    for path in iglob(include):
        logger.info('Validating file "%s".', path)
        with open(path, 'rb') as f:
            document = json.load(f)
            validate(document, schema, format_checker=FormatChecker())

    logger.info('All files validated.')


if __name__ == '__main__':
    args = parser.parse_args()
    lint(args.include, args.schema)
