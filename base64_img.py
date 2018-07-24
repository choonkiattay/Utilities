import cv2
import base64
import numpy as np


def encode(img):
    cv2_encode = cv2.imencode('.jpg', img)[1].tostring()
    base64_image = base64.b64encode(cv2_encode)
    return base64_image


def decode(base64_image):
    # decode_img = base64.b64decode(base64_image)
    decode_img = np.fromstring(base64_img.decode('base64'), np.uint8)
    return decode_img


if __name__ == '__main__':
    ori_img = cv2.imread('/home/tunnel/past/crop/BJN4988.jpg')
    base64_img = encode(ori_img)
    print(base64_img)
    decoded_img = decode(base64_img)
    rgb_img = cv2.imdecode(decoded_img, cv2.IMREAD_ANYCOLOR)
    cv2.imwrite("/home/tunnel/test.png", rgb_img)


