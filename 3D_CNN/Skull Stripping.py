import os
import nipype
import nipype.interfaces.fsl as fsl
#import win32con
from sys import platform

if platform=='win32':
    root='C:/Users/douce/Desktop/MIT Fall 2018/6.869 Machine Vision/Final Project/'
else: root='/home/ubuntu'

file_path=os.path.join(root,'oasis-scripts/scans')
for file in os.listdir(os.path.join(file_path)):
    file_path_2=os.path.join(file_path,file)
    #print(file)
    for scan in os.listdir(file_path_2):
        scan_path=os.path.join(file_path_2,scan)
        #print(scan)
        for image in os.listdir(scan_path):
            if image.endswith('nii.gz'):
                iFile=os.path.join(scan_path,image)
                #print(iFile)
                try:
                    mybet = nipype.interfaces.fsl.BET(in_file=iFile,
                                                      out_file=os.path.join(scan_path,image + '_stripped.nii'),
                                                      frac=0.5)
                    mybet.run()  # executing the brain extraction
                    print(file + ' is skull stripped')
                except:
                    print(file + ' is not skull stripped')