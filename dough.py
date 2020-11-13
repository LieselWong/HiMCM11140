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
    
#jobtraits = [False, True, True, False, False, False]
#applicanttraits = [True, True, True, False, False, False]

#print(hollandcode(jobtraits, applicanttraits))
#weights = [1, 1, 1, 1, 1]
'''jobvalues = [percentdifference(5000, 6000), difficulty(3, 5),
             percentdifference(time(), 5),
             hollandcode(jobtraits, applicanttraits)]'''

'''random.randint(6, 28) random.randint(0, 12)random.randint(1, 5)'''

def jobvaluesss(cheese, expected):
    newcheese = []
    newcheese.append(percentdifference(cheese[0], expected[0]))
    newcheese.append(hollandcode(cheese[1], expected[1]))
    newcheese.append(percentdifference(time(cheese[2]), expected[2])) #need to add commute time
    newcheese.append(difficulty(cheese[3], expected[3]))
    newcheese.append(difficulty(cheese[4], expected[4]))
    newcheese.append(int(cheese[5] == expected[5]))
    return newcheese
    
def satisfaction(weights, jobvalues):
    isfaction = 0
    for i in range (1, len(weights)):
        isfaction += weights[i] * jobvalues[i]
    return isfaction

'''jobvaluesss(jobs)
print(Satisfaction(weights, jobs))'''
