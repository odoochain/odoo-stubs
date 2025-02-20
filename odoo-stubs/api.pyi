from collections import defaultdict
from weakref import WeakSet

from collections.abc import Mapping
from typing import Any, Optional

from .modules.registry import Registry
from .sql_db import Cursor
from .tools import StackMap

__all__: Any
_logger: Any
INHERITED_ATTRS: Any

class Params:
    args: Any = ...
    kwargs: Any = ...
    def __init__(self, args: Any, kwargs: Any) -> None: ...
    def __str__(self): ...

class Meta(type):
    def __new__(meta: Any, name: Any, bases: Any, attrs: Any): ...

def attrsetter(attr: Any, value: Any): ...
def propagate(method1: Any, method2: Any): ...
def constrains(*args: Any): ...
def onchange(*args: Any): ...
def depends(*args: Any): ...
def depends_context(*args: Any): ...
def returns(model: Any, downgrade: Optional[Any] = ..., upgrade: Optional[Any] = ...): ...
def downgrade(method: Any, value: Any, self: Any, args: Any, kwargs: Any): ...
def split_context(method: Any, args: Any, kwargs: Any): ...
def autovacuum(method: Any): ...
def model(method: Any): ...

_create_logger: Any

def _model_create_single(create: Any, self: Any, arg: Any): ...
def model_create_single(method: Any): ...
def _model_create_multi(create: Any, self: Any, arg: Any): ...
def model_create_multi(method: Any): ...
def _call_kw_model(method: Any, self: Any, args: Any, kwargs: Any): ...
def _call_kw_model_create(method: Any, self: Any, args: Any, kwargs: Any): ...
def _call_kw_multi(method: Any, self: Any, args: Any, kwargs: Any): ...
def call_kw(model: Any, name: Any, args: Any, kwargs: Any): ...

class Environment(Mapping):
    _local: Any = ...
    cr: Cursor = ...
    uid: int = ...
    context: dict = ...
    su: bool = ...
    envs: Environments = ...
    @classmethod
    def manage(cls) -> None: ...
    @classmethod
    def reset(cls) -> None: ...
    registry: Registry = ...
    cache: Cache = ...
    _cache_key: Any = ...
    _protected: Any = ...
    all: Environments = ...
    def __new__(cls, cr: Cursor, uid: Any, context: Any, su: bool = ...) -> Environment: ...
    def __contains__(self, model_name: Any) -> bool: ...
    def __getitem__(self, model_name: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __call__(self, cr: Optional[Cursor] = ..., user: Optional[Any] = ..., context: Optional[Any] = ..., su: Optional[Any] = ...) -> Environment: ...
    def ref(self, xml_id: Any, raise_if_not_found: bool = ...): ...
    def is_superuser(self) -> bool: ...
    def is_admin(self) -> bool: ...
    def is_system(self) -> bool: ...
    @property
    def user(self):
        return self['res.users']
    @property
    def company(self):
        return self['res.company']
    @property
    def companies(self):
        return self['res.company']
    @property
    def lang(self) -> str: ...
    def clear(self) -> None: ...
    def clear_upon_failure(self) -> None: ...
    def is_protected(self, field: Any, record: Any): ...
    def protected(self, field: Any): ...
    def protecting(self, what: Any, records: Optional[Any] = ...) -> None: ...
    def fields_to_compute(self): ...
    def records_to_compute(self, field: Any): ...
    def is_to_compute(self, field: Any, record: Any): ...
    def not_to_compute(self, field: Any, records: Any): ...
    def add_to_compute(self, field: Any, records: Any): ...
    def remove_to_compute(self, field: Any, records: Any) -> None: ...
    def norecompute(self) -> None: ...
    def cache_key(self, field: Any): ...

class Environments:
    envs: WeakSet = ...
    cache: Cache = ...
    protected: StackMap = ...
    tocompute: defaultdict = ...
    towrite: defaultdict = ...
    def __init__(self): ...
    def add(self, env: Any) -> None: ...
    def __iter__(self) -> Any: ...

NOTHING: Any

class Cache:
    _data: Any = ...
    def __init__(self) -> None: ...
    def contains(self, record: Any, field: Any): ...
    def get(self, record: Any, field: Any, default: Any = ...): ...
    def set(self, record: Any, field: Any, value: Any) -> None: ...
    def update(self, records: Any, field: Any, values: Any) -> None: ...
    def remove(self, record: Any, field: Any) -> None: ...
    def get_values(self, records: Any, field: Any) -> None: ...
    def get_until_miss(self, records: Any, field: Any): ...
    def get_records_different_from(self, records: Any, field: Any, value: Any): ...
    def get_fields(self, record: Any) -> None: ...
    def get_records(self, model: Any, field: Any): ...
    def get_missing_ids(self, records: Any, field: Any) -> None: ...
    def invalidate(self, spec: Optional[Any] = ...) -> None: ...
    def check(self, env: Any) -> None: ...
