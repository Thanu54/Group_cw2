#step 1 is a forward step in lane 5 so probabilities
#left=0.3 forward=0.4 right=0.3

import random
import csv

lanes=list(range(1,10))
#print(lanes)#the possible lanes

total_steps=1
forward_steps=1
left_steps=0
right_steps=0
'''
#headings= 1L, 2L, 1F, 2F, 1R, 2R
lane1=[(0.00,0.30,0.70),(0.00,0.40,0.60),(0.00,0.30,0.70),(0.00,0.20,0.80),NA,NA]
lane2=[(0.05,0.30,0.65),(0.10,0.40,0.55),(0.05,0.30,0.65),(0.05,0.25,0.70),(0.05,0.20,0.75),NA]
lane3=[(0.15,0.35,0.50),(0.25,0.40,0.35),(0.10,0.35,0.55),(0.05,0.30,0.65),(0.05,0.25,0.70),(0.05,0.20,0.75)]
lane4=[(0.30,0.35,0.35),(0.40,0.35,0.25),(0.20,0.35,0.45),(0.15,0.40,0.45),(0.10,0.35,0.55),(0.10,0.30,0.60)]
lane5=[(0.40,0.35,0.25),(0.50,0.30,0.20),(0.30,0.40,0.30),(0.25,0.50,0.25),(0.25,0.35,0.40),(0.20,0.30,0.50)]
lane6=[(0.55,0.35,0.10),(0.60,0.30,0.10),(0.45,0.35,0.20),(0.45,0.40,0.15),(0.35,0.35,0.30),(0.25,0.35,0.40)]
lane7=[(0.70,0.25,0.05),(0.75,0.20,0.05),(0.55,0.35,0.10),(0.65,0.30,0.05),(0.50,0.35,0.15),(0.35,0.40,0.25)]
lane8=[(0.75,0.20,0.05),NA,(0.65,0.30,0.05),(0.70,0.25,0.05),(0.65,0.30,0.05),(0.55,0.40,0.10)]
lane9=[NA,NA,(0.70,0.30,0.00),(0.80,0.20,0.00),(0.70,0.30,0.00),(0.60,0.40,0.00)]
'''
'''
lane1=[]
lane2=[]
lane3=[]
lane4=[]
lane5=[]
lane6=[]
lane7=[]
lane8=[]
lane9=[]

file=open('Probabilities.csv')
for line in file:
    for csv in line:
        lane1.append(csv)

file.close()
print(lane1)
'''
#current=4
#print(lanes[current])
#print(lanes[current-1])

for steps in range(101):
    current=4
    #print(lanes[current]) #step 1 is in lane 5
    options=[lanes[current-1],lanes[current],lanes[current+1]]
    probability=[0.3,0.4,0.3]
    random_lane=random.choices(options,probability)
    print('Man is now in lane'+str(random_lane)) #randomly generated new lane
    current=random_lane
    if random_lane==[lanes[current]]:
        forward_steps=forward_steps+1
    elif random_lane==[lanes[current-1]]:
        left_steps=left_steps+1
    else:
        right_steps=right_steps+1
    total_steps=forward_steps+left_steps+right_steps

print('Total number of steps forwards:' +str(forward_steps))
print('Total number of steps left:' +str(left_steps))
print('Total number of steps right:' +str(right_steps))

