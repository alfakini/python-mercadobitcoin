class ApiError(Exception):
    def __init__(self, error, status_code):
        super(Exception, self).__init__(self, error)
        self.error = error
        self.status_code = status_code

    def __str__(self):
        return repr(self.error)


class ArgumentError(Exception):
    def __init__(self, error):
        super(Exception, self).__init__(self, error)
        self.error = error

    def __str__(self):
        return repr(self.error)
