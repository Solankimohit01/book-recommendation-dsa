from book import books
books = []

def add_book(title, author, genre, rating):
    books.append({"title": title, "author": author, "genre": genre, "rating": rating})
    print(f"Book '{title}' added successfully!")

def search_by_author(author):
    found = False
    for book in books:
        if book['author'].lower() == author.lower():
            print(f"{book['title']} - {book['genre']} - Rating: {book['rating']}")
            found = True
    if not found:
        print("No books found for this author.")

def search_by_genre(genre):
    found = False
    for book in books:
        if book['genre'].lower() == genre.lower():
            print(f"{book['title']} by {book['author']} - Rating: {book['rating']}")
            found = True
    if not found:
        print("No books found for this genre.")

def recommend_top_books():
    if not books:
        print("No books in database.")
        return
    top_books = sorted(books, key=lambda x: x['rating'], reverse=True)
    print("Top Rated Books:")
    for book in top_books[:5]:
        print(f"{book['title']} by {book['author']} - {book['rating']}/5")
