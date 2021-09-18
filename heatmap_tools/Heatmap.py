import numpy as np
import cv2 as cv

# image(H*W*3): opencv image.
# response(H*W): output from CNN, usually more than 1 dim,
#                you need to sum them to 1 dim or select specific channels .
# aphla(0-1): ratio of img and heatcolor
# Use as get_heatmap(image, response)

def get_heatmap(image, response, alpha=0.7):
    # Transform response to colormap
    img = np.zeros(image.shape, dtype=np.uint8)
    heat_color =cv.applyColorMap(__resize_normalize(image, response), cv.COLORMAP_JET)
    cv.addWeighted(image, alpha, heat_color, 1 - alpha, 0, img)
    return img
def __resize_normalize(image, response):
    img_height = image.shape[1]
    img_width = image.shape[0]
    resized_res = cv.resize(response, (img_height, img_width), interpolation=cv.INTER_CUBIC)
    # normalize heat map
    max_value = np.max(resized_res)
    min_value = np.min(resized_res)
    normalized_res = (255 * (resized_res - min_value) / (max_value - min_value))
    arr = np.array(normalized_res, dtype=np.uint8)
    return arr
