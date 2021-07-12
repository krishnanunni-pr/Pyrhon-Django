# 3. Create a Book class with instance Library_name, book_name, author, pages?

class Book:

    def bookdetails(self,bkname,author,pages,library_name):
        self.library_name=library_name
        self.bkname=bkname
        self.author=author
        self.pages=pages
        print("Book name :",bkname)
        print("Authour :",author)
        print("Number of pages :",pages)
        print("Library section :",library_name)

obj=Book()
bname=input("Enter the name of book :")
author=input("Name of authour :")
pageno=int(input("Number of pages :"))
library_name=input("Enter library name :")
obj.bookdetails(bname,author,pageno,library_name)
