'''
Taking 20 images from the train and 5 images from the Test for each class
Here, we are doing mixup of AMAZON and DSLR
'''
import cv2
import pdb
import os 
import glob



all_images = glob.glob("./Office-31/dslr/*/*")
# pdb.set_trace()

"""
Copying 5 images of each class of DSLR to the mixup data creation
"""
path5_dict = {}
path5_dict["count"] = 0
for img_path in all_images:
	class_name = img_path.split('/')[-2]
	img_name = img_path.split('/')[-1]
	if class_name in path5_dict.keys():
		if len(path5_dict[class_name])<5:
			path5_dict[class_name].append(img_path)
			path5_dict["count"] += 1
	else:
		path5_dict[class_name] = [img_path]
		path5_dict["count"] += 1
path5_dict["count"] = str(path5_dict["count"])
pdb.set_trace()
for keys in path5_dict.keys():
	print(f"{keys}: {len(path5_dict[keys])}")
pdb.set_trace()