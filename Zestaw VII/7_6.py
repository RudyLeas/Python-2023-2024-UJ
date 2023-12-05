import random


def zeros_ones_repeting():
    while True:
        yield 0
        yield 1
zeros_ones_iter = zeros_ones_repeting()
for i in range(100):
    print(next(zeros_ones_iter), end=", "if i % 20!=19 else "\n")
print()
def random_direction():
    directions = ["N", "S", "W", "E"]
    while True:
        yield directions[random.randint(0, 3)]
dir_iter = random_direction()
for i in range(100):
    print(next(dir_iter), end=", " if i % 20!=19 else "\n")
print()
def days_of_week():
    days = [0,1,2,3,4,5,6]
    while True:
        for day in days:
            yield day
days_iter = days_of_week()
for i in range(100):
    print(next(days_iter), end=", " if i % 20!=19 else "\n")