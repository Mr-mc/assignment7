#!/usr/bin/env python
# coding: utf-8

# In[296]:


"""Michael Collins EECS690 assignment 7"""
import numpy as np
import random
"""globals"""
gamma = 1 # discounting rate
n = 0
firsttermepoc = -1
rewardSize = -1
gridSize = 5
terminationStates = [[0,0], [gridSize-1, gridSize-1]]
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
numiterations = 1000
prob_rtplus1_st_at =.25
prob_stplus1_st_at =.25
def actionRewardFunction(initialPosition, action):

    if initialPosition in terminationStates:
        return initialPosition, 0

    reward = rewardSize
    finalPosition = np.array(initialPosition) + np.array(action)
    if -1 in finalPosition or 5 in finalPosition:
        finalPosition = initialPosition

    return finalPosition, reward

valueMap = np.zeros((gridSize, gridSize))
states = [[i, j] for i in range(gridSize) for j in range(gridSize)]
#valueMap

# initialization
V = np.zeros((gridSize, gridSize))
returns = {(i, j):list() for i in range(gridSize) for j in range(gridSize)}
deltas = {(i, j):list() for i in range(gridSize) for j in range(gridSize)}
numiterations = 1000


# In[297]:


converge = False
t=0
deltas = []
def checkConvergence(deltas):

    #print(deltas[-1])
    deltas = np.array(deltas)
    countme = 0
    for all in deltas[-1]:
        if all == 0:
            countme+=1
        else:
#            print("not done", all)
            break
    if countme > 23:
        print("done found ", countme, "zeroes in deltas")
        numiterations == t
        return True
    else:
        return False
#deltas
#checkConvergence([0,0])

def setN(i):
    n = i
    return n
# In[298]:
def getN():
    return n

while converge == False:
    gotit = 0
    while True:#100):#nd converge:
        copyValueMap = np.copy(valueMap)
        t+=1
        deltaState = []
        for state in states:
            weightedRewards = []
            for action in actions:
                finalPosition, reward = actionRewardFunction(state, action)
                #print("final postion, rewards: ", finalPosition, reward)
                weightedRewards.append(reward+(valueMap[finalPosition[0], finalPosition[1]]))
                #print(weightedRewards)
            wrindex = np.argmax(weightedRewards)
            weightedRewards = np.max(weightedRewards)
            #print("weightedrewards index ", wrindex,"weighted reward max", weightedRewards)
            deltaState.append(np.abs(copyValueMap[state[0], state[1]]-weightedRewards))
            copyValueMap[state[0], state[1]] = weightedRewards
       #print(valueMap)
        deltas.append(deltaState)
        converge = checkConvergence(deltas)
        if(converge == True):
            n = t
            gotit = setN(t)
            nn = getN()
            #$$Rnumiterations = n
            print("Iteration ", nn , " is repeated of previous iteration ",gotit-1)
            #gotit = gotit-1
            #break
        valueMap = copyValueMap
        numiterations = gotit
        abc = getN()-1
        if t in [1,2,setN(getN()) ]:
           #print(numiterations)
            print("Iteration {}".format(t))
            print(valueMap)
            print("")
            if n < 10000 and converge == True:
                False
                break
