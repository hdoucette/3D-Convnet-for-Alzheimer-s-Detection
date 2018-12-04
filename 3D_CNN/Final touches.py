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
denom=len(train_list)+len(test_list)

label_path=os.path.join(PD_Path,'train_data.csv')
labels_df=pd.read_csv(label_path,names=['path','patient_ID','diagnosis'])

#labeling and object formation
num=0
netdata=[]
for list in [train_list,test_list]:
    for file in list:
        path=file[0]
        label=file[1]
        if int(float(label)) == 0:
            labelar = np.array([1, 0, 0])
        elif int(float(label)) >= 2:
            labelar = np.array([0, 0, 1])
        else:
            labelar = np.array([0, 0, 1])
        #netdata=[] #will be used for numpy object
        try:
            img = nibabel.load(path)  # loading the image
            img = img.get_data()
            img = skimage.transform.resize(img.astype(int), (176, 256, 256), mode='constant')
            num=num+1
            netdata.append([img, labelar,path])
#             np.save(path, netdata)
            print(num, 'of',denom," is transformed")
        except:
            print(path,' could not be appended and saved as numpy array')
#
# #normalization
num=0
totalnum=[] #total number of pixels in the image
mean=[]  #mean of the pixels in the image
nummax=[]  #maximum value of pixels in the image
num=0

for item in netdata:
    img = item[0]
    average=np.mean(img)
    max=np.max(img)
    size=img.shape[0]*img.shape[1]*img.shape[2]
    mean.append(average)
    totalnum.append(size)
    nummax.append(max.astype(float))
    num=num+1
    print(num," of",denom," appended to mean and max")

nummean=np.vdot(mean,totalnum)/np.sum(totalnum)
nummax=np.max(nummax)
print('NUMMAX:',nummax,' NUMMEAN:',nummean)

num=0
for item in netdata:
    img=item[0]
    try:
        img=(img-nummean)/nummax #normalisation(x-mean/max value)
        item[0]=img
        num+=1
        print(num,' of',denom, ' is normalized')
        np.savez_compressed(item[2],data=item)
    except:
        continue

# Test Image Output
# path=item[2]+'.npz'
# print(path)
# img_data=np.load(path)
# img_data=img_data['data']
# print(img_data.shape)
# multi_slice_viewer(img_data[0])
# plt.show()



