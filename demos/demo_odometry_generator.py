"""Example of pykitti.odometry usage."""
import pykitti

__author__ = "Christoph Rist"
__email__ = "christoph.rist@student.kit.edu"

# Change this to the directory where you store KITTI data
basedir = '/data/rist/kitti/'

# Specify the dataset to load
sequence = '01'

# Optionally, specify the frame range to load
frame_range = range(0, 20, 5)

# Load the data
dataset = pykitti.odometry(basedir, sequence, frame_range)

# Load some data
#.load_calib()        # Calibration data are accessible as named tuples
#dataset.load_timestamps()   # Timestamps are parsed into timedelta objects
dataset.load_poses()        # Ground truth poses are loaded as 4x4 arrays
#dataset.load_gray()         # Left/right images are accessible as named tuples
#dataset.load_rgb()          # Left/right images are accessible as named tuples
#dataset.load_velo()         # Each scan is a Nx4 array of [x,y,z,reflectance]


