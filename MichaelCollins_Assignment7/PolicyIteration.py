#!/usr/bin/env python
# coding: utf-8

# In[632]:


"""Michael Collins EECS690 assignment 7"""
import numpy as np
import matplotlib.pyplot as plt
import random
"""globals"""
gamma = 1 # discounting rate
firsttermepoc = -1
rewardSize = -1
gridSize = 5
terminationStates = [[0,0], [gridSize-1, gridSize-1]]
actions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
numIterations = 5000
prob_rtplus1_st_at =.25
prob_stplus1_st_at =.25
deltas = []
numiterations = numIterations
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
def actionRewardFunction(initialPosition, action):

    if initialPosition in terminationStates:
        return initialPosition, 0

    reward = rewardSize
    finalPosition = np.array(initialPosition) + np.array(action)
    if -1 in finalPosition or 5 in finalPosition:
        finalPosition = initialPosition

    return finalPosition, reward


# In[633]:


valueMap = np.zeros((gridSize, gridSize))
states = [[i, j] for i in range(gridSize) for j in range(gridSize)]


# In[634]:


converge = []
c = []
t = 0
final_t = 0
DONE = False
for it in range(numIterations):
    copyValueMap = np.copy(valueMap)
    t+=1
    deltaState = []
    for state in states:
        weightedRewards = 0
        for action in actions:
            finalPosition, reward = actionRewardFunction(state, action)
            weightedRewards += (1/len(actions))*(reward+(valueMap[finalPosition[0], finalPosition[1]]))
        deltaState.append(np.abs(copyValueMap[state[0], state[1]]-weightedRewards))
        copyValueMap[state[0], state[1]] = weightedRewards
    deltas.append(deltaState)
   # print(deltas[-1])
    c = np.subtract(valueMap, copyValueMap)
    converge = checkConvergence(deltas)
    if(converge == True):
        print(converge, t)
        final_t = t
    # IMPORTANT
    # np.sum is(not true anymore I changed it to deltas) used because float values became so small the probability that it was diverging was already happening. sum all values and subtract total difference causes some rounding.
    # deltas(difference between last q state and this q state for all rows and columns) was not used because values were very small but deltas will prove convergence.
    # The way I do it leaves possiblity of non-convergence but it's not probable : storage =(np.sum(valueMap, dtype = np.float32))-( np.sum(copyValueMap, dtype = np.float32))
    # In example below the function checkConvergence says that the true DELTAS being zero means there is confirmed convergence however
    # I found that I could notice convergence sooner by taking the sum of valueMap and copyValueMap as float32 then subtracting the difference. This leads to some rounding issues which is good
    # compare  deltas[-1] at iteration 401 and 1200. Deltas at 400 are very small but not 0.
    # Notice iteration 401 and 1200 are rounding(converging) very slowly to the 0.000_  place. -34.33295828 vs. -34.33333333
    # difference between sum of values of last iteration to this iteration(to test convergence) is 0. Stop iterating immediately sum of a - sum of b =  -793.3285 -  -793.3285 = 0.0 False
    # in the above line we get a value of 0.0 from np.sum(array1 )-np.sum(array2) but we get False statement which means the change in last iteration to this was very small but not exactly 0 for every row and column BUT CLOSE ENOUGH
    # We don't get the final iteration that it truly converges we just get an early estimation.
    """Iteration 422
    [[  0.         -22.99986569 -34.33312708 -39.66642405 -41.66640961]
     [-22.99986569 -30.66648508 -36.33311466 -38.99976269 -39.66642405]
     [-34.33312708 -36.33311466 -37.33310834 -36.33311466 -34.33312708]
     [-39.66642405 -38.99976269 -36.33311466 -30.66648508 -22.99986569]
     [-41.66640961 -39.66642405 -34.33312708 -22.99986569   0.        ]]"""
    """Iteration 1200
    [[  0.         -23.         -34.33333333 -39.66666667 -41.66666667]
     [-23.         -30.66666667 -36.33333333 -39.         -39.66666667]
     [-34.33333333 -36.33333333 -37.33333333 -36.33333333 -34.33333333]
     [-39.66666667 -39.         -36.33333333 -30.66666667 -23.        ]
     [-41.66666667 -39.66666667 -34.33333333 -23.           0.        ]]"""
    # In my opinion I imagine it would be hard to prove that Iteration 422 doesn't guarantee convergence but I believe that everything must converge by the next iteration*3 and since we know deltas are 0 at 1200 this idea works.
    storage =(np.sum(valueMap, dtype = np.float32))-( np.sum(copyValueMap, dtype = np.float32))
    numIt = 0
    if storage == 0.0:
        #print("difference between sum of values of last iteration to this iteration(to test convergence) is 0. Stop iterating immediately ", np.sum(valueMap, dtype = np.float32), "- ",np.sum(copyValueMap, dtype = np.float32), "=", storage, converge )
        numIt = t
        DONE = True
    valueMap = copyValueMap
    if it in [0,9,numIt,final_t-1]:
        print("Iteration {}".format(it+1))
        print(valueMap)
        print("")
    if (DONE== True) and converge == True:
        break


# In[ ]:





# In[ ]:
