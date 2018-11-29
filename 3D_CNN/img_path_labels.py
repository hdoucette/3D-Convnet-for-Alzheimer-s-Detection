import os
import csv
from sys import platform
from Visualisation import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if platform=='win32':
   root='C:/Users/douce/Desktop/MIT Fall 2018/6.869 Machine Vision/Final Project/'
else: root='/home/ubuntu'

#Read Patient Data
PD_Path=os.path.join(root,'oasis-scripts/Patient_Data.csv')
df = pd.read_csv(PD_Path, index_col='Subject')

#list = Image Path, Patient ID, and Diagnosis
image_paths=[]
file_path=os.path.join(root,'oasis-scripts/scans')
for file in os.listdir(os.path.join(file_path)):
    patientID=file[:8]
    file_path_2=os.path.join(file_path,file)
    diagnosis = df.loc[patientID, 'UDS D1: Clinician Diagnosis']
    for scan in os.listdir(file_path_2):
        scan_path=os.path.join(file_path_2,scan)
        for image in os.listdir(scan_path):
            if image.endswith('.nii.gz'):
                image_paths.append([os.path.join(scan_path,image),patientID,diagnosis])



csv_path=os.path.join(root,'oasis-scripts/image_paths.csv')
with open(csv_path, 'w',newline= '') as writeFile:
     writer = csv.writer(writeFile)
     writer.writerows(path for path in image_paths)

# #test images
# img=nibabel.load(image_paths[0])                         #loading the image
# img_data=img.get_data()                                                     #accessing image array
# multi_slice_viewer(img_data)
# plt.show()


