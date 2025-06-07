import cv2
import pytesseract
from PIL import Image
import numpy as np

# Optional: Specify path to tesseract if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Read image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding (binary inverse)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

    # Optional: Remove noise using dilation + erosion
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    return processed

def extract_text(image_path):
    processed_img = preprocess_image(image_path)

    # Convert OpenCV image to PIL for pytesseract
    pil_img = Image.fromarray(processed_img)

    # OCR using pytesseract
    text = pytesseract.image_to_string(pil_img, config='--psm 8')  # PSM 8: treat image as a single word
    return text.strip()

# Example usage
if __name__ == "__main__":
    captcha_path = 'captcha.png'  # Replace with your CAPTCHA file path
    result = extract_text(captcha_path)
    print("CAPTCHA Text:", result)
