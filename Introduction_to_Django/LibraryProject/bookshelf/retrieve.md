# Retrieve Book
```python
newbook = Book.objects.get(title='1984')
print(newbook)
# Expected Output: 1984 by George Orwell, published in 1949