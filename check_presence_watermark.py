# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 12:43:27 2023

@author: CBS Computer
"""
import cv2
import numpy as np
import pywt
import hashlib
from PIL import Image




def extract_watermark(img_path, alpha=0.5):
    # Read the watermarked image
    img_wm = cv2.imread(img_path)

    # Perform DWT on the watermarked image
    LL_wm, (LH_wm, HL_wm, HH_wm) = pywt.dwt2(img_wm, 'haar')

    # Extract the watermark from the LH subband
    bit_array = ((LH_wm - LH_wm.mean()) / alpha).flatten().astype(np.uint8)

    # Convert the bit array back to a string using SHA-256 hashing
    hash_object = hashlib.sha256(bit_array)
    watermark = hash_object.hexdigest()

    return watermark

#Extract the watermark from the watermarked image and the decoded image
watermark= extract_watermark('watermarked_image.jpg')
decoded_watermark = extract_watermark('output_decoded.jpg')

# Compare the two watermarks
if np.all(watermark == decoded_watermark):
    print("Watermark is still present after decoding.")
else:
    print("Watermark is not present after decoding.")
    