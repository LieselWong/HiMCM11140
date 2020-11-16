import random
import csv

def getJobs():
    with open("rollingpin.csv") as file:
        reader = csv.reader(file)
        next(reader)
        next(reader)
        jobs = []
        for row in reader:
            temp = []
            for char in "RIASEC":
                temp.append(char in row[2])
            jobs.append([row[0], float(row[1]), temp, float(row[5]), int(row[6]), int(row[8]), row[4]])
        return jobs

def getTimes():
    times = []
    with open("results.txt") as file:
        for _ in range(10):
            personTimes = []
            for _ in range(4):
                file.readline()
            for _ in range(99):
                personTimes.append(float(file.readline().split()[-1])/3)
            times.append(personTimes)
    return times

def getJobScores(people, jobs = getJobs(), times = getTimes()):
    jobScores = []
    for i, person in enumerate(people):
        personScores = []
        values, weights = person
        for j, job in enumerate(jobs):
            commute = times[i][j]
            jobValues = jobvaluesss(job[1:]+[commute], values)
            personScores.append(satisfaction(weights, jobValues))
        jobScores.append(personScores)
    return jobScores
    # format: [[person0job0, person0job1...],...,[personNjob0,...,personNjobN]] 

def percentdifference(actual, expected):
    if expected == 0:
        return actual #ASK ANGEL HALP: answer: say cannot enter
    return (actual - expected)/expected

def difficulty(actual, expected):
    x = percentdifference(actual, expected)
    return abs(x) * -1

def time(workinghours, commutehr, selfcare = 1, sleep = 8):
    #selfcare is inputted by person
    x = 24 - selfcare - sleep - workinghours - 2*commutehr
    if x < 0:
        x = 0
    return x

def hollandcode(jobtraits, applicanttraits):
    matches = 0
    for i in range(len(jobtraits)):
        if jobtraits[i] and applicanttraits[i]:
            matches += 1
    return matches/jobtraits.count(True) - 1
    
def jobvaluesss(cheese, expected):
    newcheese = []
    newcheese.append(percentdifference(cheese[0], expected[0]))
    newcheese.append(hollandcode(cheese[1], expected[1]))
    newcheese.append(percentdifference(time(cheese[2], cheese[6]), expected[2]))
    newcheese.append(difficulty(cheese[3], expected[3]))
    newcheese.append(difficulty(cheese[4], expected[4]))
    newcheese.append(int(cheese[5] == expected[5])-1)
    return newcheese
    
def satisfaction(weights, jobvalues):
    isfaction = 0
    for i in range(len(weights)):
        isfaction += weights[i] * jobvalues[i]
    return isfaction

