import logging

logger = logging.getLogger("__name__")
logging.basicConfig(
    filename="Employee-Record.log",
    level=logging.INFO,
    format="%(levelname)s:%(message)s",
)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logging.info("Created employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Correy", "Schafer")
emp_3 = Employee("Jane", "Doe")
x = 2
print(emp_1)
