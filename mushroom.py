import csv
import dough
import flour
from ast import literal_eval as makeTuple

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

