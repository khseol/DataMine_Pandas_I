# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:03:46 2020

@author: Kathy
"""

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
        
    print(neighbors)


    #to return the rgb values...
    #the first and third elements of even index numbers are automatically added (0 and 2)


    rgb = []
    #BG
    #RG
    #if the pattern of the square is regular:
    if columnBGB % 2 ==0:
      g1 = neighbors[1]
      g2 = neighbors[3]
      green = int((g1 + g2) /2)
      print(g1, g2, '/2', green)

      #add RED, GREEN, BLUE
      rgb.append(neighbors[2]) #RED
      rgb.append(green)
      rgb.append(neighbors[0]) #BLUE

      #expected value for the first location should be (8,5,0)
      print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
    
    else:
      g1 = neighbors[0]
      g2 = neighbors[2]
      green = green = int((g1 + g2) /2)
      print(g1, g2, '/2', green)

      #at this point, the pattern is GBGR, therefore the order from a linear standpoint is:
      rgb.append(neighbors[3])
      rgb.append(green)
      rgb.append(neighbors[1])
      print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')

    return neighbors

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
  print(neighbors)


    #to return the rgb values...
    #the first and third elements of even index numbers are automatically added (0 and 2)


    rgb = []
    #BG
    #RG
    #if the pattern of the square is regular:
    if columnRGR % 2 ==0:
      g1 = neighbors[1]
      g2 = neighbors[3]
      green = int((g1 + g2) /2)
      print(g1, g2, '/2', green)

      #add RED, GREEN, BLUE
      rgb.append(neighbors[0]) #RED
      rgb.append(green)
      rgb.append(neighbors[2]) #BLUE

      #expected value for the first location should be (8,5,0)
      print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
    
    else:
      g1 = neighbors[0]
      g2 = neighbors[2]
      green = green = int((g1 + g2) /2)
      print(g1, g2, '/2', green)

      #at this point, the pattern is GBGR, therefore the order from a linear standpoint is:
      rgb.append(neighbors[1])
      rgb.append(green)
      rgb.append(neighbors[3])
      print(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')
      fileIn.write(str(rgb[0]) +' '+ str(rgb[1]) +' '+ str(rgb[2]) + '\n')

    return neighbors



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

def main():
    starting = [0,0] #this is the border....by hard-code...so in as 512x512 the end borders would be [510,510]
    np_eight = np.arange(64).reshape(8,8)
    grid = np.ndarray.tolist(np_eight)
    for i in range(len(grid)):
        print(grid[i])


    #print(getRGB_other(starting, grid, counter))
    #starting = getNewLocation(starting, grid)
    #counter = 1
    #print(getRGB_other(starting,grid,counter))

    #main problem is to reset the column pattern counter after the square has reached the end...
    #by set up, starting has the function of being an xy coordinate where x- rows and y =columns...in this case

    newFile = open('testing,txt', 'w')
    newFile.write("RGB\n")
    newFile.write("8\n8\n")

    counterBGB = 0
    counterRGR = 0
    #code itself works, but will need to fix up the values...
    while(starting != None):
      if(starting[0]%2 == 0):
        
        print("This is counter : " + str(counterBGB))
        getRGB(starting, grid, counterBGB, newFile)
        starting = getNewLocation(starting, grid)
        print(starting)
        counterBGB +=1
      else:
       
        print("This is counter : " + str(counterRGR)) #this is the problem. the counter is not incrementing....
        getRGB_other(starting, grid, counterRGR, newFile)
        starting = getNewLocation(starting, grid)
        print(starting)
        counterRGR +=1

    print(get(RGB))

    newFile.close()      

if __name__ == "__main__":
    main()
