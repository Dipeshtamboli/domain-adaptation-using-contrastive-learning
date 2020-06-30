'''
Taking 10 images from the train and 4 images from the Test for each class
Here, we are doing mixup of AMAZON and DSLR
'''
import shutil
import cv2
import pdb
import os 
import glob

def copy_img(src,dest):
    if not os.path.exists(os.path.join(*(dest.split('/')[:-1]))):
        os.makedirs(os.path.join(*(dest.split('/')[:-1])))
    dest = shutil.copy(src, dest) 


domains = {'source':'amazon',
           'target':'dslr'}
num_imgs = {'source':10,
           'target':4}
# pdb.set_trace()

"""
Copying 10 images of each class of DSLR(source) to the mixup data creation
And 4 images from AMAZON(target) to the mixup data creation
total mizup images = 31*10 x 31*4 = 38440
"""
path_dict = {}
save_folder = "small_Office-31"
for domain in domains.keys():
    all_images = glob.glob(f"./dataset/Office-31/{domains[domain]}/*/*")
    temp_path_dict = {}
    # temp_path_dict["count"] = 0
    for img_path in all_images:
        class_name = img_path.split('/')[-2]
        img_name = img_path.split('/')[-1]
        if class_name in temp_path_dict.keys():
            if len(temp_path_dict[class_name])<=num_imgs[domain]:
                temp_path_dict[class_name].append(img_path)
                # print(img_path)
                # pdb.set_trace()

                destination =img_path.split('/')
                destination[-4] = save_folder
                destination = os.path.join(*destination)
                copy_img(img_path, destination)
                # temp_path_dict["count"] += 1
        else:
            temp_path_dict[class_name] = [img_path]
    path_dict[domains[domain]] = temp_path_dict
        # temp_path_dict["count"] += 1
# path_dict["count"] = str(path_dict["count"])
# for keys in path_dict.keys():
#   print(f"{keys}: {len(path_dict[keys])}")
#   for path in path_dict[keys]:

# pdb.set_trace()