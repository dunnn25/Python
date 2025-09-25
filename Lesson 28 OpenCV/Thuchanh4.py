import cv2 

im = cv2.imread('car.png')

if im is None:
    print("Lỗi rồi bro")    
else:
    # NOTE Thay đổi kích thước giữ tỉ lệ ảnh
    print(im.shape)  # (height, width, channels)
    H0 = im.shape[0]
    W0 = im.shape[1]
    print("Chiều cao ban đầu = ", H0) 
    print("Chiều rộng ban đầu = ", W0)
    
    # chỉ định chiều rộng mới
    # W1 = 375
    # H1 = int((H0 * W1) / W0)
    H1 = 700
    W1 = int((W0*H1)/H0)
    new_size = (W1, H1)
    resize_img = cv2.resize(im, new_size, interpolation=cv2.INTER_LINEAR)
    
    cv2.imshow('Image Resize', resize_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()