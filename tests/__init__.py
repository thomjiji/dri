def skip_if_resolve_none(func):
    def wrapper(self, *args, **kwargs):
        if self.resolve is None:
            self.skipTest("resolve object is None, skipping test.")
        else:
            return func(self, *args, **kwargs)

    return wrapper