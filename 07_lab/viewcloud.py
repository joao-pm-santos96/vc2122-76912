# ***********************************************************************************
# Name:           viewcloud.py
# Revision:
# Date:           30-10-2019
# Author:         Paulo Dias
# Comments:       Viewcloud
#
# images         left1.jpg->left19.jpg
# Revision:
# Libraries:    Python 3.7.5 + openCV 4.1.0
# ***********************************************************************************
import numpy as np
import open3d as o3d
import cv2
import copy

def displayPcl(pcl, size=1):
    # Create axes mesh
    Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size)
    # show meshes in view
    o3d.visualization.draw_geometries([pcl , Axes])

def draw_registration_result(source, target, transformation):
    # Create axes mesh
    Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(1)

    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0, 0]) 
    target_temp.paint_uniform_color([0, 1, 0]) 

    transformed = copy.deepcopy(source)
    transformed.transform(transformation)
    transformed.paint_uniform_color([0, 0, 1]) 

    o3d.visualization.draw_geometries([source_temp, target_temp, transformed, Axes])


# filter cloud
p = np.load('cloud.npz')['cloud'].reshape(-1,3)
colors = cv2.imread('pcl_image.jpg').reshape(-1,3)

fp = []
cp = []
for i in range(p.shape[0]):
    if np.all(~np.isinf(p[i])):
        if np.abs(p[i][2]) > 25 and np.abs(p[i][2]) < 75:
            fp.append(p[i])
            cp.append(np.divide(colors[i], 255))

pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(fp)
pcl.colors = o3d.utility.Vector3dVector(cp)

displayPcl(pcl, size=10)

# pcl read
clouds = ['./Depth_Images/filt_office1.pcd', './Depth_Images/filt_office2.pcd']
for file in clouds:
    pcl = o3d.io.read_point_cloud(file)
    displayPcl(pcl)

# ICP
source = o3d.io.read_point_cloud(clouds[0])
target = o3d.io.read_point_cloud(clouds[1])

threshold = 0.1

print("Apply point-to-point ICP")
reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold,
    estimation_method=o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)




