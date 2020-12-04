import csv
import random


#I've changed function1 so it now takes in 2 inputs (x and y co-ordinates
#of the probability table) and will output the correct probability 
def function1(x,y):
    last_turns=[]
    lanes=[]
    prob = open('probabilities.csv')
    readprob = csv.reader(prob)
    for column in readprob:
        last_turns.append(column[x])#appends entire given column
    #print(last_turns)
    lane_num=last_turns[y]
    print(lane_num) #prints correct row from given column


########################
#I still apply random.choices function which considers the weighted
#probabilities
    

direction = ['L','F','R']

#Already know initial step so I simulate the second step, given the
#first step

steps = ['F']#starting initially with an F
lane = [5]#starting initially in lane 5
prob2 = (0.3,0.4,0.3)
step=random.choices(direction,prob2)
steps.append(step[0])
print(steps)


#testing for the first 10 steps only
print("\nfor loop")          
for i in range(10):
    #determine the x value from the table by looking at the direction
    #of the previous 2 steps
    if (steps[-1]=='L') and (steps[-2]!='L'):
        x=1
    elif (steps[-1]=='L') and (steps[-2]=='L'):
        x=2
    elif (steps[-1]=='F') and (steps[-2]!='F'):
        x=3
    elif (steps[-1]=='F') and (steps[-2]=='F'):
        x=4
    elif (steps[-1]=='R') and (steps[-2]!='R'):
        x=5
    else:
        x=6
    #add to the list 'lane' to store which lane each step is taken in
    if step[-1]=="L":
        next_lane=lane[-1]-1
    elif step[-1]=="F":
        next_lane=lane[-1]
    else:
        next_lane=lane[-1]+1
    lane.append(next_lane)
    #determine the y value by looking at what lane the last step was in
    y=lane[-1]
    next_prob=function1(x,y)#call the relevent probability
    #print(next_prob)
    print(y)
    step=random.choices(direction,next_prob)#generate the direction of the
                                            #next step
    steps.append(step[0])#add this step to the steps list
    print(steps)
    #print(lane)
 
