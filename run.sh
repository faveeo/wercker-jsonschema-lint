#!/bin/bash

if [ ! -n "$WERCKER_JSONSCHEMA_LINT_INCLUDE" ]; then
    fail 'Please specify an include glob pattern.'
fi

sudo pip install -r requirements.txt

if [ ! -n "$WERCKER_JSONSCHEMA_LINT_SCHEMA" ]; then
    sudo python jsonschema-lint.py --include=$WERCKER_JSONSCHEMA_LINT_INCLUDE
else
    sudo python jsonschema-lint.py --include=$WERCKER_JSONSCHEMA_LINT_INCLUDE --schema=$WERCKER_JSONSCHEMA_LINT_SCHEMA
fi
