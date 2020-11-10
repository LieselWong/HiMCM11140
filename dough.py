def percentdifference(actual, expected):
    if expected = 0:
        return actual #ASK ANGEL HALP
    return (actual - expected)/expected

def difficulty(actual, expected):
    x = percentdifference(actual, expected)
    if x == 0:
        return 1
    else:
        return abs(x) * -1

def time(selfcare = 1.5, sleep = 8, workinghours = 7, commutehr = 2):
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
weights = [1, 1, 1, 1]
jobvalues = [percentdifference(5000, 6000), difficulty(3, 5),
             percentdifference(time(), 5),
             hollandcode(jobtraits, applicanttraits)]

def Satisfaction (weights, jobvalues):
    isfaction = 0
    for i in range (len(weights)):
        isfaction += weights[i] * jobvalues[i]
    return isfaction

print(Satisfaction(weights, jobvalues))
