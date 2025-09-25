import cv2

img = cv2.imread('car.png') 

if img is None:
    print("Lỗi rồi bro")
else:
    # NOTE: Resize không giữ tỉ lệ ảnh
    new_width = 375
    new_height = 812
    img_resize = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR_EXACT)
    cv2.imshow('Image Resize', img_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()