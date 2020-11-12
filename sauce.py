import random

def randPerson():
    wage = randWage()
    codes = random.sample(range(6), 3)
    codes = [i in codes for i in range(6)]
    hours = random.randint(1, 8)
    difficulty = random.randint(1, 5)
    weights = [1, 1, 1, 1] #TODO: use AHP
    return [wage, codes, hours, difficulty], weights

def randPeople(n):
    return [randPerson() for _ in range(n)]

def randWage():
    x = random.randint(0, 95)
    if x < 1:
        return random.randint(6, 9)
    if x < 8:
        return random.randint(9, 11)
    if x < 23:
        return random.randint(11, 12)
    if x < 42:
        return random.randint(12, 14)
    if x < 60:
        return random.randint(14, 16)
    if x < 72:
        return random.randint(16, 18)
    if x < 81:
        return random.randint(18, 20)
    if x < 86:
        return random.randint(20, 22)
    if x < 89:
        return random.randint(22, 24)
    if x < 93:
        return random.randint(24, 26)
    return random.randint(26, 28)

