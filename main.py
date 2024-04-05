import worldometer
from datetime import datetime
from application.people import get_employees
from application.salary import calculate_salary


def time():
    print(datetime.now())


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    time()

