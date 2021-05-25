import logging

# info: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# info: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
logger = logging.getLogger(__name__)

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]\
        %(message)s',
        filename='test.log',
        level=logging.INFO)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logger.info(f'Add: {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logger.info(f'Sub: {num_1} - {num_2} = {sub_result}')

mul_result = multiply(num_1, num_2)
logger.info(f'Mul: {num_1} * {num_2} = {mul_result}')

div_result = divide(num_1, num_2)
logger.info(f'Div: {num_1} / {num_2} = {div_result}')
