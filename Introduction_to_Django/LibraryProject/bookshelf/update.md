# Update Book
```python
newbook = Book.objects.get(title='1984')
newbook.title = 'Nineteen Eighty-Four'
newbook.save()