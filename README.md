This repository is used for visualizing the LIDAR scans with their represantative times, and labelling the pointcloud points with using MATLAB's Lidar Labeler Tool. You may want to go with first only visualizing and not labelling (semantic-kitti-api) and then proceed with labeling (MATLAB).  

Note that MATLAB itself helps you to visualize scans too!   
Make sure that you understood [https://semantic-kitti.org/dataset.html](https://semantic-kitti.org/dataset.html#overview) fully!, especially the folder structures, you need to extract different installed folders inside of your custom kitti folder. Also another suggestion might be doing all of this inside of a virtual python environment to avoid overall conflictions! 

# KITTI Scan Visualization & Labeling Guide

## 📊 Visualization Steps

To generate your own visualizations:

1. **Install** one of the raw synced + rectified video sequences.  <--- I have installed the 2011_09_26_drive_0036 (3.1 GB) one, the 05th video of the provided raw data inside the Residential category.  
2. **Create** a custom KITTI folder:
   - Inside it, create a `sequences` directory.
   - Follow the **same folder structure** as required by the SemanticKITTI API.  <--- This process suggests installing the calibration and also the labels from https://semantic-kitti.org/dataset.html#download.
3. **Run** the `visualize.py` script.

> ⚠️ This process only enables to visualize scans based on timestamps — it does **not** include labeling process.

---


## 📁 Directory Structure for using semantic-kitti-api

The following folder structure is used for this project:

/custom_kitti/  
└── sequences/  
├── 05/ <--- Since I am working on the installed 05 th sequence from the Kitti Vision Benchmark  
│ ├── labels/  
│ │ ├── 000000.label   
│ │ └── 000001.label  
│ └── velodyne/  
│ │ ├── 0000000000.bin   
│ │ └── 0000000001.bin  

---


## 🏷️ Labeling Scans Using MATLAB Lidar Labeler

To evaluate the scans with labeling, this project currently uses **MATLAB’s Lidar Labeler Toolbox**.

Follow these steps:

1. **Install** MATLAB.
2. **Install** the **Lidar Labeler Toolbox** via MATLAB Add-Ons.
3. **Convert** the Velodyne `.bin` files to `.pcd` format using the provided script:
   ```bash
   python convert_kitti_to_pcd_xyzi.py

   
## 📁 Directory Structure for using MATLAB

The following folder structure is used for this project:

custom_kitti/
└── sequences/
    └── 05/  <--- Since I am working on the installed 05 th sequence from the Kitti Vision Benchmark  
        ├── velodyne/           # Input .bin files
        └── velodyne_pcd/       <--- This will be created if the convert_kitti_to_pcd_xyzi script is called, and only if there is none of this folder exists to avoid multiple creating.
