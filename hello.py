num_books = int(input("How many books? "))
books = []

for i in range(num_books):
    title = input(f"Book {i + 1} title: ")
    pages = int(input(f"Book {i + 1} pages: "))
    rating = int(input(f"Book {i + 1} rating (1-5): "))
    books.append({"title": title, "pages": pages, "rating": rating})

# Accumulator: total pages and total rating for average
total_pages = 0
total_rating = 0
for book in books:
    total_pages += book["pages"]
    total_rating += book["rating"]
average_rating = total_rating / len(books)

# Min/Max: find highest-rated book
top_book = books[0]
for book in books:
    if book["rating"] > top_book["rating"]:
        top_book = book

# Filter: books rated 4 or higher
favorites = []
for book in books:
    if book["rating"] >= 4:
        favorites.append(book["title"])

# Output
print("---")
print("Book Collection")
print("---")
for book in books:
    print(f"{book['title']}: {book['pages']} pages ({book['rating']}/5)")

print("---")
print(f"Total pages: {total_pages}")
print(f"Average rating: {average_rating}")
print(f"Top rated: {top_book['title']} ({top_book['rating']}/5)")

if len(favorites) > 0:
    print(f"Favorites (4+): {', '.join(favorites)}")
else:
    print("Favorites (4+): none")