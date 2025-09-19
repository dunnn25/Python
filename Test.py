import pygame
import sys
import math

# Khởi tạo Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Quả bóng nảy trong hình lục giác quay")
clock = pygame.time.Clock()

# Định nghĩa màu sắc
WHITE = (255, 255, 255)  # Màu nền
BLACK = (0, 0, 0)       # Màu hình lục giác
RED = (255, 0, 0)       # Màu quả bóng

# Thiết lập thông số hình lục giác
center = (300, 300)      # Tâm hình lục giác
radius = 200             # Bán kính hình lục giác
angle = 0                # Góc quay ban đầu
angular_speed = 0.01     # Tốc độ quay (radian/khung hình)

# Class để quản lý quả bóng
class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x              # Vị trí x
        self.y = y              # Vị trí y
        self.radius = radius    # Bán kính quả bóng
        self.color = color      # Màu quả bóng
        self.vx = 2            # Vận tốc ban đầu theo x
        self.vy = 0            # Vận tốc ban đầu theo y
        self.ax = 0            # Gia tốc theo x
        self.ay = 0.1          # Gia tốc trọng lực theo y

    def update(self):
        # Cập nhật vận tốc với gia tốc
        self.vx += self.ax
        self.vy += self.ay
        # Áp dụng ma sát (giảm vận tốc)
        self.vx *= 0.99
        self.vy *= 0.99
        # Cập nhật vị trí
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Hàm vẽ hình lục giác
def draw_hexagon(screen, color, center, radius, angle):
    points = []
    for i in range(6):
        x = center[0] + radius * math.cos(angle + 2 * math.pi * i / 6)
        y = center[1] + radius * math.sin(angle + 2 * math.pi * i / 6)
        points.append((x, y))
    pygame.draw.polygon(screen, color, points)

# Hàm tính khoảng cách từ điểm đến đoạn thẳng
def distance_to_line(point, line_start, line_end):
    line_vec = (line_end[0] - line_start[0], line_end[1] - line_start[1])
    point_vec = (point[0] - line_start[0], point[1] - line_start[1])
    line_len = math.sqrt(line_vec[0]**2 + line_vec[1]**2)
    if line_len == 0:
        return math.sqrt(point_vec[0]**2 + point_vec[1]**2)
    t = max(0, min(1, (point_vec[0] * line_vec[0] + point_vec[1] * line_vec[1]) / line_len**2))
    projection = (line_start[0] + t * line_vec[0], line_start[1] + t * line_vec[1])
    return math.sqrt((point[0] - projection[0])**2 + (point[1] - projection[1])**2)

# Hàm tính vector pháp tuyến của đoạn thẳng
def normal_vector(line_start, line_end):
    dx = line_end[0] - line_start[0]
    dy = line_end[1] - line_start[1]
    length = math.sqrt(dx**2 + dy**2)
    if length == 0:
        return (0, 0)
    return (-dy / length, dx / length)

# Tạo đối tượng quả bóng
ball = Ball(300, 300, 10, RED)

# Vòng lặp chính
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Xóa màn hình
    screen.fill(WHITE)

    # Cập nhật góc quay của hình lục giác
    angle += angular_speed

    # Tính toán các đỉnh của hình lục giác
    points = []
    for i in range(6):
        x = center[0] + radius * math.cos(angle + 2 * math.pi * i / 6)
        y = center[1] + radius * math.sin(angle + 2 * math.pi * i / 6)
        points.append((x, y))

    # Vẽ hình lục giác
    draw_hexagon(screen, BLACK, center, radius, angle)

    # Cập nhật trạng thái quả bóng
    ball.update()

    # Kiểm tra và xử lý va chạm với các bức tường
    for i in range(6):
        line_start = points[i]
        line_end = points[(i + 1) % 6]
        dist = distance_to_line((ball.x, ball.y), line_start, line_end)
        if dist <= ball.radius:
            # Tính vector pháp tuyến
            normal = normal_vector(line_start, line_end)
            # Tính tích vô hướng
            dot_product = ball.vx * normal[0] + ball.vy * normal[1]
            # Phản xạ vận tốc
            ball.vx -= 2 * dot_product * normal[0]
            ball.vy -= 2 * dot_product * normal[1]
            # Di chuyển quả bóng ra khỏi tường để tránh kẹt
            overlap = ball.radius - dist
            ball.x += normal[0] * overlap
            ball.y += normal[1] * overlap

    # Vẽ quả bóng
    ball.draw(screen)

    # Cập nhật màn hình
    pygame.display.flip()
    clock.tick(60)  # Giới hạn 60 khung hình/giây