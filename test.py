import cv2 as cv
import numpy as np

haystack = cv.imread('albion_screen_includes_seaweed.PNG', cv.IMREAD_UNCHANGED)# must be the same type, png / jpeg
needle = cv.imread('albion_littleflower.PNG', cv.IMREAD_UNCHANGED)


result = cv.matchTemplate(haystack, needle, cv.TM_CCOEFF_NORMED)

#cv.imshow('Result', result)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)   # gives you the maximum value, the whitest pixel which is the best match of the two images and the miniumum which is the blackest least match pixel
# also how white the maximum is , and black 0 is the darkest black, will also return locations, 4 returns

print(' best match top left position:' + f'{max_loc}')
print(' best match confidence:'+ f'{max_val}')

needle_width = needle.shape[0]
needle_height = needle.shape[1]

top_left = max_loc
bottom_right = (top_left[0] + needle_width, top_left[1] + needle_height)

threshhold = .5

if max_val > threshhold:
    print('matches 50% atleast')
    cv.rectangle(haystack, top_left, bottom_right, #coordiantes for the top left and bottom right of the rectangle we are trying to draw
                 color=(0, 255, 9), thickness=2, lineType=cv.LINE_4)


else: print('dosent match ')

#cv.imwrite(filename='', contents)  #haystack image... this save the image as a new file
cv.imshow('result', haystack)
cv.waitKey()


