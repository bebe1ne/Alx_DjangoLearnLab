# Delete Book
```python
from bookshelf.models import Book
newbook = Book.objects.get(title='Nineteen Eighty-Four')
newbook.delete()
Book.objects.all()

# Expected Output: <QuerySet []>
