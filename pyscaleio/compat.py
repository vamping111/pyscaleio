from __future__ import unicode_literals

try:
    from collections.abc import Mapping, MutableMapping, MutableSequence, Sequence
except ImportError:
    from collections import Mapping, MutableMapping, MutableSequence, Sequence  # noqa: F401
