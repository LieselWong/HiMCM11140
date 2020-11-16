import dough
import sauce
import csv

jobs = dough.getJobs()
def printTopN(n, scores):
    topIndices = sorted(range(len(scores)), key=lambda x: -scores[x])[:n]
    for i in topIndices:
        print(f"{scores[i]:.3f}, "+jobs[i][0])

if __name__ == "__main__":
    people = sauce.randPeople(10)
    scores = dough.getJobScores(people)
    for i in range(len(scores)):
        print("Top 10 Jobs for Person "+str(i))
        printTopN(10, scores[i])
        print()
    with open("redpepper.csv", "w") as out:
        writer = csv.writer(out)
        writer.writerow([""] + people)
        scores = [list(i) for i in zip(*scores)]
        for i in range(len(jobs)):
            writer.writerow([jobs[i][0]] + scores[i])

