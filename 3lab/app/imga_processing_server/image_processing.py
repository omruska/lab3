import numpy as np
import cv2

def invert_colors(img):
    return 255 - img

def log_correction(img):
    c = 255 / np.log(1 + np.max(img))
    return np.array(c * np.log(1 + img), dtype=np.uint8)

def gamma_correction(img, gamma_val=1.0):
    norm_img = img / 255.0
    gamma_corrected = np.power(norm_img, gamma_val)
    return np.uint8(gamma_corrected * 255)

def apply_erlang_noise(img, k=2, lam=0.5):
    shape = img.shape
    erlang_noise = np.sum(np.random.exponential(1.0 / lam, (k,) + shape), axis=0)
    noisy_img = img + erlang_noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)

def compute_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))
