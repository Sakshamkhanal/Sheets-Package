class Dialect:
    '''
    A container for options that control how a csv file should be handled when
    converting it to a set of objects

    has_header_row
        A Boolean indicating whether the file has a row containing header
        values.If True,that row will be skipped  when looking for data .
        Defaults to False
    '''

    def __init__(self,has_header_row=False,**kwargs):
        self.has_header_row = has_header_row
        self.csv_dialect = kwargs