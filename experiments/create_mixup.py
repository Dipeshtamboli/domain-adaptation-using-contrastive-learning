'''
loading images from the small_Office-31 dataset and creating mixup
'''
from tqdm import tqdm
import numpy as np
import glob
import os
import pdb
import cv2

def save_img(filename, img ):
    dest = filename
    if not os.path.exists(os.path.join(*(dest.split('/')[:-1]))):
        os.makedirs(os.path.join(*(dest.split('/')[:-1])))
    cv2.imwrite(filename, img) 
domains_dict = {'source':'dslr',
           'target':'amazon'}
load_folder = "small_Office-31"
save_folder = "mixup_Office-31"

MIXUP_ALPHA = 0.4

path_dict = {}
for domain in domains_dict.keys():
    path_dict[domains_dict[domain]] = glob.glob(f"./dataset/{load_folder}/{domains_dict[domain]}/*/*")

for key in path_dict.keys():
    print(f"total images {key}: {len(path_dict[key])}")
    # for path in path_dict[key]:
    #   print(path)
for source_path in tqdm(path_dict[domains_dict['source']]):
    num_all_imgs = 0
    for target_path in path_dict[domains_dict['target']]:
        num_all_imgs +=1
        # print(source_path)
        src_img = cv2.imread(source_path)   # images are in the range of 0-255
        tgt_img = cv2.imread(target_path)   # images are in the range of 0-255
        src_resized = cv2.resize(src_img, (500, 500))
        tgt_resized = cv2.resize(tgt_img, (500, 500))
        mixup_img = (src_resized*MIXUP_ALPHA + tgt_resized*(1- MIXUP_ALPHA))

        destination =source_path.split('/')
        destination[-4] = save_folder
        destination = os.path.join(*destination)
        destination = destination.split('.jpg')[0]+f'_{num_all_imgs}.jpg'
        # pdb.set_trace()
        save_img(destination, mixup_img)
        # print(f'src shape: {src_img.shape}\ntgt shape:{tgt_img.shape}')
        # print(f'src resized shape: {src_resized.shape}\ntgt resized shape:{tgt_resized.shape}')

        # cv2.imshow('src_img', src_img)
        # cv2.imshow('tgt_img', tgt_img)
        # cv2.imshow('src_re_img', src_resized)
        # cv2.imshow('tgt_re_img', tgt_resized)
        # cv2.imshow('mixup', mixup_img)
        # cv2.waitKey(0) 
        # exit()