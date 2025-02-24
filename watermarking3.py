
import cv2
import numpy as np
import pywt
import hashlib
from PIL import Image

def string_to_bits(string):
    # Convert a string to a bit array
    bit_array = []
    for char in string:
        bits = bin(ord(char))[2:].rjust(8, '0')
        bit_array.extend([int(bit) for bit in bits])
    return np.array(bit_array, dtype=np.uint8)

def embed_watermark(img_path, watermark, alpha=0.5):
    # Read the image
    img = cv2.imread(img_path)

    # Perform DWT on the image
    LL, (LH, HL, HH) = pywt.dwt2(img, 'haar')

    # Convert the watermark to a bit array using SHA-256 hashing
    hash_object = hashlib.sha256(watermark.encode('utf-8'))
    bit_array = np.frombuffer(hash_object.digest(), dtype=np.uint8)

    # Pad the bit array with zeros to match the size of the LH subband
    bit_array = np.pad(bit_array, (0, LH.size - bit_array.size), 'constant')

    # Embed the watermark in the LH subband
    LH_wm = LH + alpha * bit_array.reshape(LH.shape)

    # Combine the modified subbands to reconstruct the image
    img_wm = pywt.idwt2((LL, (LH_wm, HL, HH)), 'haar')

    return img_wm.astype(np.uint8)

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

# Example usage:
img_path = 'baboon.jpg'
watermark_text = 'Hello world!'

# Embed the watermark in the image
img_wm = embed_watermark(img_path, watermark_text)

# Save the watermarked image
cv2.imwrite('watermarked_image.jpg', img_wm)


# Extract the watermark from the watermarked image
watermark_extracted = extract_watermark('watermarked_image.jpg')
watermark_extracted = '0746623f6247f096ff00dc2012fe38e7ecdb8c7729dd7e2c9c4db2e87cf49402'
watermark_text = bytes.fromhex(watermark_extracted).decode('latin-1')
print(watermark_text)

# Print the extracted watermark
print(watermark_extracted)

