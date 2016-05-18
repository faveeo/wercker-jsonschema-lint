#!/bin/bash

if [ ! -n "$WERCKER_INCLUDE" ]; then
    fail 'Please specify an include glob pattern'
fi

sudo pip install -r requirements.txt

if [ ! -n "$WERCKER_SCHEMA" ]; then
    sudo python jsonschema-lint.py --include=$WERCKER_INCLUDE
else
    sudo python jsonschema-lint.py --include=$WERCKER_INCLUDE --schema=$WERCKER_SCHEMA
fi
