import os
import csv



import dough



import random



import sauce



#os.chdir("/Users/christinelee/Documents/Github/HiMCM11140")



with open("rollingpin.csv") as csvfile:



reader = csv.reader(csvfile)



next(reader)



next(reader)



jobs = []



for row in reader:



temp = []



for char in "RIASEC":



temp.append(char in row[2])



jobs.append([row[0], float(row[1]), temp, float(row[5]), random.randint(1, 5)])



people = sauce.randPeople(10)



for person in people:



applicantvalues, weights = person



jobScores = []



for job in jobs:



jobvalues = dough.jobvaluesss(job[1:], applicantvalues)



jobScores.append((dough.satisfaction(weights, jobvalues), job))



jobScores.sort(key = lambda x: x[0])



print("Top five jobs for this random person:")



print(person)



for job in jobScores[::-1][:5]:



print(job)


print("\n")
