import csv
import random

#I've changed function1 so it now takes in 2 inputs (x and y co-ordinates
#of the probability table) and will output the correct probability 
def function1(x,y):
    last_turns=[]
    lanes=[]
    prob = open('Probabilities.csv')
    readprob = csv.reader(prob)
    for column in readprob:
        last_turns.append(column[x])#appends entire given column
    #print(last_turns)
    lane_prob=last_turns[y]
    prob.close()
    words=lane_prob.strip("()")
    words2=words.split(",")
    a=[]
    for i in words2:
        a.append(float(i))
    return a #prints correct row from given column
    

direction = ['L','F','R']
for k in range(5):
    
    #Already know initial step so I simulate the second step
    steps = ['F']
    lane = [5]
    prob2 = (0.30,0.40,0.30)
    step=random.choices(direction,weights=prob2,k=1)
    steps.append(step[0])

    #print("\nfor loop")          
    for i in range(100):
        #print("\n")
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
        if steps[-1]=='L': #changed step to steps
            next_lane=lane[-1]-1
        elif steps[-1]=='F':
            next_lane=lane[-1]
        else:
            next_lane=lane[-1]+1
        lane.append(next_lane)
        #determine the y value by looking at what lane the last step was in
        y=lane[-1]
        #function1(x,y)
        next_prob=function1(x,y)#call the relevent probability
        #print(next_prob)
        #print('Lane: '+str(y))
        step=random.choices(direction,weights=next_prob,k=1)
        steps.append(step[0])#add this step to the steps list
        #print(steps)
        #print(lane)

for i in range(10,101,10):
    lane_count=lane[0:i]
    print('\nFrequencies for the first '+str(i)+' steps')
    lane1_freq=lane_count.count(1)
    print('Lane 1: ' + str(lane1_freq))
    lane2_freq=lane_count.count(2)
    print('Lane 2: ' + str(lane2_freq))
    lane3_freq=lane_count.count(3)
    print('Lane 3: ' + str(lane3_freq))
    lane4_freq=lane_count.count(4)
    print('Lane 4: ' + str(lane4_freq))
    lane5_freq=lane_count.count(5)
    print('Lane 5: ' + str(lane5_freq))
    lane6_freq=lane_count.count(6)
    print('Lane 6: ' + str(lane6_freq))
    lane7_freq=lane_count.count(7)
    print('Lane 7: ' + str(lane7_freq))
    lane8_freq=lane_count.count(8)
    print('Lane 8: ' + str(lane8_freq))
    lane9_freq=lane_count.count(9)
    print('Lane 9: ' + str(lane9_freq))
        

