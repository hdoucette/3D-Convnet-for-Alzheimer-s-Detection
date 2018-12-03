import os
import pandas as pd
import numpy as np
import skimage
from skimage import transform
import nibabel
from sys import platform
import csv
from Visualisation import *
import matplotlib.pyplot as plt
# from skimage.viewer import ImageViewer

def getdata(path,file):
    file_path=os.path.join(path,file)
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data=list(reader)
        return data

if platform=='win32':
   root='C:/Users/douce/Desktop/MIT Fall 2018/6.869 Machine Vision/Final Project/'
else: root='/home/ubuntu'

#Read Patient Data
PD_Path=os.path.join(root,'oasis-scripts')
train_list=getdata(PD_Path,'train_data.csv')
test_list=getdata(PD_Path,'test_data.csv')


label_path=os.path.join(PD_Path,'train_data.csv')
labels_df=pd.read_csv(label_path,names=['path','patient_ID','diagnosis'])

#labeling and object formation
for list in [train_list,test_list]:
    for file in list:
        path=file[0]
        label=file[2]
        netdata=[] #will be used for numpy object
        img = nibabel.load(path)  # loading the image
        #img=nibabel.load('C:/Users/douce/Desktop/MIT Fall 2018/6.869 Machine Vision/Final Project/oasis-scripts/scans\OAS30345_MR_d0087/anat2\sub-OAS30345_ses-d0087_run-01_T1w.nii.gz')
        try:
            img = nibabel.load(path)  # loading the image
            img = img.get_data()
            img = skimage.transform.resize(img.astype(int), (176, 256, 256), mode='constant')
            if int(float(label)) == 0:
                labelar = np.array([1, 0, 0])
                netdata.append([img, labelar])
                np.save(path, netdata)
                print(path," is saved as npy")
            elif int(float(label)) >=2:
                labelar = np.array([0, 1, 0])
                netdata.append([img, labelar])
                np.save(path, netdata)
                print(path, " is saved as npy")
            else:
                labelar = np.array([0, 0, 1])
                netdata.append([img, labelar])
                np.save(path, netdata)
                print(path, " is saved as npy")
        except:
            continue

#normalization
totalnum=[] #total number of pixels in the image
mean=[]  #mean of the pixels in the image
nummax=[]  #maximum value of pixels in the image
for list in [train_list,test_list]:
    for file in train_list:
        file_name=file[0]+'.npy'
        try:
            img = np.load(file_name)
            mean.append(np.mean(img[0][0]))
            totalnum.append((img[0][0].shape[0]*img[0][0].shape[1]*img[0][0].shape[2]))
            nummax.append(np.max(img[0][0]))
            print(file_name, " is added to mean and max")
        except:
            continue


nummean=np.vdot(mean,totalnum)/np.sum(totalnum)
nummax=np.max(nummax)
print(nummax,nummean)

for list in [train_list,test_list]:
    for file in train_list:
        try:
            file_name=file[0]+'.npy'
            img = np.load(file_name)
            img[0][0]=(img[0][0]-nummean)/nummax #normalisation(x-mean/max value)
        except:
            continue

# #Test Image Output
img_data=img[0][0]
# multi_slice_viewer(img_data)
# plt.show()
np.save(file_name,img)



