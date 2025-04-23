class Column:
    '''
    An individual column within a CSV file.This serves as a base for attributes
    and methods that are common to all types of columns.Subclasses of Column
    will define behaviour for more specific data types.
    '''

    def __init__(self,title=None,required=True):
        self.title = title
        self.required = required

    def attach_to_class(self,cls,name,options):
        self.cls = cls
        self.name = name
        self.options = options
        if self.title is None:
            #Check for None so that an empty string will skip this behaviour
            self.title = name.replace('_',' ')