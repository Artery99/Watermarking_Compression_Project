# Watermarking Compression Project
This project implements a digital watermarking system with image compression. The system embeds a watermark into an image using Discrete Wavelet Transform (DWT) and then compresses the watermarked image using Huffman coding. It also supports decoding and watermark extraction.

# Features
Watermark Embedding: Uses DWT to embed a watermark in the frequency domain.
Watermark Extraction: Extracts the embedded watermark from a watermarked image.
Compression: Utilizes Huffman coding for lossless compression.
Decompression & Decoding: Recovers the original image and extracts the watermark.

# File Overview
watermarking3.py – Handles watermark embedding and extraction.
encoder.py – Compresses the watermarked image.
decoder.py – Decompresses the image.
huffman.py – Implements Huffman coding for compression.
Watermark_compression.py – Calls encoding and decoding scripts.
check_presence_watermark.py – Checks if a watermark is present.
utils.py – Utility functions.

# Dependencies
Python 3.x
OpenCV (cv2)
NumPy
PyWavelets (pywt)
Pillow (PIL)
