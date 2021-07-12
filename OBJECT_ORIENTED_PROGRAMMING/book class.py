class Book:
    library_name="ABC Library"
    def bookdetails(self,bkname,author,pages):
        self.bkname=bkname
        self.author=author
        self.pages=pages
        print("Book name :",bkname)
        print("Authour :",author)
        print("Number of pages :",pages)
        print("Library section :",Book.library_name)

obj=Book()
bname=input("Enter the name of book :")
author=input("Name of authour :")
pageno=int(input("Number of pages :"))
obj.bookdetails(bname,author,pageno)

# 2 Types of variables
# 1.----Static variabale....Related to class..Access using classs name
# 2.---Instasnce varable---Realated to methods ...Access using self