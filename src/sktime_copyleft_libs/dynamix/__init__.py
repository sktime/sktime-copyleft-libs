"""DynaMix, vendored from DurstewitzLab/DynaMix-python.

Inference-only subset of the upstream package. The training, metrics, plotting
and dataset modules are not included.

Licensed under GPL-3.0. See the LICENSE file in this directory.

Source: https://github.com/DurstewitzLab/DynaMix-python

Modified from upstream: this ``__init__`` and ``utilities/__init__`` were
rewritten in 2026 to drop imports of the excluded modules. All other files are
unmodified.
"""

from .model.dynamix import DynaMix
from .model.forecaster import DynaMixForecaster
from .utilities.utilities import load_hf_model, load_hf_model_config

__all__ = [
    "DynaMix",
    "DynaMixForecaster",
    "load_hf_model",
    "load_hf_model_config",
]
