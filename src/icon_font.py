class classproperty(property):
    def __get__(self, instance, owner):
        return self.fget(owner)


class Icon:
    _close = "\ue6e8"
    _tophint_off = "\ue60f"
    _tophint_on = "\ue6e9"
    _setting = "\ue663"

    @classproperty
    def CLOSE(cls) -> str:
        return cls._close

    @classproperty
    def TOPHINT_OFF(cls) -> str:
        return cls._tophint_off

    @classproperty
    def TOPHINT_ON(cls) -> str:
        return cls._tophint_on

    @classproperty
    def SETTING(cls) -> str:
        return cls._setting
