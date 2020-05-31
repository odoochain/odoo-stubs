from ..models import MAGIC_COLUMNS as MAGIC_COLUMNS
from functools import partial as partial
from odoo.tools.misc import get_lang as get_lang
from typing import Any, Optional

NOT_OPERATOR: str
OR_OPERATOR: str
AND_OPERATOR: str
DOMAIN_OPERATORS: Any
TERM_OPERATORS: Any
NEGATIVE_TERM_OPERATORS: Any
DOMAIN_OPERATORS_NEGATION: Any
TERM_OPERATORS_NEGATION: Any
TRUE_LEAF: Any
FALSE_LEAF: Any
TRUE_DOMAIN: Any
FALSE_DOMAIN: Any
_logger: Any

def normalize_domain(domain: Any): ...
def is_false(model: Any, domain: Any): ...
def combine(operator: Any, unit: Any, zero: Any, domains: Any): ...
def AND(domains: Any): ...
def OR(domains: Any): ...
def distribute_not(domain: Any): ...
def _quote(to_quote: Any): ...
def generate_table_alias(src_table_alias: Any, joined_tables: Any = ...): ...
def get_alias_from_query(from_query: Any): ...
def normalize_leaf(element: Any): ...
def is_operator(element: Any): ...
def is_leaf(element: Any, internal: bool = ...): ...
def is_boolean(element: Any): ...
def check_leaf(element: Any, internal: bool = ...) -> None: ...
def select_from_where(cr: Any, select_field: Any, from_table: Any, where_field: Any, where_ids: Any, where_operator: Any): ...
def get_unaccent_wrapper(cr: Any): ...

class expression:
    _unaccent: Any = ...
    root_model: Any = ...
    root_alias: Any = ...
    expression: Any = ...
    query: Any = ...
    def __init__(self, domain: Any, model: Any, alias: Optional[Any] = ..., query: Optional[Any] = ...) -> None: ...
    def get_tables(self): ...
    def parse(self): ...
    def __leaf_to_sql(self, leaf: Any, model: Any, alias: Any): ...
    def to_sql(self): ...
