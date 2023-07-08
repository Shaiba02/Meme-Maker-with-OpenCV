import cv2 as cv
import numpy as np

#meme_string='Aur cdc lag gyi?'

#brightness im + offset
#contrast   im*contrast
#im *contrast + brightness
img = cv.imread('doraemon.jpg')
img = np.float32(img/255)

meme_string = input("Enter: ")
font = cv.FONT_HERSHEY_SIMPLEX

window = 'MY MEME'

contrast = 10
max_contrast = 100

brightness = 0
max_brightness = 100

rescale_value = 100
max_rescale = 200

def change_text_size(a):
    return a/50

# Function to resize the image based on trackbar value
def resize_image(scale_percent):

    # Calculate the new dimensions
    width = int(img1.shape[1] * scale_percent / 100)
    height = int(img1.shape[0] * scale_percent / 100)

    # Resize the image
    resized_img = cv.resize(img, (width, height), interpolation=cv.INTER_LINEAR)
    set_meme(meme_string, resized_img,scale_percent)
    return resized_img

def set_meme(s,image,scale = 50):
    cv.putText(image, s, org=(30, 90), fontFace=font, fontScale=change_text_size(scale), color=(0, 0, 255), thickness=2)

def trackbar_pos(val):
    global scale_percent
    scale_percent = val
    rescale_show(scale_percent)

def set_contrast(val):
    global contrast
    contrast = val/10
    perform_operation()

def set_brightness(val):
    global brightness
    brightness = val/100
    perform_operation()

def perform_operation():
    global img1
    img1 = img * contrast + brightness
    set_meme(meme_string, img1)
    cv.imshow(window, img1)

def rescale_show(scale):
    rescaled_image = resize_image(scale)
    cv.imshow(window,rescaled_image)

cv.imshow(window, img)

# Creating trackbars
cv.createTrackbar("Contrast", window, contrast, max_contrast, set_contrast)
cv.createTrackbar("Brightness", window, brightness, max_brightness, set_brightness)
cv.createTrackbar('Scale', window , rescale_value , max_rescale, trackbar_pos)

# Keep the window open for infinite milliseconds until something is pressed
cv.waitKey(0)
cv.destroyAllWindows()
