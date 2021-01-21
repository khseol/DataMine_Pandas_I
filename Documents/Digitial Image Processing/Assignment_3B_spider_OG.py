import os
from Coded_3A_spider import *

#%%
#the function to find the average frequency of each intensities
#formula will go as:
# 
# summation of some color intensity frequency i 
#_______________________________________________________________________________________ = average
# The number of times the color insntisty has appeared on the set, ie. the txt files, N

#if the set does not have the frequency of the color intensity, the value will be zero, but the N will remain the same regardless as it the total number
#of the sets we have.
def getNormals(triplet, total):
    p_r = {}
    p_g = {}
    p_b = {}
    pixel_R = getRedFreq(triplet, p_r)
    pixel_G = getGreenFreq(triplet, p_g)
    pixel_B =getBlueFreq(triplet, p_b)
    
    
    
    return pixel_R, pixel_G, pixel_B 



#%% 
#this will be used to obtain the average of a color component from each type of object
def getAverage(n1,n2,n3,n4,n5,n6,n7,n8,n9):
    dummy = {}
    avg = {}
    for i in n1.keys():
        dummy.update({i: n1[i]})
    for i in n2.keys():
        if i in dummy.keys():
            update = n2[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n2[i]})
    for i in n3.keys():
        if i in dummy.keys():
            update = n3[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n3[i]})
    for i in n4.keys():
        if i in dummy.keys():
            update = n4[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n4[i]})
    for i in n5.keys():
        if i in dummy.keys():
            update = n5[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n5[i]})
    for i in n6.keys():
        if i in dummy.keys():
            update = n6[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n6[i]})
    for i in n7.keys():
        if i in dummy.keys():
            update = n7[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n7[i]})
    for i in n8.keys():
        if i in dummy.keys():
            update = n8[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n8[i]})
    for i in n9.keys():
        if i in dummy.keys():
            update = n9[i] + dummy[i]
            dummy.update({i:update})
        else:
            dummy.update({i: n9[i]})
    
    for i in dummy.keys():
        avg.update({i: dummy[i]/9})
    
        
    
    return avg
        

#%%: for ball


#below is the test to see if i can access a file from a directory of specific coded name
file_path = ".\\easy\\ball\\"
file_list = []
for files in sorted(os.listdir(file_path)):
    file_list.append(files)
#################################################    
test_path1 = file_path + '\\' + file_list[0]
print(file_list[0])
p1,t1 = getPixels(test_path1)
ball_nR1, ball_nG1, ball_nB1 = getNormals(p1,t1)
red_ball = {}
green_ball = {}
blue_ball = {}
red_ball_1 = getRedFreq(p1,red_ball)
green_ball_1 = getGreenFreq(p1,green_ball)
blue_ball_1 = getBlueFreq(p1,blue_ball)
red_ball = {}
green_ball = {}
blue_ball = {}
red_ball_1n = normalize(red_ball_1,red_ball,t1)
green_ball_1n = normalize(green_ball_1,green_ball,t1)
blue_ball_1n = normalize(blue_ball_1,blue_ball,t1)
print(red_ball_1)
print(red_ball_1n)
red_hist(red_ball_1n)

#################################################
test_path1 = file_path + '\\' + file_list[1]
p2,t2 = getPixels(test_path1)
#below coded for some reason fixes the multiple iteration count when i put it as a separate function...
red_ball = {}
green_ball = {}
blue_ball = {}
red_ball_2 = getRedFreq(p2,red_ball)
green_ball_2 = getGreenFreq(p2,green_ball)
blue_ball_2 = getBlueFreq(p2,blue_ball)
red_ball = {}
green_ball = {}
blue_ball = {}
red_ball_2n = normalize(red_ball_2,red_ball,t2)
green_ball_2n = normalize(green_ball_2,green_ball,t2)
blue_ball_2n = normalize(blue_ball_2,blue_ball,t2)

##################################################
test_path1 = file_path + '\\' + file_list[2]
p3,t3 = getPixels(test_path1)
ball_nR3, ball_nG3, ball_nB3 = getNormals(p3,t3)
#################################################
test_path1 = file_path + '\\' + file_list[3]
p4,t4 = getPixels(test_path1)
ball_nR4, ball_nG4, ball_nB4 = getNormals(p4,t4)
#################################################
test_path1 = file_path + '\\' + file_list[4]
p5,t5 = getPixels(test_path1)
ball_nR5, ball_nG5, ball_nB5 = getNormals(p5,t5)
#################################################
test_path1 = file_path + '\\' + file_list[5]
p6,t6 = getPixels(test_path1)
ball_nR6, ball_nG6, ball_nB6 = getNormals(p6,t6)
#################################################
test_path1 = file_path + '\\' + file_list[6]
p7,t7 = getPixels(test_path1)
ball_nR7, ball_nG7, ball_nB7 = getNormals(p7,t7)
#################################################
test_path1 = file_path + '\\' + file_list[7]
p8,t8 = getPixels(test_path1)
ball_nR8, ball_nG8, ball_nB8 = getNormals(p8,t8)
#################################################
test_path1 = file_path + '\\' + file_list[8]
p9,t9 = getPixels(test_path1)
ball_nR9, ball_nG9, ball_nB9 = getNormals(p9,t9)

