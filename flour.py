import os
import csv
import dough
import random 
os.chdir("/Users/christinelee/Documents/Github/HiMCM11140")
with  open("rollingpin.csv") as csvfile:
    reader = csv.reader(csvfile)
    next (reader)
    next (reader)
    jobs = []
    for row in reader:
        temp = []
        for char in "RIASEC":
            temp.append(char in row[2])
        jobs.append([row[0], float(row[1]), temp, float(row[5]), 0])
    weights = [1, 1, 1, 1, 1]
    dough.jobvaluesss(jobs[0])
    print(dough.Satisfaction(weights, jobs[0]))
