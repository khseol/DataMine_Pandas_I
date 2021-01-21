# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:42:09 2020

@author: Kathy
"""

import numpy as np

string_vol = ''

with open ('kseol_easy.txt') as vol: #name changes based on the txt file
    for p in vol.readlines():
        string_vol = p

#each digit is considered a string...
split = string_vol.split(',')

pixel =[]
for s in split:
    #type conversion
    temp = int(s)
    pixel.append(temp)

new_file = open('kseol_easy_RGB_2A.txt', 'w+') #changes and depends on the file
new_file.write('RGB\n')
new_file.write('512\n512\n') #values change depending on which file im using

pixel_np = np.array(pixel).reshape(512,512)
print(np.shape(pixel_np))

grid = np.ndarray.tolist(pixel_np)


#because the bayer filter goes througha GBG and RGR etc kind of pattern per evey line
#every even row is goes by the pattern og GBG and odd rows are GRG...
#per row, there is a limit of 256 columns

#first value is a green component and seconf value is green,

#after inquiry, the pattern of even is BGB and odd is RGR

to_str = ''
for rows in range(len(grid)):
    for cells in range(len(grid[rows])):
        if rows %2 == 0: #the even rows will hold the pattern of GBG
            if cells %2 == 0: #each cell of the row will be either G(even) or B(odd)
                
                #i'm having a brain attack
                #R - red G -green B-blue
                #mixing up the pattern to have twice as many blues....
                #below is the correct order
                
                to_str = to_str = '0 0 ' + str(grid[rows][cells]) + '\n'
                new_file.write(to_str)
                #print(to_str)
            else:
                #if the cell index is odd, then G
                to_str = '0 ' + str(grid[rows][cells]) + ' 0\n'
                new_file.write(to_str)
                #print(to_str)
        else:
            #for odd rows that have the pattern RGR
            if cells %2 == 0: #the color is G
                to_str = '0 ' + str(grid[rows][cells]) + ' 0\n'
                new_file.write(to_str)
                #print(to_str)
            else:
                #the cells are R
                to_str = str(grid[rows][cells]) + ' 0 0\n'
                new_file.write(to_str)
                #print(to_str)

new_file.close()
vol.close()
