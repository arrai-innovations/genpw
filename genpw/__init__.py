# Copyright (C) 2020 Arrai Innovations Inc. - All Rights Reserved
__version__ = "1.0.0"

try:
    from .genpw import pronounceable_passwd

    __all__ = ["pronounceable_passwd"]
except ImportError:
    pass
