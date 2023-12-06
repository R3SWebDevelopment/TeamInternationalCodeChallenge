import cProfile
import random
from DataCapture import DataCapture

options = [
    n
    for n in range(1000)
]  # Numbers for 0 to 1000

numbers_count = 10000  # Number of items to be used
numbers = random.choices(options, k=numbers_count)  # Random select the numbers to be used

less_param = random.choice(numbers)  # Randomly pick a number to be used as parameter for less function
greater_param = random.choice(numbers)  # Randomly pick a number to be used as parameter for greater function

# Randomly pick a number to be used as parameter for between function
value_min = random.choice(numbers)
value_max = random.choice(numbers)

value_min, value_max = (value_max, value_min) if value_max < value_min else (value_min, value_max)


def main():
    capture = DataCapture()

    for n in numbers:
        capture.add(n)

    stats = capture.build_stats()

    print(f"Querying for the less number of: {less_param}")
    results = stats.less(less_param)
    print(f"Results: {results}")
    print(f"Querying for the greater number of: {greater_param}")
    results = stats.greater(greater_param)
    print(f"Results: {results}")
    print(f"Querying for the between number of: {value_min} and {value_max}")
    results = stats.between(value_min, value_max)
    print(f"Results: {results}")


if __name__ == "__main__":
    cProfile.run('main()')
