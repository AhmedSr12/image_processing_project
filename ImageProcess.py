import cv2
import numpy as np


def crop(img):
    image = cv2.resize(img, (540, 920))
    orig = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 30, 50)

    contours, hierarchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    targetlist = []
    for c in contours:
        p = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * p, True)
        if len(approx) == 4:
            targetlist.append(approx)

    new_endpoints = [0, 0, 0, 0]

    for i in range(0, 2):
        target = targetlist[i]
        endpoints = []
        for j in range(len(target)):
            endpoints.append(list(target[j][0]))

        endpoints[2][1] = endpoints[2][1] + 184
        endpoints[3][1] = endpoints[3][1] + 179

        for k in range(len(endpoints)):
            if endpoints[k][0] < 210 and endpoints[k][1] < 410:
                new_endpoints[0] = endpoints[k]
            elif endpoints[k][0] < 450 and endpoints[k][1] < 450:
                new_endpoints[1] = endpoints[k]
            elif endpoints[k][0] < 210 and endpoints[k][1] > 500:
                new_endpoints[3] = endpoints[k]
            else:
                new_endpoints[2] = endpoints[k]

        if 0 not in new_endpoints:
            break

    pts = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])
    approx = np.float32(new_endpoints)

    op = cv2.getPerspectiveTransform(approx, pts)
    dst = cv2.warpPerspective(orig, op, (800, 800))

    gray_dist = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    index1 = 0
    for i in range(670):
        for j in range(670):
            if gray_dist[i][j] < 100:
                index1 = i

    cropped = dst[100:index1, 0:800]
    return cropped

