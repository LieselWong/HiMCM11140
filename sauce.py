import random

def randPerson():
    wage = random.randint(7, 25)
    codes = random.sample(range(6), 3)
    codes = [i in codes for i in range(6)]
    hours = random.randint(1, 8)
    difficulty = random.randint(1, 5)
    weights = [1, 1, 1, 1] #TODO: use AHP
    return [wage, codes, hours, difficulty], weights

def randPeople(n):
    return [randPerson() for _ in range(n)]

