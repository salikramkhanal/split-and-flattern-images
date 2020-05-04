# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:32:52 2019

@author: INESC TEC
"""
import numpy as np
import cv2
input_path = 'D:\\A\\Test\\'
output_path = 'D:\\A\\Test\\'
ext = '.tiff'
training_data_R,training_data_G,training_data_B,training_data_GRAY = [],[],[],[]
for i in range(1,10):
    complete_path = input_path+str(i)+ext
    I = cv2.imread(complete_path,1)
    I_GRAY = cv2.imread(complete_path,0)
    #I =I[50:350,50:350]
    #I_GRAY =I_GRAY[50:350,50:350]
    I=cv2.resize(I,(96,96))
    I_GRAY=cv2.resize(I_GRAY,(96,96))
    I_R =I[:,:,0] 
    I_G =I[:,:,1] 
    I_B =I[:,:,2]
    I_R=(I_R.flatten())/255
    I_G=(I_G.flatten())/255
    I_B=(I_B.flatten())/255
    I_GRAY = (I_GRAY.flatten())/255
    training_data_R.append([I_R]) 
    training_data_G.append([I_G])   
    training_data_B.append([I_B])  
    training_data_GRAY.append([I_GRAY])
    print(i)
X_R = np.asarray(training_data_R)
X_G = np.asarray(training_data_G)
X_B = np.asarray(training_data_B)
X_GRAY = np.asarray(training_data_GRAY)
np.save(output_path+'R_All4',X_R)
np.save(output_path+'G_All4',X_G)
np.save(output_path+'B_All4',X_B)
np.save(output_path+'GRAY_All4',X_GRAY)
print('saved')
