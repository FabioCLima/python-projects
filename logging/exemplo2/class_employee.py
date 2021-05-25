import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
        format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]\
        %(message)s',
        filename='employee.log',
        level=logging.INFO)


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f'Created Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee('Fabio', 'Lima')
emp_2 = Employee('Fabiana', 'Lima')
emp_3 = Employee('John', "Smith")
