Miscellaneous pre-commit hooks
==============================

This repository contains miscellaneous hooks for [pre-commit](https://pre-commit.com/) that I couldn't find anywhere else.

At the moment there's just one hook. I'm not really planning on actively maintaining this repository, but putting it up in case it saves anyone else a bit of time.

Example entry in .pre-commit-config.yaml:
``` yaml
- repo: https://github.com/czlee/pre-commit-hooks
  rev: v0.0.1
  hooks:
  - id: check-file-name-pattern
    files: directory-to-check/.+
    args:
    - --pattern
    - "[a-z0-9\\-]+.xml"
```

Hooks available
---------------

### `check-file-name-pattern`

Checks that file names match a given regex pattern.

You should specify a pattern using something like `args: ['--pattern=[a-z]+.xml']`. The default pattern is `.*`, which vacuously matches everything.
