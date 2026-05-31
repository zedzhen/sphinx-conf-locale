__all__ = ["LazyFormat"]


class LazyFormat(str):
    """Lazy calc format string
    based on https://github.com/sphinx-doc/sphinx/issues/1260#issuecomment-1881649107
    """

    def __new__(cls, msg: str, *args, **kwargs):
        instance = super().__new__(cls, msg)
        instance._lazy_msg = msg
        instance._lazy_args = args
        instance._lazy_kwargs = kwargs
        return instance

    def __str__(self):
        return self._lazy_msg.format(*self._lazy_args, **self._lazy_kwargs)
