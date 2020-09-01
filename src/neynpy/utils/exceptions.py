class ValidationError(Exception):
    """
    ValidationError to raise all invalid errors
    """
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors
