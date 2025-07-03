import numpy as np
import os

def write_pcd_text_with_intensity(xyz_intensity_data, pcd_output_path):
    """
    Writes a NumPy array with XYZI data to a text-based .pcd file.

    Args:
        xyz_intensity_data (np.ndarray): NumPy array of shape (N, 4) where columns are X, Y, Z, Intensity.
        pcd_output_path (str): Path to save the output .pcd file.
    """
    num_points = xyz_intensity_data.shape[0]

    # PCD header for XYZI data
    header = f"""# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z intensity
SIZE 4 4 4 4
TYPE F F F F
COUNT 1 1 1 1
WIDTH {num_points}
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS {num_points}
DATA ascii
"""
    with open(pcd_output_path, 'w') as f:
        f.write(header)
        # Save the data with specified float precision
        np.savetxt(f, xyz_intensity_data, fmt='%.6f %.6f %.6f %.6f') 
    print(f"Saved '{os.path.basename(pcd_output_path)}' with XYZI data.")

def batch_convert_kitti_velodyne_with_intensity(input_bin_dir, output_pcd_dir):
    """
    Batch converts all .bin files in a directory to .pcd files (text format with XYZI).

    Args:
        input_bin_dir (str): Path to the directory containing input .bin files.
        output_pcd_dir (str): Path to the directory where output .pcd files will be saved.
    """
    if not os.path.exists(output_pcd_dir):
        os.makedirs(output_pcd_dir)
        print(f"Created output directory: {output_pcd_dir}")

    bin_files = sorted([f for f in os.listdir(input_bin_dir) if f.endswith('.bin')])

    print(f"Found {len(bin_files)} .bin files in '{input_bin_dir}'")

    for bin_file_name in bin_files:
        bin_file_path = os.path.join(input_bin_dir, bin_file_name)
        pcd_file_name = bin_file_name.replace('.bin', '.pcd')
        pcd_output_path = os.path.join(output_pcd_dir, pcd_file_name)
        
        try:
            # Load the binary data (x, y, z, intensity as float32)
            lidar_points = np.fromfile(bin_file_path, dtype=np.float32).reshape(-1, 4)
            write_pcd_text_with_intensity(lidar_points, pcd_output_path)
        except Exception as e:
            print(f"Error converting {bin_file_path}: {e}")

    print("Batch conversion complete.")

if __name__ == "__main__":
    # Define your input and output directories
    # This should be your 'velodyne_points/data/' folder
    input_bin_directory = '/home/efepc/custom_kitti/sequences/05/velodyne' 
    # This will be your new folder for PCDs, which you'll point MATLAB to
    output_pcd_directory = '/home/efepc/custom_kitti/sequences/05/velodyne_pcd' 


    # Run the batch conversion
    batch_convert_kitti_velodyne_with_intensity(input_bin_directory, output_pcd_directory)