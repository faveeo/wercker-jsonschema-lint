#!/bin/bash

if [ ! -n "$WERCKER_INCLUDE" ]; then
    fail 'Please specify an include glob pattern'
fi

if [ ! -n "$WERCKER_SCHEMA" ]; then
    fail 'Please specify a schema URL'
fi

sudo pip install -r requirements.txt
sudo python jsonschema-lint.py --include=$WERCKER_INCLUDE --schema=$WERCKER_SCHEMA
