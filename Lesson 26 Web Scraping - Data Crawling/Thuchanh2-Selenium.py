from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Đi set một số options cho trình duyệt Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy trình duyệt ở chế độ ẩn danh (không hiển thị giao diện)

# tạo chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# lấy đường dẫn trang web
url = "https://quotes.toscrape.com/"
driver.get(url) # truy cập và dynamic website
time.sleep(3) # chờ 3s để web load xong - trường hợp mạng yếu
def scape_quote():
    # trích xuất các title
    titles = driver.find_elements(By.CLASS_NAME, "text")
    for title in titles:
        print(title.text)
scape_quote()

# muốn crawl 1 page tiếp theo
for _ in range(5): # ví dụ muốn lấy thêm thông tin của N pages
    next_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/nav/ul/li/a")
    next_button.click()
    time.sleep(3) # chờ 3s để web load xong - trường hợp mạng yếu
    scape_quote()   # Sử dụng lại vì cấu trúc giống nhau

driver.quit() # đóng trình duyệt