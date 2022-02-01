## Data Introduction

### AwA

- **Key Information:** 30475 samples | 50 animals classes | 6 views (extracted features) | <a href="https://cvml.ist.ac.at/AwA/">src</a>
- **Features:** 2688-D color histogram, 2000-D local self-similarity, 252-D PHOG, 2000-D SIFT, 2000-D color SIFT and 2000-D SURF
- **Overview:** This dataset provides a platform to benchmark transfer-learning algorithms, in particular attribute base classification. It consists of 30475 images of 50 animals classes with six pre-extracted feature representations for each image. The animals classes are aligned with Osherson's classical class/attribute matrix [2, 3], thereby providing 85 numeric attribute values for each class. Using the shared attributes, it is possible to transfer information between different classes.

### YouTubeVideo

- **Key Information:** 101499 samples | 31 classes | 5 views (extracted features) | <a href="http://archive.ics.uci.edu/ml/datasets/YouTube+Multiview+Video+Games+Dataset">src</a>
- **Features:** 64-D audio volume, 512-D vision cuboids histogram, 64-D vision HIST, 647-D vision HOG, 838-D vision MISC 
- **Overview:** This dataset contains about 120k instances, each described by 13 feature types, with class information, specially useful for exploring multi-view topics (co-training, ensembles, clustering,..).

### Caltech101

- **Key Information:** 9144 samples | 101 classes | 5 views (extracted features) | <a href="http://www.vision.caltech.edu/Image_Datasets/Caltech101/">src</a>
- **Features:** 48-D Gabor, 40-D Wavelet Moments, 254-D Cenhist, 512-D GIST and 928-D LBP
- **Overview:** Pictures of objects belonging to 101 categories. About 40 to 800 images per category. Most categories have about 50 images. Collected in September 2003 by Fei-Fei Li, Marco Andreetto, and Marc 'Aurelio Ranzato. The size of each image is roughly 300 x 200 pixels.

### Handwritten

- **Key Information:** 2000 samples | 10 classes | 6 views (extracted features) | <a href="https://archive.ics.uci.edu/ml/datasets/Multiple+Features/">src</a>
- **Features:** 76-D fourier coefficient, 216-D profile correlation, 64-D Karhunen-Love coefficient, 240-D pixel average, 47-D Zernike moment and 6-D morphological features
- **Overview:** This dataset consists of features of handwritten numerals ('0--9') extracted from a collection  of Dutch utility maps. 200 patterns per class (for a total of 2,000 patterns) have been digitized in binary images.

### SUNRGBD3

- **Key Information:** 10335 samples | 45 classes | 2 views (extracted features) | <a href="http://rgbd.cs.princeton.edu/">src</a>
- **Features:** deep neural network on the original images to extract features of two views.
- **Overview:** ---

### NUS-WIDE

- **Key Information:** 23953 samples | 31 classes | 5 views (extracted features) | <a href="https://lms.comp.nus.edu.sg/wp-content/uploads/2019/research/nuswide/NUS-WIDE.html">src</a>
- **Features:** 4-D color histogram, 144-D color correlogram, 73-D edge direction histogram, 128-D wavelet texture, 225-D block-wise color moments and 500-D bag of words based on SIFT descriptions.
- **Overview:** This is a web image dataset created by Lab for Media Search in National University of Singapore.

## Feature Reference

- **color histogram:** 
- **color correlogram:**
- **local self-similarity:** 
- **PHOG:** 
- **SIFT:** 
- **SURF:** 
- **audio volume:** 
- **vision cuboids histogram:** 
- **vision HIST:** 
- **vision HOG:** 
- **vision MISC:** 
- **Gabor:** 
- **Wavelet Moments:** 
- **Cenhist:** 
- **GIST:** 
- **LBP:** 
- **fourier coefficient:** 
- **profile correlation:** 
- **Karhunen-Love coefficient:** 
- **pixel average:** 
- **Zernike moment:** 
- **morphological:** 
- **edge direction histogram:** 
- **wavelet texture:** 
- **block-wise color moments:** 
- **bag of words based on SIFT:** 
- 