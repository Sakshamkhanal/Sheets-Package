from sheets import options

class RowMeta(type):
    def __init__(cls,name,base,attrs):
        if 'Dialect' in attrs:
            #Filter out python's own additions to namespace
            items = attrs['Dialect'].__dict__.items()
            items = dict((k,v) for (k,v) in items if not k.startswith('__'))
        else:
            items = {}
            dialect = options.Dialect(**items)