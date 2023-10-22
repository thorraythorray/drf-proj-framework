from settings import *


def setting_dict():
    import settings as conf
    CONF = dict()
    for i in dir(conf):
        if not i.startswith("_") and getattr(conf, i):
            CONF[i] = getattr(conf, i)
    return CONF
