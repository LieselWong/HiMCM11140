import csv
import numpy as np

with open("redpepper.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        greenpepper = [float(n) for n in row[1:]]
        print(row[0] + "\nMean Score: " + str(np.mean(greenpepper)) + "\nStdev: " + str(np.std(greenpepper)) + "\n")

