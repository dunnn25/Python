###Bài tập 1: Quản lý sách
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True
    def borrow(self):
        self.is_available = False
    def return_book(self):
        self.is_available = True
    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        print("Thông tin sách")
        print("Tiêu đề:", self.title)
        print("Tác giả:", self.author)
        print("Năm xuất bản:", self.publication_year)
        print("Trạng thái:", status)    

book1 = Book("War and Peace", "Leo Tolstoy", 1869)
book1.display_info()
book1.borrow()
book1.display_info()
