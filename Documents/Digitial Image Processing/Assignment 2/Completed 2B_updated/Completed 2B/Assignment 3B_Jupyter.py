#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np

#flow of the code:
#given start location --> get rgb values --> get new new start location

def getRGB(location,grid, fileIn):
    neighbors = []
    #initial location is added :: BLUE ::EVEN
    neighbors.append(grid[location[0]][location[1]])

    #right from the initial location :: GREEN :: ODD
    copy = location[:]
    right = copy[1] + 1
    if right < len(grid[copy[0]]):
        neighbors.append(grid[copy[0]][right])
    
    #Down from the initial location :: RED ::EVEN
    copy = location[:]
    down = copy[0] + 1
    
    if down < len(grid[copy[1]]):
        neighbors.append(grid[down][copy[1]])
    
    #down_right from the initial location :: GREEN :: ODD
    copy = location[:]
    down_d = copy[0] + 1
    right_d = copy[1] + 1
    if down < len(grid[copy[1]]):
        neighbors.append(grid[down_d][right_d])


    #to return the rgb values...
    #the first and third elements of even index numbers are automatically added (0 and 2)

    rgb = []
    g1 = neighbors[1]
    g2 = neighbors[2]
    green = int((g1 + g2) /2)

    #add RED, GREEN, BLUE
    rgb.append(neighbors[3]) #RED
    rgb.append(green)
    rgb.append(neighbors[0]) #BLUE

    #expected value for the first location should be (8,5,0)
    fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')

    return rgb


# In[94]:


def getNewLocation(start, grid):
    new_location = []
    right = start[1] + 2 #from 0,0 it would be 0,2
    down = start[0] + 2 #from 0,0 it wopould 2,0
    
    #print('This is the starting location: ' + str(start))
    
    #when the current square is at the boundary
    if (start[0] == (len(grid[0]) -2) and start[1] == len(grid[1]) -2):
        print("This is the end of the grid!.")
        new_location = None
        return new_location
        
    #if the current location +2 is less than the length of the row of the current location, proceed to move right 2    
    elif right < len(grid[start[0]]): #510
        new_locationX = start[0]
        new_locationY = right #from the file, the new cell location is value 249...need to remind myself thatt here are multiple 24
        
        new_location.append(new_locationX)
        new_location.append(new_locationY)
        
        #print("Im in new location: " + str(new_location))
        return new_location #the return value will be 249 BECAUSE THE FIRST OCCURENCE OF 249 is at 0,2
                
    #when the current square has reached the bounds of the grid and there is more to convert
    elif right == len(grid[start[0]]):
        new_locationX = down
        new_locationY = 0 #from the file, the new cell location is value 249...need to remind myself thatt here are multiple 24
        
        new_location.append(new_locationX)
        new_location.append(new_locationY)
        
        #print("Im in new location: " + str(new_location))
        return new_location


# In[95]:


def main():
    starting = [0,0] #this is the border....by hard-code...so in as 512x512 the end borders would be [510,510]
    np_eight = np.arange(64).reshape(8,8)
    grid = np.ndarray.tolist(np_eight)
    for i in range(len(grid)):
        print(grid[i])
    string_vol = ''
    with open ('kseol_medium.txt') as vol: #name changes based on the txt file
        for p in vol.readlines():
            string_vol = p
    split = string_vol.split(',')
    pixel =[]
    for s in split:
        temp = int(s)
        pixel.append(temp)
    
    pixel_np = np.array(pixel).reshape(512,512)
    print(np.shape(pixel_np))
    grid1 = np.ndarray.tolist(pixel_np)
    
    #print(getNewLocation(starting,grid)) this is just a test
    
    newFile = open('kseol_medium_2B.txt','w+')
    newFile.write('RGB\n')
    newFile.write('256\n256\n')
    
    while(starting != None):
        getRGB(starting, grid1, newFile)
        starting = getNewLocation(starting, grid1)
    
    newFile.close()
    
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




