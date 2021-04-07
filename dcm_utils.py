from pydicom import dcmread
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import savemat, loadmat
import os


def dcm_to_mat(rootdir):
    """
    Takes in the root directory of the dcm files and converts all 1-1.dcm
    files to a .mat file
    TODO: update to also save the label alongside the pixel data

    inputs:
    rootdir: the root directory of the dcm files
    """
    count = 0
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            path = os.path.join(subdir, file)
            if file == "1-1.dcm":
                ds = dcmread(path)
                data = {"data" : ds.pixel_array}
                savemat(f"dcm/img{count:05d}.mat", data)
                count += 1

def image_generator(rootdir):
    """
    Calling next on this generator yields a mat file with the data in it
    TODO: also return the label for the data

    inputs:
    rootdir: The root directory of the .mat files created in dcm_to_mat
    """
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_path = os.path.join(subdir, file)
            data = loadmat(file_path)
            yield data['data']