import cv2 

# Load image always change to style BGR bule - green - red

img = cv2.imread('car.png')

if img is None:
    print("Lỗi rồi bro")
else:
    # Hiện thị ảnh trên màn hình
    cv2.imshow('Image', img)
    
    # Muốn giữ cửa sổ hiện thị cần có ảnh này
    cv2.waitKey(5000)    # Chuyền vào số nguyên dương (ms) hoặc 0 (giữ mãi) cho đến khi có phím bấm
    cv2.destroyAllWindows() 
    