from config.settings.base import *
try:
    if ENVIRONMENT == 'local':
        from config.settings.local import *
    elif ENVIRONMENT == 'stage':
        from config.settings.stage import *
    elif ENVIRONMENT == 'prod':
        from config.settings.prod import *
except ImportError:
    raise