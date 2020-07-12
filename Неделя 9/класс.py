from sys import stdin


class Matrix:
    def __init__(self, m):
        from copy import deepcopy
        self.m = deepcopy(m)

    def __str__(self):
        return (
            '\n'.join(
                map(
                    lambda line: '\t'.join(
                        map(
                            str,
                            line
                        )
                    ),
                    self.m
                )
            )
        )

    def size(self):
        return len(self.m), len(self.m[0])

    def __add__(self, other):
        from operator import add
        if (len(self.m), len(self.m[0])) == (len(other.m), len(other.m[0])):
            return (
                Matrix(
                    map(
                        lambda sline, oline: map(
                            add,
                            sline,
                            oline
                        ),
                        self.m,
                        other.m
                    )
                )
            )
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        return (
            Matrix(
                map(
                    lambda line: map(
                        lambda i: i * other,
                        line
                    ),
                    self.m
                )
            )
        )

    __rmul__ = __mul__

    def transpose(self):
        # self.m = [list(line) for line in zip(*self.m)]
        self.m = \
            list(
                map(
                    lambda line: list(line),
                    zip(*self.m)
                )
            )
        return self

    @staticmethod
    def transposed(matrix):
        # return [list(line) for line in zip(*matrix)]
        return (
            Matrix(
                list(
                    map(
                        lambda line: list(line),
                        zip(*matrix.m)
                    )
                )
            )
        )


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


exec(stdin.read())
