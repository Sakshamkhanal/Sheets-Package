from sheets import options

class RowMeta(type):
    def __init__(cls,name,base,attrs):
        if 'Dialect' in attrs:
            #Filter out python's own additions to namespace
            items = attrs['Dialect'].__dict__.items()
            items = dict((k,v) for (k,v) in items if not k.startswith('__'))
        else:
            items = {}
        cls._dialect = options.Dialect(**items)

        for key,attr in attrs.items():
            if hasattr(attr,'attach_to_class'):
                attr.attach_to_class(cls,key,cls._dialect)


class Row(metaclass=RowMeta):
    pass