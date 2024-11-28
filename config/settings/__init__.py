from config.settings.base import *
try:
    if LOCAL:
        from config.settings.local import *
    elif STAGE:
        from config.settings.stage import *
    elif PROD:
        from config.settings.prod import *
except ImportError:
    raise