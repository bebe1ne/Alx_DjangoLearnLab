# CRUD Operations for Book Model

## Create a Book Instance

```python
from bookshelf.models import Book
book = Book.objects.create(title='1984', author='George Orwell', publication_year=1949)
# Expected Output: <Book: 1984>

 Retrieve the Book

book = Book.objects.get(title='1984')
print(book)
# Expected Output: 1984 by George Orwell, published in 1949


Update the Book Title


book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
# Expected Output: <Book: Nineteen Eighty-Four>


Delete the Book Instance

book = Book.objects.get(title='Nineteen Eighty-Four')
book.delete()
Book.objects.all()

