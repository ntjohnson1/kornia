from __future__ import annotations

from copy import deepcopy
from typing import Any, Optional


def default_with_one_parameter_changed(*, default: Optional[dict[str, Any]] = None, **possible_parameters: Any) -> Any:
    if default is None:
        default = {}
    if not isinstance(default, dict):
        raise AssertionError(f"default should be a dict not a {type(default)}")

    for parameter_name, possible_values in possible_parameters.items():
        for v in possible_values:
            param_set = deepcopy(default)
            param_set[parameter_name] = v
            yield param_set
