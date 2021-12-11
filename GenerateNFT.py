# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:33:44 2021

@author: Mahmut Can Gonol
"""

from PIL import Image
import random
 
 

print("Don't forget only file png")
array = []
count_values = input("Enter a how many different title a variable: ")
if count_values.isdigit():
    count=0
    while True:
        value = input(f"{count}.Title Enter a image a png format: ")
        if value=="exit":
            count+=1
            array.append(str(count))
            if count >=int(count_values):
                break
        elif value=="fullexit":
            break
        else:
            if '.png' in value:
                array.append(value)
                
            else:
                print("Error. Please enter '.png' file")

is_empty = False    
for i in range(len(array)):
   if len(array) == 0:
       is_empty = True

is_error = False
if is_empty == False:
    variables = []
    for i in range(len(array)):
        if array[i].isdigit() == False:
            
            variables.append(array[i])
    images = []
    for i in range(len(variables)):
        try:
            img = Image.open(variables[i]).convert('RGBA')
            img.putalpha(1)
            print(img)
            images.append(img)
        except:
            is_error = True
            print("We detect denised file!")
    
     
    if is_error==False:
        for i in range(len(images)):
           if i!=0:
               x,y = images[i].size
               images[0].paste(images[i],(random.randint(0,x),random.randint(0,y)))             
         
        images[0].show()   

        
        
        













