import os
import csv
import dough
import random 
#os.chdir("/Users/christinelee/Documents/Github/HiMCM11140")
with open("rollingpin.csv") as csvfile:
    reader = csv.reader(csvfile)
    next (reader)
    next (reader)
    jobs = []
    for row in reader:
        temp = []
        for char in "RIASEC":
            temp.append(char in row[2])
        jobs.append([row[0], float(row[1]), temp, float(row[5]), random.randint(1, 5)])
    weights = ["test", 1, 1, 1, 1]
    applicantvalues = ["test", 15, [True, True, True, False, False, False], 4, 4]
    jobScores = []
    for job in jobs:
        jobvalues = dough.jobvaluesss(job, applicantvalues)
        jobScores.append((dough.Satisfaction(weights, jobvalues), job))
    jobScores.sort(key = lambda x: x[0])
    for job in jobScores[::-1]:
        print(job)

