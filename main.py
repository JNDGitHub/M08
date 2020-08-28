#!/usr/bin/env python

from imageprocessor import ImageProcessor
from videoprocessor import VideoProcessor
from filesearcher import FileSearcher
from log import Log

import sys, os
import subprocess
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

try:
    files_path = sys.argv[1]
except:
    print('Processo precisa do argumento files_path com a localizacao dos arquivos')
    exit(1)

log_obj = Log(files_path)
file_searcher = FileSearcher(files_path)
file_searcher.get_from_directory(log_obj, 0, verbose_fs=True) #signal_msg, task_id

img_proc = ImageProcessor(file_searcher.files["images"])
# use_gpu, total_processes, child_conn
img_proc.process(True, 1, log_obj)    

# vid_proc = VideoProcessor(files_searcher.files["videos"])
# # use_gpu, total_processes, child_conn
# vid_proc.process(True, 1, log_obj)    