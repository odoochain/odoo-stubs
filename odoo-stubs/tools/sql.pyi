from typing import Any, Optional

_schema: Any
_CONFDELTYPES: Any

def existing_tables(cr: Any, tablenames: Any): ...
def table_exists(cr: Any, tablename: Any): ...
def table_kind(cr: Any, tablename: Any): ...
def create_model_table(cr: Any, tablename: Any, comment: Optional[Any] = ..., columns: Any = ...) -> None: ...
def table_columns(cr: Any, tablename: Any): ...
def column_exists(cr: Any, tablename: Any, columnname: Any): ...
def create_column(cr: Any, tablename: Any, columnname: Any, columntype: Any, comment: Optional[Any] = ...) -> None: ...
def rename_column(cr: Any, tablename: Any, columnname1: Any, columnname2: Any) -> None: ...
def convert_column(cr: Any, tablename: Any, columnname: Any, columntype: Any) -> None: ...
def set_not_null(cr: Any, tablename: Any, columnname: Any) -> None: ...
def drop_not_null(cr: Any, tablename: Any, columnname: Any) -> None: ...
def constraint_definition(cr: Any, tablename: Any, constraintname: Any): ...
def add_constraint(cr: Any, tablename: Any, constraintname: Any, definition: Any) -> None: ...
def drop_constraint(cr: Any, tablename: Any, constraintname: Any) -> None: ...
def add_foreign_key(cr: Any, tablename1: Any, columnname1: Any, tablename2: Any, columnname2: Any, ondelete: Any): ...
def fix_foreign_key(cr: Any, tablename1: Any, columnname1: Any, tablename2: Any, columnname2: Any, ondelete: Any): ...
def index_exists(cr: Any, indexname: Any): ...
def create_index(cr: Any, indexname: Any, tablename: Any, expressions: Any) -> None: ...
def create_unique_index(cr: Any, indexname: Any, tablename: Any, expressions: Any) -> None: ...
def drop_index(cr: Any, indexname: Any, tablename: Any) -> None: ...
def drop_view_if_exists(cr: Any, viewname: Any) -> None: ...
def escape_psql(to_escape: Any): ...
def pg_varchar(size: int = ...): ...
def reverse_order(order: Any): ...
