import csv
import dough
import flour
from ast import literal_eval as makeTuple
#import numpy as np

with open("redpepper.csv") as file:
    reader = csv.reader(file)
    people = next(reader)
    values, weights = makeTuple(people[1])
    for index in range(len(weights)):
        x = weights[index] * 0.05
        newWeights = [n + x/5 if i != index else n - x for i, n in enumerate(weights)]
        newScores = dough.getJobScores([(values, newWeights)])
        print("Top 10 Jobs:")
        flour.printTopN(10, newScores[0])
        print()

    #for row in reader:
        #greenpepper = [float(n) for n in row[1:]]
        #print(row[0] + "\nMean Score: " + str(np.mean(greenpepper)) + "\nStdev: " + str(np.std(greenpepper)) + "\n")


