__all__ = ["_", "_f"]

from sphinx.locale import _ as sphinx__

from sphinx_conf_locale.lazy_format import LazyFormat


def _(message: str) -> str:
    return LazyFormat(sphinx__(message))


def _f(message: str, *args, **kwargs) -> str:
    return LazyFormat(sphinx__(message), *args, **kwargs)
