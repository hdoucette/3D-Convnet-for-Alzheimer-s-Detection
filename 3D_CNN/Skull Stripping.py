import os
import nipype
import nipype.interfaces.fsl as fsl
#import win32con

data_dir='/home/ubuntu/OAS30001_MR_d0129/anat3'                                                                                                                              #path to raw image directory
ssdata_dir='/home/ubuntu/OAS30001_MR_d0129/anat3_test'                                                                                                                           #path to skull stripped image directory

# for file in os.listdir(data_dir):
#     try:
#         mybet = nipype.interfaces.fsl.BET(in_file=os.path.join(data_dir,file),out_file=os.path.join(ssdata_dir,file +'_2.nii'), frac=0.2)                #frac=0.2
#         mybet.run()                                                                                                                                      #executing the brain extraction
#         print(file+'is skull stripped')
#     except:
#         print(file+'is not skull stripped')
file='sub-OAS30001_ses-d0129_run-02_T1w.nii'
try:
    mybet = nipype.interfaces.fsl.BET(in_file=os.path.join(data_dir, file),
                                      out_file=os.path.join(ssdata_dir, file + '_2.nii'), frac=0.2)  # frac=0.2
    mybet.run()  # executing the brain extraction
    print(file + ' is skull stripped')
except:
    print(file + ' is not skull stripped')

mybet = nipype.interfaces.fsl.BET(in_file=os.path.join(data_dir, file),
                                      out_file=os.path.join(ssdata_dir, file + '_2.nii'), frac=0.2)  # frac=0.2
mybet.run()  # executing the brain extraction
print(file + ' is skull stripped')