import settings as CONF


ROOT = CONF.BASE_DIR

def setting_dict():
    import settings as conf
    _ = dict()
    for i in dir(conf):
        if not i.startswith("_") and getattr(conf, i):
            _[i] = getattr(conf, i)
    return _
