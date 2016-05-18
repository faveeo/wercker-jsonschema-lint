# wercker-jsonschema-lint

This [Wercker](http://wercker.com/) step validates a JSON file according to its schema.

This step must be used with a box containing Python 2.7 and Pip.


## Versions

| Release date | Step version |
| -------------| -------------|
| 2016-05-17   | 0.1          |


## Options

* `include` (required) A glob pattern of files to lint
* `schema` (required) Schema URL

## Example

```
build:
  steps:
    ...
    - 1science/jsonschema-lint:
        include: **.json
```
