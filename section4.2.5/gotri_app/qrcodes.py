import cv2
import os
import qrcode


def generate_payment_code(commuter_id, security_token, filepath):
    if commuter_id is None or security_token is None or filepath is None:
        raise ValueError('Cannot generate a QR payment code with null values')
    data = commuter_id + ":" + security_token
    image = qrcode.make(data)
    image.save(filepath)


def scan_payment_code(filepath):
    if not os.path.isfile(filepath):
        raise ValueError('Cannot scan a QR payment code from a nonexistent file')
    image = cv2.imread(filepath)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(image)
    return data
