class AccountNotFoundError(BaseException):
    def __init__(self, message):
        super().__init__(message)

    class InsufficientFundsError(BaseException):
        def __init__(self, message):
            super().__init__(message)

    class InvalidPinError(BaseException):
        def __init__(self, message):
            super().__init__(message)
