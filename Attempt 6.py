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
lane1=[]
lane2=[]
lane3=[]
lane4=[]
lane5=[]
lane6=[]
lane7=[]
lane8=[]
lane9=[]

for k in range(20):
    
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
        lane1_freq=lane_count.count(1)
        lane1.append(lane1_freq)
        lane2_freq=lane_count.count(2)
        lane2.append(lane2_freq)
        lane3_freq=lane_count.count(3)
        lane3.append(lane3_freq)
        lane4_freq=lane_count.count(4)
        lane4.append(lane4_freq)
        lane5_freq=lane_count.count(5)
        lane5.append(lane5_freq)
        lane6_freq=lane_count.count(6)
        lane6.append(lane6_freq)
        lane7_freq=lane_count.count(7)
        lane7.append(lane7_freq)
        lane8_freq=lane_count.count(8)
        lane8.append(lane8_freq)
        lane9_freq=lane_count.count(9)
        lane9.append(lane9_freq)


#The following section prints out the sum of the total frequency spent in each lane
    #in the entire simulation, not each separate simulation.
#We use the sum function to find the total frequency spent in each lane throughout
    #the entire simulation

        
for n in range(1,11): #the range is for the number of lanes (9)
    count = 10*n
    print("lane 1 after " + str(count) + " steps: " + str(sum(lane1[n::10])))
print("\n")
#the last 4 lines was only for lane 1
#they have been repeated for the rest of the lanes in the following code.
for n in range(1,11):
    count = 10*n
    print("lane 2 after " + str(count) + " steps: " + str(sum(lane2[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 3 after " + str(count) + " steps: " + str(sum(lane3[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 4 after " + str(count) + " steps: " + str(sum(lane4[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 5 after " + str(count) + " steps: " + str(sum(lane5[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 6 after " + str(count) + " steps: " + str(sum(lane6[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 7 after " + str(count) + " steps: " + str(sum(lane7[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 8 after " + str(count) + " steps: " + str(sum(lane8[n::10])))
print("\n")
for n in range(1,11):
    count = 10*n
    print("lane 9 after " + str(count) + " steps: " + str(sum(lane9[n::10])))
print("\n")


