# - define a UncountableError that takes in wrong_value as the only argument
# - the UncountableError should inherit ValueError
# - the UncountableError should indicate an error message like this:
# 'Invalid value for n, WRONG_VALUE. n must be greater than 0.'
#  where WRONG_VALUE should be replaced by the given value in the argument
# define your UncountableError here:

class UncountableError(ValueError):
    """[Custom error that takes in wrong_value as the only argument, inherit
    from ValueError class]

    Args:
        ValueError ([int]): [negative integer which raises a custom error]
    """
    def __init__(self, wrong_value):
        super().__init__(f"Invalid value for n, {wrong_value}. n must be \
    greater than 0.")


def count_from_zero_to_n(n: int) -> None:
    """[Takes in an integer n as an argument, and prints out the integer
    from 0 to n. If someone calls this function with a negative integer,
    the function would print out nothing.]

    Args:
        n (int): [integer argument]
    """
    if n < 0:
        raise UncountableError(n)
    for x in range(0, n+1):
        print(x)


count_from_zero_to_n(3)
count_from_zero_to_n(-4)
