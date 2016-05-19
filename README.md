# wercker-jsonschema-lint

This [Wercker](http://wercker.com/) step validates a JSON file according to a schema.

This step must be used with a box containing Python 2.7 and Pip.


## Versions

| Release date | Step version |
| -------------| -------------|
| 2016-05-19   | 0.0.2        |
| 2016-05-18   | 0.0.1        |


## Options

* `include` (required) A glob pattern of files to lint
* `schema` (optional) URL of a default schema to be used for validation, if JSON does not specify one. Default: http://json-schema.org/schema

## Example

```
build:
  steps:
    ...
    - 1science/jsonschema-lint:
        include: **.json
        schema: http://json-schema.org/schema
```
