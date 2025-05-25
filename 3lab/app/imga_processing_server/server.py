from flask import Flask, request, jsonify
import cv2
import numpy as np
import os
from image_processing import apply_erlang_noise, invert_colors, log_correction, gamma_correction, compute_psnr

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    img_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(img_path)

    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return jsonify({'error': 'Invalid image'}), 400

    # Apply transformations
    inverted = invert_colors(img)
    log_transformed = log_correction(img)
    gamma_corrected = gamma_correction(img, gamma_val=0.8)
    noisy = apply_erlang_noise(img)

    # Compute PSNR values
    psnr_inverted = compute_psnr(img, inverted)
    psnr_log = compute_psnr(img, log_transformed)
    psnr_gamma = compute_psnr(img, gamma_corrected)

    # Save processed images
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, 'inverted.jpg'), inverted)
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, 'log_transformed.jpg'), log_transformed)
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, 'gamma_corrected.jpg'), gamma_corrected)
    cv2.imwrite(os.path.join(UPLOAD_FOLDER, 'noisy.jpg'), noisy)

    return jsonify({
        'psnr': {
            'inverted': psnr_inverted,
            'log_transformed': psnr_log,
            'gamma_corrected': psnr_gamma
        },
        'message': 'Processing complete. Images saved.'
    })

if __name__ == '__main__':
    app.run(debug=True)
