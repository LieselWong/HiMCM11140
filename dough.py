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
            jobValues = jobvalues(job[1:]+[commute], values)
            personScores.append(satisfaction(weights, jobValues))
        jobScores.append(personScores)
    return jobScores
    # format: [[person0job0, person0job1...],...,[personNjob0,...,personNjobN]] 

def percentdifference(actual, expected):
    if expected == 0:
        return actual
    return (actual - expected)/expected

def absvaldiff(actual, expected):
    x = percentdifference(actual, expected)
    return abs(x) * -1

def time(workinghours, commutehr, selfcare = 1, sleep = 8):
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
    
def jobvalues(jobtraits, expected):
    vals = []
    vals.append(percentdifference(jobtraits[0], expected[0]))
    vals.append(hollandcode(jobtraits[1], expected[1]))
    vals.append(percentdifference(time(jobtraits[2], jobtraits[6]), expected[2]))
    vals.append(absvaldiff(jobtraits[3], expected[3]))
    vals.append(absvaldiff(jobtraits[4], expected[4]))
    vals.append(int(jobtraits[5] == expected[5])-1)
    return vals
    
def satisfaction(weights, jobvalues):
    s = 0
    for i in range(len(weights)):
        s += weights[i] * jobvalues[i]
    return s

