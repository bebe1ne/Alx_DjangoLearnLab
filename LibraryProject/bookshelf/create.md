# Create Book
```python
from bookshelf.models import Book
newbook = Book(title='1984', author='George Orwell', publication_year=1949)
newbook.save() 
# Expected Output: <Book: 1984>