import book_pb2

book = book_pb2.Book(
    isbn="1234567890",
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    publisher="Scribner",
    published_date="1925-04-10",
    price=10.99,
    page_count=180,
    genre="Fiction"
)

book.title = "응"
serialized_book = book.SerializeToString()

print('시리얼라이징')
print(serialized_book)
print(type(serialized_book))

deserialized_book = book_pb2.Book()
deserialized_book.ParseFromString(serialized_book)

print("--------------------------------")

print('디시리얼라이징')
print(deserialized_book)
print(type(deserialized_book))