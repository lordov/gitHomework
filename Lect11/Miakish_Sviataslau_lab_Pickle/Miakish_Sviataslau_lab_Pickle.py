import pickle


class Book:
    def __init__(self):
        self.pages = []
    
    def add_page(self, text):
        self.pages.append(f'Page: {len(self.pages) + 1} - {text}')

    def __iter__(self):
        return iter(self.pages)


book = Book()
for i in range(1, 8):
    book.add_page(f'the page number is {i}')

for page in book:
    print(page)

with open('data.pickle', 'wb') as fo:
    pickle.dump(book, fo)

with open('data.pickle', 'rb') as fo:
    new_book = pickle.load(fo)

for page in new_book:
    print(page)
    