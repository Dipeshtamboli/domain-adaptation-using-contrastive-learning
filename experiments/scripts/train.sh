#!/bin/bash
# ./experiments/scripts/train.sh ./experiments/config/Office-31/CAN/office31_train_amazon2dslr_cfg.yaml 0 CAN office31_a2d_normal
# ./experiments/scripts/train.sh ./experiments/config/Office-31/CAN/office31_train_amazon2dslr_cfg.yaml 0 CAN office31_a2d_mixup
export PYTHONPATH="`pwd`:${PYTHONPATH}"
if [ $# != 4 ]
then 
  echo "Please specify 1) cfg; 2) gpus; 3) method; 4) exp_name."
  exit
fi

cfg=${1}
gpus=${2}
method=${3}
exp_name=${4}

out_dir=./experiments/ckpt/${exp_name}
if [ -d ${out_dir} ]
then
  rm -rf ${out_dir}
fi
mkdir -p ${out_dir}

CUDA_VISIBLE_DEVICES=${gpus} python3 -W ignore ./tools/train.py --cfg ${cfg} \
           --method ${3} --exp_name ${4} 2>&1 | tee ${out_dir}/log.txt
