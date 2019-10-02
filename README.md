# wercker-jsonschema-lint

This [Wercker](http://wercker.com/) step validates JSON files recursively according to a given schema, or a default schema.

This step must be used with a box containing Python 2.7 and Pip.

# Origin
This is a fork of https://github.com/1science/wercker-jsonschema-lint to make the step recursive.

## Versions

| Release date | Step version |
| -------------| -------------|
| 2019-10-02   | 0.0.5
| 2017-05-15   | 0.0.4        |
| 2016-05-19   | 0.0.3        |
| 2016-05-19   | 0.0.2        |
| 2016-05-18   | 0.0.1        |


## Options

* `path` (required) The root of the path to be validated recursively. Rooted in the output directory. ($WERCKER_OUTPUT_DIR)
* `filepattern` (optional) A glob pattern of files to validate. Default: *.json
* `schema` (optional) URL of a default schema to be used for validation, if JSON does not specify one. Default: http://json-schema.org/draft-03/hyper-schema

## Example

```
build:
  steps:
    ...
    - faveeo/jsonschema-lint:
        filepattern: **.json
        schema: http://json-schema.org/draft-03/schema
```
