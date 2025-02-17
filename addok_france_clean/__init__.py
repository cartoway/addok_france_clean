from addok.helpers import yielder

from . import utils
try:
    import pkg_resources
except ImportError:  # pragma: no cover
    pass
else:
    if __package__:
        VERSION = pkg_resources.get_distribution(__package__).version


clean_query = yielder(utils.clean_query)
multi_token_synonymize = utils.multi_token_synonymize
