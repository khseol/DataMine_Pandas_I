#!/usr/bin/env python
# coding: utf-8

# In[40]:


def getRedFreq(rgb, red):

  #for loop for the red component
    for i in range(len(rgb)):
        if rgb[i][0] in red.keys():
            red[(rgb[i][0])] +=1
        else:
            red.update({rgb[i][0] : 1})

    return red


# In[41]:


def getGreenFreq(rgb, green):

  #for loop for the green component    
    for i in range(len(rgb)):
        if rgb[i][1] in green.keys():
            green[(rgb[i][1])] +=1
        else:
            green.update({rgb[i][1] : 1})
  

    return green


# In[42]:


def getBlueFreq(rgb, blue):

    #for loop for the blue component
    for i in range(len(rgb)):
        if rgb[i][2] in blue.keys():
            blue[(rgb[i][2])] +=1
        else:
            blue.update({rgb[i][2] : 1})
            
    return blue


# In[48]:


#Function for normalizing the frequencies
#This is the last part to do and then output the graph!!!
def normalize(component,normal_component):
    #To normalize a component...
    #frequency / total number of pixels ie. dimensions (256*256 and 512*512)
    for keys in component.keys():
        print('this is the current key: ' + str(keys))
        print('This is the current key vlaue: ' + str(component[keys]))
        normal = (component[keys] / (512*512)) #TOTAL NUMBER OF PIXELS CHANGES DEPENDING ON THE SIZE AND FILE BEING READ
        normal_component.update({keys:normal})
        print('current keys normalized value: ' + str(normal))
        
    return normal_component


# In[56]:


string_pixel = ''
pixel = []

#THIS VALUE CHANGES DEPENDING ON THE FILE BEING READ
with open ('kseol_hard.txt') as op:
    for i in op.readlines():
        string_pixel = i
        pixel.append(string_pixel.split())

#for-loop below changes the string number into int numbers
for i in range(len(pixel)):
    for j in range(len(pixel[i])):
        pixel[i][j] = int(pixel[i][j])

        
red_component = {}
green_component = {}
blue_component = {}

print('This is the red component\n')
red = getRedFreq(pixel,red_component)
normalize_r = {}
red_normal = normalize(red,normalize_r)

print('\nThis is the green component')
#print('this is for the green component')
green = getGreenFreq(pixel, green_component)
normalize_g = {}
green_normal = normalize(green,normalize_g)

print('\nThis is the blue component\n')
#print('this is for the blue component')
blue = getBlueFreq(pixel, blue_component)
normalize_b = {}
blue_normal = normalize(blue,normalize_b)


#these values and functions change depending on which component is being analyzed


# In[50]:


#######################################################################
#this section will have comments for each picture to avoid picture overlap

import matplotlib.pyplot as plot

#plot.bar(red_normal.keys(), red_normal.values(),1.5, color = 'r')
#plot.savefig('red_normal_hard.png')

plot.bar(green_normal.keys(), green_normal.values(),1.5, color = 'g')
plot.savefig('green_normal_hard.png')

#plot.bar(blue_normal.keys(), blue_normal.values(),1.5, color = 'b')
#plot.savefig('blue_normal_hard.png')


# In[ ]:




