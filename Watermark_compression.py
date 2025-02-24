# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:03:56 2023

@author: hp
"""

import argparse
import os
import math
import numpy as np
from utils import *
from scipy import fftpack
from PIL import Image
from huffman import HuffmanTree
import cv2
import numpy as np
import pywt
import hashlib



import encoder
import decoder


input_file = r'watermarked_image.jpg'
output_file = r'compressed_image.bin'

output_file2=r'output_decoded.jpg'

# encoder.main()
os.system("python .\encoder.py .\watermarked_image.jpg .\output_enc.bin")

# decoder.main()
os.system("python .\decoder.py .\output_enc.bin ")

