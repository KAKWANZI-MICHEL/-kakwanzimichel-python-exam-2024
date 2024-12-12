class Book:  
    def __init__(self, title, author, pages):  
        self.title = title  
        self.author = author  
        self.pages = pages  

    def display_info(self):  
        return f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}'  

book_instance = Book('Justice', 'George Orwell', 328)  
print(book_instance.display_info())  
