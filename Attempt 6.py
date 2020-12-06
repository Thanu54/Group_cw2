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

#LANE1 FREQUENCIES
freq10_1=lane1[0::10]
freq20_1=lane1[1::10]
freq30_1=lane1[2::10]
freq40_1=lane1[3::10]
freq50_1=lane1[4::10]
freq60_1=lane1[5::10]
freq70_1=lane1[6::10]
freq80_1=lane1[7::10]
freq90_1=lane1[8::10]
freq100_1=lane1[9::10]

#LANE 2 FREQUENCIES
freq10_2=lane2[0::10]
freq20_2=lane2[1::10]
freq30_2=lane2[2::10]
freq40_2=lane2[3::10]
freq50_2=lane2[4::10]
freq60_2=lane2[5::10]
freq70_2=lane2[6::10]
freq80_2=lane2[7::10]
freq90_2=lane2[8::10]
freq100_2=lane2[9::10]

#LANE 3 FREQUENCIES
freq10_3=lane3[0::10]
freq20_3=lane3[1::10]
freq30_3=lane3[2::10]
freq40_3=lane3[3::10]
freq50_3=lane3[4::10]
freq60_3=lane3[5::10]
freq70_3=lane3[6::10]
freq80_3=lane3[7::10]
freq90_3=lane3[8::10]
freq100_3=lane3[9::10]

#LANE 4 FREQUENCIES
freq10_4=lane4[0::10]
freq20_4=lane4[1::10]
freq30_4=lane4[2::10]
freq40_4=lane4[3::10]
freq50_4=lane4[4::10]
freq60_4=lane4[5::10]
freq70_4=lane4[6::10]
freq80_4=lane4[7::10]
freq90_4=lane4[8::10]
freq100_4=lane4[9::10]

#LANE 5 FREQUENCIES
freq10_5=lane5[0::10]
freq20_5=lane5[1::10]
freq30_5=lane5[2::10]
freq40_5=lane5[3::10]
freq50_5=lane5[4::10]
freq60_5=lane5[5::10]
freq70_5=lane5[6::10]
freq80_5=lane5[7::10]
freq90_5=lane5[8::10]
freq100_5=lane5[9::10]

#LANE 6 FREQUENCIES
freq10_6=lane6[0::10]
freq20_6=lane6[1::10]
freq30_6=lane6[2::10]
freq40_6=lane6[3::10]
freq50_6=lane6[4::10]
freq60_6=lane6[5::10]
freq70_6=lane6[6::10]
freq80_6=lane6[7::10]
freq90_6=lane6[8::10]
freq100_6=lane6[9::10]

#LANE 7 FREQUENCIES
freq10_7=lane7[0::10]
freq20_7=lane7[1::10]
freq30_7=lane7[2::10]
freq40_7=lane7[3::10]
freq50_7=lane7[4::10]
freq60_7=lane7[5::10]
freq70_7=lane7[6::10]
freq80_7=lane7[7::10]
freq90_7=lane7[8::10]
freq100_7=lane7[9::10]

#LANE 8 FREQUENCIES
freq10_8=lane8[0::10]
freq20_8=lane8[1::10]
freq30_8=lane8[2::10]
freq40_8=lane8[3::10]
freq50_8=lane8[4::10]
freq60_8=lane8[5::10]
freq70_8=lane8[6::10]
freq80_8=lane8[7::10]
freq90_8=lane8[8::10]
freq100_8=lane8[9::10]

#LANE 9 FREQUENCIES
freq10_9=lane9[0::10]
freq20_9=lane9[1::10]
freq30_9=lane9[2::10]
freq40_9=lane9[3::10]
freq50_9=lane9[4::10]
freq60_9=lane9[5::10]
freq70_9=lane9[6::10]
freq80_9=lane9[7::10]
freq90_9=lane9[8::10]
freq100_9=lane9[9::10]


print("lane 1 after 10 steps: " + str(sum(freq10_1)))
print("lane 1 after 20 steps: " + str(sum(freq20_1)))
print("lane 1 after 30 steps: " + str(sum(freq30_1)))
print("lane 1 after 40 steps: " + str(sum(freq40_1)))
print("lane 1 after 50 steps: " + str(sum(freq50_1)))
print("lane 1 after 60 steps: " + str(sum(freq60_1)))
print("lane 1 after 70 steps: " + str(sum(freq70_1)))
print("lane 1 after 80 steps: " + str(sum(freq80_1)))
print("lane 1 after 90 steps: " + str(sum(freq80_1)))
print("lane 1 after 100 steps: " + str(sum(freq100_1)))

print("\n lane 2 after 10 steps: " + str(sum(freq10_2)))
print("lane 2 after 20 steps: " + str(sum(freq20_2)))
print("lane 2 after 30 steps: " + str(sum(freq30_2)))
print("lane 2 after 40 steps: " + str(sum(freq40_2)))
print("lane 2 after 50 steps: " + str(sum(freq50_2)))
print("lane 2 after 60 steps: " + str(sum(freq60_2)))
print("lane 2 after 70 steps: " + str(sum(freq70_2)))
print("lane 2 after 80 steps: " + str(sum(freq80_2)))
print("lane 2 after 90 steps: " + str(sum(freq90_2)))
print("lane 2 after 100 steps: " + str(sum(freq100_2)))

