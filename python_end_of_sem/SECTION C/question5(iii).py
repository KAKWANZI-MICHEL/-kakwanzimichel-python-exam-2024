class Book:  
    def __init__(self, title, author):  
        self.title = title  
        self.author = author  

    def get_info(self):  
        return f'Title: {self.title}, Author: {self.author}'  
     
book_instance = Book("JUSTICE", "George Orwell")  
print(book_instance.get_info())  