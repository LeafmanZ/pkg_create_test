import pandas as pd
class BookLover:
    
    # constructor
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name # string type
        self.email = email # string type
        self.fav_genre = fav_genre # string type
        self.num_books = num_books # int type
        self.book_list = book_list # dataframe type
        
    def add_book(self, book_name, rating):
        if type(book_name) != str:
            raise TypeError('book name must be a string')
        elif type(rating) != int:
            raise TypeError('rating must be an integer')
        elif rating > 5 or rating < 0:
            raise ValueError('rating must be between values of 0 and 5 inclusive')
        elif self.has_read(book_name):
            print('book has already been read')
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            
            self.num_books += 1
            
    def has_read(self, book_name):
        """ This function takes book_name (string) as input and determines if the person has read the book.
            That is, if that book name is in book_list.
            Again, it is sufficient to match on book_name.
            The method should return True if the person has read the book, False otherwise."""
        
        return book_name in list(self.book_list.book_name)

    def num_books_read(self): 
        return self.num_books
    
    def fav_books(self):
        return self.book_list.loc[self.book_list.book_rating > 3]