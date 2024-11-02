import os, sys, cv2
from functions import predict_phishing


def main(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        sys.exit(1)

    image = cv2.imread(image_path)
    prediction, confidence = predict_phishing(image)
    
    if prediction == 1:
        print(f"This website is likely a phishing attempt! (Confidence: {confidence:.2f}%)")
    else:
        print(f"This website is legitimate. (Confidence: {confidence:.2f}%)")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "--image":
        print("Usage: python detect.py --image path/to/website_screenshot.png")
        sys.exit(1)

    image_path = sys.argv[2]
    main(image_path)
