# import numpy as np
# import cv2
#
# import time
#
# camera = cv2.VideoCapture("abc.mp4")
#
# background = None
#
# while True:
#     (grabbed, frame) = camera.read()
#     if not grabbed:
#         break
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (21, 21), 0)
#
#     if background is None:
#         background = gray
#     continue
#
# subtraction = cv2.absdiff(background, gray)
# threshold = cv2.threshold(subtraction, 25, 255, cv2.THRESH_BINARY)[1]
# threshold = cv2.dilate(threshold, None, iterations=2)
# contour_img = threshold.copy()
# im, outlines, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for c in outlines:
#     print("here")
#     if cv2.contourArea(c) < 500:
#         continue
#     (x, y, w, h) = cv2.boundingRect(c)
#     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     cv2.imshow("Camera", frame)
#     cv2.imshow("Threshold", threshold)
#     cv2.imshow("subtraction", subtraction)
#     cv2.imshow("Contour", contour_img)
#
#     key = cv2.waitKey(1) & 0xFF
#     time.sleep(0.015)
#
#     if key == ord("s"):
#         break
#
# camera.release()
# cv2.destroyAllWindows()


# import cv2
#
# first_frame = None
# video = cv2.VideoCapture("abc.mp4")
#
# a = 0
# while True:
#     a += 1
#     check, frame = video.read()
#     # if not check:
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
#     if first_frame is None:
#         first_frame = gray_frame
#         continue
#
#     delta_frame = cv2.absdiff(first_frame, gray_frame)
#     res1 = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
#     cv2.imshow("capturing", gray_frame)
#     cv2.imshow("delta frame", res1)
#     print(delta_frame)
#
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         break
#
# cv2.destroyAllWindows()
# video.release()
# print(a)


import cv2
import numpy as np

cap = cv2.VideoCapture("pitch Deck Presentation.mp4")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:

    (grabbed, frame) = cap.read()
    if not grabbed:
        break

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # print("gg", thresh)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    slide_Number = 1
    idx = 0
    for contours in contours:
        # print("contour count ", cv2.contourArea(contours)
        if cv2.contourArea(contours) > 350000:
            print("contours count are above 16000", cv2.contourArea(contours))
            print(cap.get(1))
            slide_Number = slide_Number + 1
            cv2.imwrite('slides/' + 'Slide_' + str(slide_Number) + '_' + str(cap.get(1)) + '.png', frame)

            # image crop start here

            image = cv2.imread('slides/' + "Slide_" + str(slide_Number) + '_' + str(cap.get(1)) + '.png')
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            mid = cv2.Canny(blurred, 30, 150)
            edge = cv2.Canny(image, 100, 200)
            (cnts, _) = cv2.findContours(mid.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for c in cnts:
                x, y, w, h = cv2.boundingRect(c)
                # print(x, y, w, h)
                if w > 50 and h > 50:
                    idx += 1
                    new_img = image[y:y + h, x:x + w]
                    cv2.imwrite("cropped/" + 'Slide_' + str(slide_Number) + '_' + str(idx) + '.png', new_img)

            #         Image crop stops here

            continue
    # print("contours", cv2.contourArea(contours))
    cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    resized = cv2.resize(frame2, (960, 540))
    cv2.imshow("feed", resized)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()


