# threshholding is finding all spots on the haystack that ar above a set threshhold
import cv2 as cv
import numpy as np


def find_clickable_positions(needle_img, haystack_img, threshold):
    haystack = cv.imread(haystack_img, cv.IMREAD_UNCHANGED)  # must be the same type, png / jpeg
    needle = cv.imread(needle_img, cv.IMREAD_UNCHANGED)

    method = cv.TM_CCOEFF_NORMED

    result = cv.matchTemplate(haystack, needle, method)

    # cv.imshow('Result', result)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    needle_width = needle.shape[0]
    needle_height = needle.shape[1]

    locations = np.where(result >= threshold)

    locations = list(zip(*locations[
                          ::-1]))  # the list is originally two lists ( multidimensional) x and y but * opens the list and zip combines all elemnts at the saem index, x and y [0]
    # and so on the list is then reversed by ::-1
    rectangles = []

    points = []

    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_width, needle_height]
        rectangles.append(rect)
        rectangles.append(
            rect)  # this is done twice because a single rectangle around an object will dissapear if it dosent have a second rectangle to combine with

    # group rectangles takes the thick, overlapped rectangles around a threshholded image which ahs been found and makes it one rectangle
    rectangles, weight = cv.groupRectangles(rectangles, 1,
                                            1)  # group threshold always has to be 1 if lower no rectangles will show if more they will overlap
    # eps is how close rectangles have to be grouped together
    # print(rectangles)
    if len(rectangles):
        line_color = (255, 150, 85)
        line_type = cv.LINE_4
        line_thickness = 2
        marker_color = (255, 0, 0)
        marker_type = cv.MARKER_TILTED_CROSS
        print('found needle')
        for (x, y, w, h) in rectangles:
            top_left = (x, y)
            bottom_right = (x + w, y + h)
            cv.rectangle(haystack, top_left, bottom_right, line_color, line_thickness, line_type)
            center_x = x + int(w / 2)
            center_y = y + int(w / 2)
            points.append((center_x, center_y))
            cv.drawMarker(haystack, (center_x, center_y), marker_color, marker_type, markerSize=20)

        cv.imshow('Result-On Haystack', haystack)
        cv.waitKey()

    else:
        print('needle not found')
    print(points)
    return points


find_clickable_positions('seven.PNG', '100_numbers.PNG', .9)
