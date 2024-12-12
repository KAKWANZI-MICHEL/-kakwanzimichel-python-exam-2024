#5 i).define a python class named 'book' with attributes: title, author, and pages.
#provide a method in the class to dispaly information about thr book, create an instance 
#of thhe class and display the information
#5 ii) create a derived class 'Ebook' that inherits from the book class. additional attribute "formart" to the EBook class.
#display thhe information for an insatance of the Ebook class
#5iii) create a function  on the "book" class that returns only the book title and its author 
#5iv) define the following terms
# a) class b)object
Book = 'JUSTICE'
class EBook(Book):  
    def __init__(self, title, author, pages, file_size):  
        super().__init__(title, author, pages)  
        self.file_size = file_size  

    def display_info(self):  
        return super().display_info() + f', File Size: {self.file_size}MB'  
 
ebook_instance = EBook('Brave New World', 'Aldous Huxley', 288, 1.2)  
print(ebook_instance.display_info()) 