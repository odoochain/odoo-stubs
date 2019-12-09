# Stubs for odoo.tools.safe_eval (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

unsafe_eval = eval

def test_expr(expr: Any, allowed_codes: Any, mode: str = ...): ...
def const_eval(expr: Any): ...
def safe_eval(expr: Any, globals_dict: Optional[Any] = ..., locals_dict: Optional[Any] = ..., mode: str = ..., nocopy: bool = ..., locals_builtins: bool = ...): ...
