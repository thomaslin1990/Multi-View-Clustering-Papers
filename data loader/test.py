from MVDataBaseClass import DataShell
from load_data_fns import load_scene15, load_landuse21, load_caltech101_20


# example 1
scene_15 = DataShell("./data/Scene-15.mat", load_scene15, missing=0.1)
print(scene_15.__len__())

# example 2
land_use_21 = DataShell("./data/LandUse-21.mat", load_landuse21, missing=0.5)
print(land_use_21.__len__())

# example 3
caltech_101_20 = DataShell("./data/Caltech101-20.mat", load_caltech101_20, missing=0.1)
print(caltech_101_20.__len__())