print("\nlane 3 after 10 steps: " + str(sum(freq10_3)))
print("lane 3 after 20 steps: " + str(sum(freq20_3)))
print("lane 3 after 30 steps: " + str(sum(freq30_3)))
print("lane 3 after 40 steps: " + str(sum(freq40_3)))
print("lane 3 after 50 steps: " + str(sum(freq50_3)))
print("lane 3 after 60 steps: " + str(sum(freq60_3)))
print("lane 3 after 70 steps: " + str(sum(freq70_3)))
print("lane 3 after 80 steps: " + str(sum(freq80_3)))
print("lane 3 after 90 steps: " + str(sum(freq90_3)))
print("lane 3 after 100 steps: " + str(sum(freq100_3)))

print("\nlane 4 after 10 steps: " + str(sum(freq10_4)))
print("lane 4 after 20 steps: " + str(sum(freq20_4)))
print("lane 4 after 30 steps: " + str(sum(freq30_4)))
print("lane 4 after 40 steps: " + str(sum(freq40_4)))
print("lane 4 after 50 steps: " + str(sum(freq50_4)))
print("lane 4 after 60 steps: " + str(sum(freq60_4)))
print("lane 4 after 70 steps: " + str(sum(freq70_4)))
print("lane 4 after 80 steps: " + str(sum(freq80_4)))
print("lane 4 after 90 steps: " + str(sum(freq90_4)))
print("lane 4 after 100 steps: " + str(sum(freq100_4)))

print("\nlane 5 after 10 steps: " + str(sum(freq10_5)))
print("lane 5 after 20 steps: " + str(sum(freq20_5)))
print("lane 5 after 30 steps: " + str(sum(freq30_5)))
print("lane 5 after 40 steps: " + str(sum(freq40_5)))
print("lane 5 after 50 steps: " + str(sum(freq50_5)))
print("lane 5 after 60 steps: " + str(sum(freq60_5)))
print("lane 5 after 70 steps: " + str(sum(freq70_5)))
print("lane 5 after 80 steps: " + str(sum(freq80_5)))
print("lane 5 after 90 steps: " + str(sum(freq90_5)))
print("lane 5 after 100 steps: " + str(sum(freq100_5)))

print("\nlane 6 after 10 steps: " + str(sum(freq10_6)))
print("lane 6 after 20 steps: " + str(sum(freq20_6)))
print("lane 6 after 30 steps: " + str(sum(freq30_6)))
print("lane 6 after 40 steps: " + str(sum(freq40_6)))
print("lane 6 after 50 steps: " + str(sum(freq50_6)))
print("lane 6 after 60 steps: " + str(sum(freq60_6)))
print("lane 6 after 70 steps: " + str(sum(freq70_6)))
print("lane 6 after 80 steps: " + str(sum(freq80_6)))
print("lane 6 after 90 steps: " + str(sum(freq90_6)))
print("lane 6 after 100 steps: " + str(sum(freq100_6)))

print("\nlane 7 after 10 steps: " + str(sum(freq10_7)))
print("lane 7 after 20 steps: " + str(sum(freq20_7)))
print("lane 7 after 30 steps: " + str(sum(freq30_7)))
print("lane 7 after 40 steps: " + str(sum(freq40_7)))
print("lane 7 after 50 steps: " + str(sum(freq50_7)))
print("lane 7 after 60 steps: " + str(sum(freq60_7)))
print("lane 7 after 70 steps: " + str(sum(freq70_7)))
print("lane 7 after 80 steps: " + str(sum(freq80_7)))
print("lane 7 after 90 steps: " + str(sum(freq90_7)))
print("lane 7 after 100 steps: " + str(sum(freq100_7)))

print("\nlane 8 after 10 steps: " + str(sum(freq10_8)))
print("lane 8 after 20 steps: " + str(sum(freq20_8)))
print("lane 8 after 30 steps: " + str(sum(freq30_8)))
print("lane 8 after 40 steps: " + str(sum(freq40_8)))
print("lane 8 after 50 steps: " + str(sum(freq50_8)))
print("lane 8 after 60 steps: " + str(sum(freq60_8)))
print("lane 8 after 70 steps: " + str(sum(freq70_8)))
print("lane 8 after 80 steps: " + str(sum(freq80_8)))
print("lane 8 after 90 steps: " + str(sum(freq90_8)))
print("lane 8 after 100 steps: " + str(sum(freq100_8)))

print("\nlane 9 after 10 steps: " + str(sum(freq10_9)))
print("lane 9 after 20 steps: " + str(sum(freq20_9)))
print("lane 9 after 30 steps: " + str(sum(freq30_9)))
print("lane 9 after 40 steps: " + str(sum(freq40_9)))
print("lane 9 after 50 steps: " + str(sum(freq50_9)))
print("lane 9 after 60 steps: " + str(sum(freq60_9)))
print("lane 9 after 70 steps: " + str(sum(freq70_9)))
print("lane 9 after 80 steps: " + str(sum(freq80_9)))
print("lane 9 after 90 steps: " + str(sum(freq90_9)))
print("lane 9 after 100 steps: " + str(sum(freq100_9)))



