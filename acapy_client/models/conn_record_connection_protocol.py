from enum import Enum


class ConnRecordConnectionProtocol(str, Enum):
    C = "c"
    O = "o"
    N = "n"
    E = "e"
    T = "t"
    I = "i"
    S = "s"
    VALUE_7 = "/"
    VALUE_8 = "1"
    VALUE_9 = "."
    VALUE_10 = "0"
    D = "d"
    X = "x"
    H = "h"
    A = "a"
    G = "g"

    def __str__(self) -> str:
        return str(self.value)
