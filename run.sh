#!/bin/bash

sudo pip install -r $WERCKER_STEP_ROOT/requirements.txt

if [ ! -n "$WERCKER_JSONSCHEMA_LINT_SCHEMA" ]; then
    sudo python $WERCKER_STEP_ROOT/jsonschema-lint.py --path=$WERCKER_OUTPUT_DIR/$WERCKER_JSONSCHEMA_LINT_PATH --filepattern=$WERCKER_JSONSCHEMA_LINT_FILEPATTERN
else
    sudo python $WERCKER_STEP_ROOT/jsonschema-lint.py --path=$WERCKER_OUTPUT_DIR/$WERCKER_JSONSCHEMA_LINT_PATH --schema=$WERCKER_JSONSCHEMA_LINT_SCHEMA --filepattern=$WERCKER_JSONSCHEMA_LINT_FILEPATTERN
fi
