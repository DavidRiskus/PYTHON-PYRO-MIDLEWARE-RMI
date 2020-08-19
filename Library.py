from __future__ import print_function
# from Book import Book
import Pyro4

def printed_books(method): #Modified print function, if list loop through and print each item, else print as a string
    if type(method) is list:
        for book in method:
            print(book)
    else:
        print(method)

@Pyro4.expose
class Library(object):
    def __init__(self):
        self.set_of_books = []

        #BOOK DETAILS:
        self.id = 0
        self.author = ""
        self.ISBN = ""
        self.title = ""
        self.year = 0
        self.loan_status = False
        self.loan_count = 0

    def return_books(self):
        print("\nUnsorted books list:\n")
        printed_books(self.set_of_books)
        return self.set_of_books

    def add_book(self, author, title, ISBN, year):
        self.id += 1
        self.author = author
        self.ISBN = ISBN
        self.title = title
        self.year = year
        self.set_of_books.append({"ID":self.id, "AUTHOR":self.author, "ISBN":self.ISBN, "TITLE":self.title, "YEAR":self.year, "ON LOAN":self.loan_status, "LOAN COUNT":self.loan_count})
        print(f"Book Title: {self.title} with ID: {self.id} Has been added \n")
        return self.id

    def select_by_year(self, start_year, end_year):
        range =[]
        for book in self.set_of_books:
            if book["YEAR"] >= start_year and book["YEAR"] <= end_year:
                range.append(book)
        if range == []:
            return "\nNo books in that range"
        else:
            print(f"\nthe following books match the search:\n")
            printed_books(range)
            return range

    def set_on_loan(self, title):
        for book in self.set_of_books:
            if book["TITLE"] == title: #need .lower() or something error checking
                book["ON LOAN"] = True
                book["LOAN COUNT"] += 1
                print(f"\nBook: {book['TITLE']} is now loaned, total times loaned: {book['LOAN COUNT']} \n")


    def set_not_loan(self, title):
        for book in self.set_of_books:
            if book["TITLE"] == title: #need .lower() or something error checking
                book["ON LOAN"] = False
                print(f"\nBook: {book['TITLE']} is no longer on loan, total times loaned: {book['LOAN COUNT']} \n")



    def return_books_sorted(self):
        sorted_list = [x for x in self.set_of_books]
        sorted_list.sort(key = lambda x: x["YEAR"])
        sorted_list.reverse()
        print("\nSorted books list: \n")
        printed_books(sorted_list)
        return sorted_list

    def return_books_ISBN(self, intValue):
        range =[]
        for book in self.set_of_books:
            if str(intValue) in book["ISBN"].split("-"):
                 range.append(book)
        if range == []:
            return f"\nNo ISBN cotains {intValue} \n"
        else:
            return range

def main():
    library = Library()
    Pyro4.Daemon.serveSimple(
        {
            library: "example.library" #objects name
        },
        ns=True)# here we actually by switching to true, start registering object URI addresses.


if __name__ == "__main__":
    main()
