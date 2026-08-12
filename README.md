# sktime-copyleft-libs

Copyleft-licensed libraries for use with [`sktime`](https://github.com/sktime/sktime).

## What this repository is for

`sktime` is licensed under the permissive BSD-3-Clause license. Some algorithms
that `sktime` interfaces are published under copyleft licenses such as GPL-3.0,
and some of those are not distributed on PyPI at all.

Vendoring copyleft code directly into `sktime` is not appropriate, since it would
mean shipping copyleft-licensed source as part of a BSD-3-Clause distribution.
Installing such code from a git URL is also undesirable, as unpinned git
installs are a supply chain risk.

This repository is the home for that code instead. It packages copyleft-licensed
libraries so that `sktime` can interface them as an ordinary, versioned,
PyPI-installable **soft dependency**, while keeping all copyleft source outside
of the `sktime` distribution.

## License

**This distribution is licensed under GPL-3.0-only.** See [`LICENSE`](LICENSE).

The whole package is copyleft, by design. Every library vendored here must carry
a license compatible with GPL-3.0, and each one retains its own upstream
`LICENSE` file and attribution alongside its source.

This is a deliberate and important difference from `sktime` itself, which is
BSD-3-Clause. Installing this package brings GPL-3.0 code into your environment.
Please make sure that is compatible with your intended use.

## Relationship to sktime

- `sktime` **does not depend on this package** as a core or hard dependency.
- Estimators that need a library from here declare it as a soft dependency, and
  it is installed by the user on demand.
- `sktime` remains BSD-3-Clause. Importing an optional GPL-3.0 package at runtime
  does not change the license of the `sktime` distribution.
- Estimators backed by this package are additionally gated behind an explicit
  license acknowledgement, so that users are made aware of the license terms
  before the model can be constructed.

## Contents

DynaMix will be the first library vendored here.

| Library | Upstream | Upstream license | Status |
|---|---|---|---|
| `dynamix` | [DurstewitzLab/DynaMix-python](https://github.com/DurstewitzLab/DynaMix-python) | GPL-3.0 | planned |

DynaMix is a mixture-of-experts dynamical-systems foundation model for zero-shot
multivariate forecasting. It is GPL-3.0 licensed and has no PyPI release, which
is what motivated this repository.

## Installation

```bash
pip install sktime-copyleft-libs
```

Requires Python 3.11 or later.

## Status

Early. The scaffolding is in place; library source has not been added yet.
