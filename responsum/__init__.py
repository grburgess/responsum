from responsum.response import OGIPResponse, InstrumentResponse

__all__ = ['OGIPResponse', 'InstrumentResponse']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
