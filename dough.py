import random
def percentdifference(actual, expected):
    if expected == 0:
        return actual #ASK ANGEL HALP: answer: say cannot enter
    return (actual - expected)/expected

def difficulty(actual, expected):
    x = percentdifference(actual, expected)
    if x == 0:
        return 1
    else:
        return abs(x) * -1

def time(workinghours, selfcare = 1, sleep = 8, commutehr = 2):
    #selfcare is inputted by person
    x = 24 - selfcare - sleep - workinghours - commutehr
    if x < 0:
        x = 0
    return x

def hollandcode(jobtraits, applicanttraits):
    matches = 0
    for i in range(len(jobtraits)):
        if jobtraits[i] and applicanttraits[i]:
            matches += 1
    return matches/jobtraits.count(True)
    
jobtraits = [False, True, True, False, False, False]
applicanttraits = [True, True, True, False, False, False]

print(hollandcode(jobtraits, applicanttraits))
weights = [1, 1, 1, 1, 1]
'''jobvalues = [percentdifference(5000, 6000), difficulty(3, 5),
             percentdifference(time(), 5),
             hollandcode(jobtraits, applicanttraits)]'''

'''def wage():
    x = random.randint(0, 100)
    if x < 1:
        return random.randint(6, 9)
    if x < 8:
        return random.randint(6, 9)
    if x < 23:
        return random.randint(6, 9)
    if x < 42:
        return random.randint(6, 9)
    if x < 60:
        return random.randint(6, 9)
    if x < 72:
        return random.randint(6, 9)
    if x < 81:
        return random.randint(6, 9)
    if x < 1:
        return random.randint(6, 9)
    if x < 1:
        return random.randint(6, 9)
    if x < 1:
        return random.randint(6, 9)
    if x < 1:
        return random.randint(6, 9)'''

'''random.randint(6, 28) random.randint(0, 12)random.randint(1, 5)'''

def jobvaluesss (cheese):
    cheese[1] = percentdifference(cheese[1], 30)
    cheese[2] = hollandcode(jobtraits, jobtraits)
    cheese[3] = percentdifference(time(cheese[3]), 4)
    #FOR CHEESE[3] FIX RANDINT BECUZ COMMUTE TIME CHANGES
    cheese[4] =  difficulty(3, 5)
    
def Satisfaction (weights, jobvalues):
    isfaction = 0
    for i in range (1, len(weights)):
        isfaction += weights[i] * jobvalues[i]
        print(jobvalues[i])
    return isfaction

'''jobvaluesss(jobs)
print(Satisfaction(weights, jobs))'''
