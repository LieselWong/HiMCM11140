def percentdifference(actual, expected):
    return (actual - expected)/expected

def difficulty(actual, expected):
    x = percentdifference(actual, expected)
    if x == 0:
        return 1
    else:
        return abs(x) * -1

def time(selfcare = 1.5):
    x = 24 - selfcare - sleep - workinghours - commutehr
    if x < 0:
        x = 0
    return x

def hollandcode(jobtraits, applicanttraits)
    matches = 0
    for i in range(len(jobtraits)):
        if jobtraits[i] and applicantstraits[i]:
            matches += 1
    return matches/3 
    
jobtraits = [True, True, True, False, False, False]
applicanttraits = [True, True, True, False, False, False]

print(hollandcode(jobtraits, applicanttraits))
