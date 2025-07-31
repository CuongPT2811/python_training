"""Assignment 4: Mini-Library Data Queries"""

import csv


class Book:
    '''
    Book class to store attributes of 
    '''
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = int(year)
        self.pages = int(pages)

    #Can define a __str__ before using __repr__
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, pages={self.pages})"
    

class Library:
    def __init__(self, csv_filepath):
        self.books = []
        try: # Load data
            with open(csv_filepath, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(row['title'], row['author'], row['year'], row['pages'])
                    self.books.append(book)
        except FileNotFoundError:
            print(f"Error: Can not find file from path '{csv_filepath}'.")
        except Exception as e:
            print(f"Error while reading file: {e}")     

    def by_author(self, name):
        #To update: Query author name/book which no need to search full name
        return [book.title for book in self.books 
                if book.author.lower() == name.lower()]
    
    def published_before(self, year):
        #To update: Add a flag to check before or after (use before=True)
        return [book for book in self.books if book.year < year]
    
    #Update: can query books have pages less/more than a number
    # def total_pages(self, total_pages, less_than = True):
    #     pass

    def total_pages(self):
        return sum(book.pages for book in self.books)
    
if __name__ == "__main__":
    csv_path = "D:/py_code_dump/git/python_training/python_training_assignments/lecture_4_assignment/books.csv"
    my_library = Library(csv_path)

    if my_library.books:
        print(f"Library loaded successfully with: {len(my_library.books)} books")

    author_name_to_find = input("Input author name: ")
    titles = my_library.by_author(author_name_to_find)
    if titles:
        print(f"Books by {author_name_to_find}: {titles}\n")
    else:
        print(f"Could not find any books by author {author_name_to_find} ")

    year_to_check = int(input("Enter the year to check: "))
    book_published_before = my_library.published_before(year_to_check)
    if book_published_before:
        print(f"Books published before {year_to_check}: ")
        for book in book_published_before:
            print(f"- {book.title} (Year: {book.year})")
    else:
        print(f"Could not find books published before {year_to_check}")
    print()

    print(f"Total pages of books: {my_library.total_pages()}")
    