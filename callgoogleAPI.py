# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:06:09 2018

@author: phott
"""

import io
import os
import cv2
import pandas as pd
import numpy as np

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\communist\My First Project-9ff19115ad07.json"



imagepath = "C:/Users/phott/Desktop/1073742152_2014-09-13_730_JPY.jpg"


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    #Make an empty dataframe with columns 'character' and 'vertices'
    data = {'character':[],'vertices':[]}
    character = pd.DataFrame(data)

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    for text in texts:
        #print('\n"{}"'.format(text.description))

        vertices = (['{},{}'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))
        # Append word into a data frame
        character = character.append({'character': text.description,'vertices': vertices},ignore_index=True)
        
    return character
        

        
        

  


t1 = cv2.getTickCount() #Đếm thời gian - Huyền thoại

character = detect_text(imagepath)

t2 = cv2.getTickCount() #Đếm thời gian - Huyền thoại

time = (t2 - t1)/ cv2.getTickFrequency() #Đếm thời gian - Huyền thoại

#sum1 = 0

'''
for i in range(len(data['character'])):
    sum = sum + len(data['character'][i])


for i in range(1,len(character['character'])):
    sum1 = sum1 + len(character['character'][i])
'''


mystr = character['character'][0]
mystr = mystr.strip().split()

#s2 = 0

#for x in mystr:
#    s2 = s2 + len(x)
    


result = []
j = 0
k = 0
chIndex = 1
#print(character['character'][chIndex])
#print('j k',j, k)
#print('chIndex',chIndex)
for i in range(len(mystr)):
    position = []
    k += len(mystr[i])
    j += len(character['character'][chIndex])
    position.append(character['vertices'][chIndex][0])
    position.append(character['vertices'][chIndex][3])
    while (j < k ):
        chIndex+=1
        j += len(character['character'][chIndex])
        #print(character['character'][chIndex])
        #print('j k',j, k)
        #print('chIndex',chIndex)
    position.append(character['vertices'][chIndex][1])
    position.append(character['vertices'][chIndex][2])
    result.append(position)
    chIndex+=1

#Change position of the pixel to be in the same format of Google API
for i in range(len(result)):
    result[i][1],result[i][3]=result[i][3],result[i][1]
    result[i][1],result[i][2]=result[i][2],result[i][1]
    
    
d = {'block':[],'vertices':[]}
data = pd.DataFrame(data=d)

for i in range(len(mystr)):
    data = data.append({'block': mystr[i],'vertices': result[i]},ignore_index=True)
    

prices_potential_location = []

# Rule no.1: Simplest
for i in range(len(mystr)):
    
    if mystr[i]=='合計':
    #Take the location of the word "total amount" in the receipt
        print(i)
        prices_potential_location.append(result[i])
            
            



