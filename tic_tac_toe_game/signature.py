from enum import Enum


class Signature(Enum):
    X = "X"
    O = "O"
    EMPTY = "EMPTY"

    def __repr__(self):
        return self.value
