import random
def AHP(): 
    chart = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    temp = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    sum = [0, 0, 0, 0, 0, 0]
    weights = [0, 0, 0, 0, 0, 0]
    weightedsum = [0, 0, 0, 0, 0, 0]
    lammax = 0
    consistency = 0
    CCorrect = False 
    for i in range(6):
        for z in range(6):
            if i == z:
                chart[i][z] = 1
            if chart[i][z] != 0:
                continue
            x = random.choice([1/i for i in range(1, 10)]+[i for i in range(1, 10)])
            chart[i][z] = x
            chart[z][i] = 1/x
    temp = chart

    #add sum of each column 
    for i in range(6):
        for z in range(6):
            sum[i] = sum[i] + chart[z][i]
    
    #divide each variable in column by sum of each column
    for i in range(6):
        for z in range(6):
            chart[z][i] = chart[z][i]/sum[i]
            
    #gives criteria weights
    for i in range(6):
        for z in range(6):
            weights[i] = chart[i][z] + weights[i]
        weights[i] = weights[i]/6
    #print(weights)
    
    #verifyingAHP
    for i in range(6):
        for z in range(6):
            temp[z][i] = weights[i] * temp[z][i]
    #findingweightesum
    for i in range(6):
        for z in range(6):
            weightedsum[i] = weightedsum[i] + temp[i][z]
    #dividing Criteria weights by weighted sums
    for i in range(6):
        weightedsum[i] = weights[i] / weightedsum[i]
    #Adding weightedsum/criteria weights to get lambda max
    for i in range(6):
        lammax = weightedsum[i] + lammax
        lammax = lammax / 6 #essentially taking average

    #consistency index is (lambda max - number of variables)/(num of variables -1)
    consistency = (lammax - 6) / (6 - 1)
    consistency = consistency / 1.24
    #1.24 is dependent on random index aka 6 variables

    if consistency < 0.1:
        CCorrect = True
    #print (CCorrect)
    return weights 

if __name__ == "__main__":
    for _ in range(10):
        print(AHP())

