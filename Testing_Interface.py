import sys
import Pyro4
import Pyro4.util
from Library import Library

sys.excepthook = Pyro4.util.excepthook

library = Pyro4.Proxy("PYRONAME:example.library")

print("ADDING TEST INPUT for book in library.return_books():\n")

def printed_books(method): #Modified print function, if list loop through and print each item, else print as a string
    if type(method) is list:
        for book in method:
            print(book)
    else:
        print(method)

#################################### BOOKS ################################
print("BOOK1\n")
author = input("Add author: ")
title = input("Add title: ")
ISBN = input("Add ISBN: ")
year = int(input("Add year: "))

library.add_book(author, title, ISBN, year)

print("\nBOOK2")
author = input("\nAdd author: ")
title = input("Add title: ")
ISBN = input("Add ISBN: ")
year = int(input("Add year: "))

library.add_book(author, title, ISBN, year)

print("\nBOOK3")
author = input("\nAdd author: ")
title = input("Add title: ")
ISBN = input("Add ISBN: ")
year = int(input("Add year: "))

library.add_book(author, title, ISBN, year)


############################### RETURN ALL BOOKS UNSORTED ############################
print("\n**RETURN ALL BOOKS** (UNSORTED):\n")
printed_books(library.return_books())

############################### RETURN ALL BOOKS SORTED ############################
print("\n**RETURN ALL BOOKS SORTED BY YEAR**:\n")
printed_books(library.return_books_sorted())

############################### CHOOSE YEAR RANGE TO SEARCH BY YEAR ############################
print("\n**SEARCH YEAR RANGE**:\n")
start_year = int(input("Insert start year: "))
end_year = int(input("Insert end_year: "))
printed_books(library.select_by_year(start_year, end_year))

############################### TESTING LOAN COUNTER  ############################
print("\n**TESTING LOAN COUNTER**\n")

title = input("Which books to set on loan? (provide title): " ) #INPUT THE TITLE
library.set_on_loan(title)
print("\n**SETTING ON LOAN**:")

print("\nRound 1 - Current Library State:\n")
printed_books(library.return_books())

print("\n**SETTING NOT ON LOAN**:\n")
library.set_not_loan(title)
##_____________________________________________________________________________
print("Round 2 - Current Library State:\n")
printed_books(library.return_books())

print("\n**SETTING ON LOAN AGAIN**:\n")
library.set_on_loan(title)

print("Current library state:\n")
printed_books(library.return_books())

print("\n**SETTING NOT ON LOAN AGAIN**:")
library.set_not_loan(title)

print("\n**Round 2 end - library state**:")
printed_books(library.return_books())

######################## SEARCH BY ISBN VALUE #############################################

ISBN_value = int(input("\n**RETURN BOOKS BY ISBN INTEGER** Please choose Integer value:\n"))
printed_books(library.return_books_ISBN(ISBN_value))
