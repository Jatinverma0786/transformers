# Copyright 2020 The HuggingFace Team. All rights reserved.

from typing import TYPE_CHECKING

from ...utils import _LazyModule
from ...utils.import_utils import define_import_structure


if TYPE_CHECKING:
    from .configuration_quatfit1 import *
    from .modeling_quatfit1 import *
else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        define_import_structure(__file__),
        module_spec=__spec__,
    )