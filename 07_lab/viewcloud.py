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

def displayPcl(pcl):
    # Create axes mesh
    Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(1)
    # show meshes in view
    o3d.visualization.draw_geometries([pcl , Axes])

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])


# Create array of random points between [-1,1]
pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(np.random.rand(2500,3) * 2 - 1)
#pcl.paint_uniform_color([0.0, 0.0, 0.0])

# Create axes mesh
Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(1)

# shome meshes in view
o3d.visualization.draw_geometries([pcl , Axes])

# filter cloud
p = np.load('cloud.npz')['cloud'].reshape(-1,3)
colors = cv2.imread('pcl_image.jpg').reshape(-1,3)

fp = []
cp = []
for i in range(p.shape[0]):
    if np.all(~np.isinf(p[i])):
        fp.append(p[i])
        cp.append(np.divide(colors[i], 255))

pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(fp)
pcl.colors = o3d.utility.Vector3dVector(cp)

displayPcl(pcl)

# pcl read
clouds = ['./Depth_Images/filt_office1.pcd', './Depth_Images/filt_office2.pcd']
for file in clouds:
    pcl = o3d.io.read_point_cloud(file)
    displayPcl(pcl)

# ICP
source = o3d.io.read_point_cloud(clouds[0])
target = o3d.io.read_point_cloud(clouds[1])

threshold = 0.02
trans_init = np.asarray([[0.862, 0.011, -0.507, 0.5],
                         [-0.139, 0.967, -0.215, 0.7],
                         [0.487, 0.255, 0.835, -1.4], 
                         [0.0, 0.0, 0.0, 1.0]])

print("Apply point-to-point ICP")
reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold,
    estimation_method=o3d.pipelines.registration.TransformationEstimationPointToPoint())
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)




