import nibabel
import matplotlib.pyplot as plt                                                 #package imports
import os
import gzip

def process_key(event):
    fig = event.canvas.figure
    ax = fig.axes[0]
    if event.key == 'a':
        previous_slice(ax)
    elif event.key == 'q':
        next_slice(ax)
    fig.canvas.draw()

def multi_slice_viewer(volume):
    fig, ax = plt.subplots()
    ax.volume = volume
    ax.index =0
    ax.imshow(volume[:, :, ax.index],cmap='gray')
    fig.canvas.mpl_connect('key_press_event', process_key)

def previous_slice(ax):
    """Go to the previous slice."""
    volume = ax.volume
    ax.index = (ax.index - 1) % volume.shape[0]  # wrap around using %
    ax.images[0].set_array(volume[:, :, ax.index])

def next_slice(ax):
    """Go to the next slice."""
    volume = ax.volume
    ax.index = (ax.index + 1) % (volume.shape[0])
    ax.images[0].set_array(volume[:, :, ax.index])


# data_dir='C:/Users/douce/Desktop/MIT Fall 2018/6.869 Machine Vision/Final Project/oasis-scripts/scans/OAS30345_MR_d0087/anat2' #image directory
# img=nibabel.load(os.path.join(data_dir,'sub-OAS30345_ses-d0087_run-01_T1w_stripped.nii.gz'))
#
# img_data=img.get_data()
# multi_slice_viewer(img_data)
# plt.show()