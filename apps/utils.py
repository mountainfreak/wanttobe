from datetime import datetime


def serialize(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        elif isinstance(v, datetime):
            if v.utcoffset() is not None:
                v = v - v.utcoffset()
            d[c.name] = v.strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            d[c.name] = v
    return d