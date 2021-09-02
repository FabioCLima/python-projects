class RuntimeErrorWithCode(Exception):
    """[Exception raised when a specific error code is needed]

    Args:
        TypeError ([str]): [description of custom error]
    """
    def __init__(self, message: str, code: int):
        super().__init__(f"Error code {code}: {message}")
        self.code = code


err = RuntimeErrorWithCode("An error happened.", 500)
print(err.__doc__)
