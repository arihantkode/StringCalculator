class InvalidInputError(Exception):
    """Custom exception for invalid input in add_string function."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)