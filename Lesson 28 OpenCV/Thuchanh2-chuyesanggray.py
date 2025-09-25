import cv2

im = cv2.imread('car.png')
# print(im.shape)  # (height, width, channels)
# print(type(im))  # numpy.ndarray
if im is None:
    print("Lỗi rồi bro")
else:
    img_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    print(img_gray.shape)  # (height, width)
    print(type(img_gray))  # numpy.ndarray
    cv2.imshow('Image Gray', img_gray)
    cv2.waitKey(0)
    # cv2.imshow('Image', im)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    