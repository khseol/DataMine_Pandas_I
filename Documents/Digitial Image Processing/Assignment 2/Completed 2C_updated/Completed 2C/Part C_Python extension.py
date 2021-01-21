#!/usr/bin/env python
# coding: utf-8

# In[109]:


import numpy as np

#flow of the code:
#given start location --> get rgb values --> get new new start location

def getRGB(location,grid, columnBGB, fileIn):
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
    #BG
    #GR
    
    #so BGGR
    #and GBRG
    #if the pattern of the square is regular:
    if columnBGB % 2 ==0:
      g1 = neighbors[1]
      g2 = neighbors[2]
      green = int((g1 + g2) /2)
      #print(g1, g2, '/2', green)

      #add RED, GREEN, BLUE
      rgb.append(neighbors[3]) #RED
      rgb.append(green)
      rgb.append(neighbors[0]) #BLUE

      #expected value for the first location should be (8,5,0)
      #print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')

    else:
      g1 = neighbors[0]
      g2 = neighbors[3]
      green = int((g1 + g2) /2)
      #print(g1, g2, '/2', green)

      #at this point, the pattern is GBGR, therefore the order from a linear standpoint is:
      rgb.append(neighbors[2])
      rgb.append(green)
      rgb.append(neighbors[1])
      #print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')

    return neighbors


# In[110]:


def getRGB_other(location, grid, columnRGR, fileIn):

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
    #GR
    #BG
    
    #so GRBG
    #and RGGB
    #if the pattern of the square is regular:
    if columnRGR % 2 ==0:
      g1 = neighbors[0]
      g2 = neighbors[3]
      green = int((g1 + g2) /2)
      #print(g1, g2, '/2', green)

      #add RED, GREEN, BLUE
      rgb.append(neighbors[1]) #RED
      rgb.append(green)
      rgb.append(neighbors[2]) #BLUE

      #expected value for the first location should be (8,5,0)
      #print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
    
    else:
      g1 = neighbors[1]
      g2 = neighbors[2]
      green = green = int((g1 + g2) /2)
      #print(g1, g2, '/2', green)

      #at this point, the pattern is GBGR, therefore the order from a linear standpoint is:
      rgb.append(neighbors[0])
      rgb.append(green)
      rgb.append(neighbors[3])
      #print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')

    return neighbors


# In[111]:


def getNewLocation(start, grid):
    new_location = []
    right = start[1] + 1 #from 0,0 it would be 0,2
    down = start[0] + 1 #from 0,0 it wopould 2,0
    
    #print('This is the starting location: ' + str(start))
    
    #when the current square is at the boundary
    if (start[0] == (len(grid[0]) -2) and start[1] == len(grid[1]) -2):
        print("This is the end of the grid!.")
        new_location = None
        return new_location
        
    #if the current location +2 is less than the length of the row of the current location, proceed to move right 2    
    elif right < len(grid[start[0]])-1: #510
        new_locationX = start[0]
        new_locationY = right #from the file, the new cell location is value 249...need to remind myself thatt here are multiple 24
        
        new_location.append(new_locationX)
        new_location.append(new_locationY)
        
        #print("Im in new location: " + str(new_location))
        return new_location #the return value will be 249 BECAUSE THE FIRST OCCURENCE OF 249 is at 0,2
                
    #when the current square has reached the bounds of the grid and there is more to convert
    elif right == len(grid[start[0]])-1:
        new_locationX = down
        new_locationY = 0 #from the file, the new cell location is value 249...need to remind myself thatt here are multiple 24
        
        new_location.append(new_locationX)
        new_location.append(new_locationY)
        
        #print("Im in new location: " + str(new_location))
        return new_location


# In[112]:


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
    
    newFile = open('kseol_medium_2C.txt','w+') #this section changes based on text files
    newFile.write('RGB\n')
    newFile.write('511\n511\n')
    
    counterBGB = 0
    counterRGR = 0
    while(starting!= None):
        if (starting[0]% 2 ==0):
            getRGB(starting,grid1,counterBGB,newFile)
            starting = getNewLocation(starting, grid1)
            counterBGB +=1
        else:
            getRGB_other(starting,grid1,counterBGB,newFile)
            starting = getNewLocation(starting, grid1)
            counterRGR +=1
    
    newFile.close()
    vol.close()
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




