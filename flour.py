import os
import csv
import dough
import random
import sauce
#os.chdir("/Users/christinelee/Documents/Github/HiMCM11140")
with open("rollingpin.csv") as csvfile, open("results.txt") as distances:
    reader = csv.reader(csvfile)
    next(reader)
    next(reader)
    jobs = []
    for row in reader:
        temp = []
        for char in "RIASEC":
            temp.append(char in row[2])
        jobs.append([row[0], float(row[1]), temp, float(row[5]), int(row[6]), int(row[8]), row[4]])
    people = sauce.randPeople(10)
    jobScoresAll = {}
    for person in people:
        for _ in range(4):
            distances.readline()
        applicantvalues, weights = person
        jobScores = []
        for i, job in enumerate(jobs):
            commute = float(distances.readline().split()[-1])/3
            jobvalues = dough.jobvaluesss(job[1:]+[commute], applicantvalues)
            score = dough.satisfaction(weights, jobvalues)
            jobScores.append((score, job+[commute]))
            jobName = job[0] + " " + str(i)
            if jobName in jobScoresAll:
                jobScoresAll[jobName].append(score)
            else:
                jobScoresAll[jobName] = [score]
        jobScores.sort(key = lambda x: x[0])
        print("Top ten jobs for this random person:")
        print(person)
        with open("redpepper.csv", "w") as out:
            writer = csv.writer(out)
            writer.writerow([""] + people)
            for job in jobScoresAll:
                writer.writerow([job] + jobScoresAll[job])
        for job in jobScores[::-1][:10]:
            print(job)
        print("\n")
        