ballMeanR = getAverage(ball_nR1, ball_nR2, ball_nR3, ball_nR4, ball_nR5, ball_nR6, ball_nR7, ball_nR8, ball_nR9)
#print(ballMeanR)
#red_hist(ballMeanR)
#ballMeanG = getAverage(ball_nG1, ball_nG2, ball_nG3, ball_nG4, ball_nG5, ball_nG6, ball_nG7, ball_nG8, ball_nG9)
#green_hist(ballMeanG)
#ballMeanB = getAverage(ball_nB1, ball_nB2, ball_nB3, ball_nB4, ball_nB5, ball_nB6, ball_nB7, ball_nB8, ball_nB9)
#blue_hist(ballMeanB)

#%%for brick 

file_path2 = ".\\easy\\brick\\"
file_list2 = []
for files in sorted(os.listdir(file_path2)):
    file_list2.append(files)
    
test_path2 = file_path2 + '\\' + file_list2[0]
p1_2,t1_2 = getPixels(test_path2)
brick_nR1, brick_nG1, brick_nB1 = getNormals(p1_2,t1_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[1]
p2_2,t2_2 = getPixels(test_path2)
brick_nR2, brick_nG2, brick_nB2 = getNormals(p2_2,t2_2)
##################################################
test_path2 = file_path2 + '\\' + file_list2[2]
p3_2,t3_2 = getPixels(test_path2)
brick_nR3, brick_nG3, brick_nB3 = getNormals(p3_2,t3_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[3]
p4_2,t4_2 = getPixels(test_path2)
brick_nR4, brick_nG4, brick_nB4 = getNormals(p4_2,t4_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[4]
p5_2,t5_2 = getPixels(test_path2)
brick_nR5, brick_nG5, brick_nB5 = getNormals(p5_2,t5_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[5]
p6_2,t6_2 = getPixels(test_path2)
brick_nR6, brick_nG6, brick_nB6 = getNormals(p6_2,t6_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[6]
p7_2,t7_2 = getPixels(test_path2)
brick_nR7, brick_nG7, brick_nB7 = getNormals(p7_2,t7_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[7]
p8_2,t8_2 = getPixels(test_path2)
brick_nR8, brick_nG8, brick_nB8 = getNormals(p8_2,t8_2)
#################################################
test_path2 = file_path2 + '\\' + file_list2[8]
p9_2,t9_2 = getPixels(test_path2)
brick_nR9, brick_nG9, brick_nB9 = getNormals(p9_2,t9_2)


#brickMeanR = getAverage(brick_nR1, brick_nR2, brick_nR3, brick_nR4, brick_nR5, brick_nR6, brick_nR7, brick_nR8, brick_nR9)
#red_hist(brickMeanR)
#brickMeanG = getAverage(brick_nG1, brick_nG2, brick_nG3, brick_nG4, brick_nG5, brick_nG6, brick_nG7, brick_nG8, brick_nG9)
#green_hist(brickMeanG)
#brickMeanB = getAverage(brick_nB1, brick_nB2, brick_nB3, brick_nB4, brick_nB5, brick_nB6, brick_nB7, brick_nB8, brick_nB9)
#blue_hist(brickMeanB)

#%%for cylinder
file_path3 = ".\\easy\\cylinder\\"
file_list3 = []
for files in sorted(os.listdir(file_path3)):
    file_list3.append(files)
    
test_path3 = file_path3 + '\\' + file_list3[0]
p1_3,t1_3 = getPixels(test_path3)
cy_nR1, cy_nG1, cy_nB1 = getNormals(p1_3,t1_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[1]
p2_3,t2_3 = getPixels(test_path3)
cy_nR2, cy_nG2, cy_nB2 = getNormals(p2_3,t2_3)
##################################################
test_path3 = file_path3 + '\\' + file_list3[2]
p3_3,t3_3 = getPixels(test_path3)
cy_nR3, cy_nG3, cy_nB3 = getNormals(p3_3,t3_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[3]
p4_3,t4_3 = getPixels(test_path3)
cy_nR4, cy_nG4, cy_nB4 = getNormals(p4_3,t4_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[4]
p5_3,t5_3 = getPixels(test_path3)
cy_nR5, cy_nG5, cy_nB5 = getNormals(p5_3,t5_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[5]
p6_3,t6_3 = getPixels(test_path3)
cy_nR6, cy_nG6, cy_nB6 = getNormals(p6_3,t6_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[6]
p7_3,t7_3 = getPixels(test_path3)
cy_nR7, cy_nG7, cy_nB7 = getNormals(p7_3,t7_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[7]
p8_3,t8_3 = getPixels(test_path3)
cy_nR8, cy_nG8, cy_nB8 = getNormals(p8_3,t8_3)
#################################################
test_path3 = file_path3 + '\\' + file_list3[8]
p9_3,t9_3 = getPixels(test_path3)
cy_nR9, cy_nG9, cy_nB9 = getNormals(p9_3,t9_3)


#cyMeanR = getAverage(cy_nR1, cy_nR2, cy_nR3, cy_nR4, cy_nR5, cy_nR6, cy_nR7, cy_nR8, cy_nR9)
#red_hist(cyMeanR)
#cyMeanG = getAverage(cy_nG1, cy_nG2, cy_nG3, cy_nG4, cy_nG5, cy_nG6, cy_nG7, cy_nG8, cy_nG9)
#green_hist(cyMeanG)
#cyMeanB = getAverage(cy_nB1, cy_nB2, cy_nB3, cy_nB4, cy_nB5, cy_nB6, cy_nB7, cy_nB8, cy_nB9)
#blue_hist(cyMeanB)




#%%for test
