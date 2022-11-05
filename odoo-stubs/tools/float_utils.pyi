def round(f: float) -> float: ...
def _float_check_precision(precision_digits: int | None = ..., precision_rounding: float | None = ...) -> float: ...
def float_round(value: float, precision_digits: int | None = ..., precision_rounding: float | None = ..., rounding_method: str = ...) -> float: ...
def float_is_zero(value: float, precision_digits: int | None = ..., precision_rounding: float | None = ...) -> bool: ...
def float_compare(value1: float, value2: float, precision_digits: int | None = ..., precision_rounding: float | None = ...) -> int: ...
def float_repr(value: float, precision_digits: int) -> str: ...
_float_repr = float_repr
def float_split_str(value: float, precision_digits: int) -> tuple[str, str]: ...
def float_split(value: float, precision_digits: int) -> tuple[int, int]: ...
def json_float_round(value: float, precision_digits: int, rounding_method: str = ...) -> float: ...
