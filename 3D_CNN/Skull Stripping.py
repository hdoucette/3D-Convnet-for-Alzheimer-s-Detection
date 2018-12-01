import os
import nipype
import nipype.interfaces.fsl as fsl
#import win32con
from sys import platform

def skull_strip_all():

    if platform=='win32':
        root='C:/Users/douce/Desktop/MIT Fall 2018/6.869 Machine Vision/Final Project/'
    else: root='/home/ubuntu'

    file_path=os.path.join(root,'oasis-scripts/scans')
    for file in os.listdir(os.path.join(file_path)):
        file_path_2=os.path.join(file_path,file)
        for scan in os.listdir(file_path_2):
            scan_path=os.path.join(file_path_2,scan)
            for image in os.listdir(scan_path):
                if image.endswith('w.nii.gz'):
                    iFile=os.path.join(scan_path,image)
                    try:
                        mybet = nipype.interfaces.fsl.BET(in_file=iFile,
                                                      out_file=os.path.join(scan_path,image + '_stripped.nii.gz'),
                                                      frac=0.5)
                        mybet.run()  # executing the brain extraction
                        print(file + ' is skull stripped')
                    except:
                        print(file + ' is not skull stripped')
    return


def skull_strip_single(img_path,dir):
    imgFile = os.listdir(img_path)
    try:
        mybet = nipype.interfaces.fsl.BET(in_file=imgFile,
                                          out_file=os.path.join(dir, imgFile + '_stripped.nii'),
                                          frac=0.5)
        mybet.run()  # executing the brain extraction
        print(imgFile + ' is skull stripped')
    except:
        print(imgFile + ' is not skull stripped')

    return

skull_strip_all()

