# main.py
from database import *
from book import books

def search_by_author(author):
    return [book for book in books if book['author'].lower() == author.lower()]

def search_by_genre(genre):
    return [book for book in books if book['genre'].lower() == genre.lower()]

def get_top_rated_books(n=5):
    return sorted(books, key=lambda x: x['rating'], reverse=True)[:n]

def main():
    while True:
        print("\n--- Book Recommendation System ---")
        print("1. Search by Author")
        print("2. Search by Genre")
        print("3. Get Top Rated Books")
        print("4. Add Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            author = input("Enter author name: ")
            results = search_by_author(author)
            if results:
                print("\nBooks by", author)
                for book in results:
                    print(f"- {book['title']} ({book['genre']}, Rating: {book['rating']})")
            else:
                print("No books found for this author.")

        elif choice == '2':
            genre = input("Enter genre: ")
            results = search_by_genre(genre)
            if results:
                print("\nBooks in", genre, "genre")
                for book in results:
                    print(f"- {book['title']} by {book['author']} (Rating: {book['rating']})")
            else:
                print("No books found for this genre.")

        elif choice == '3':
            top_books = get_top_rated_books()
            print("\nTop Rated Books:")
            for book in top_books:
                print(f"- {book['title']} by {book['author']} (Genre: {book['genre']}, Rating: {book['rating']})")
        
        
        elif choice == '4':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            genre = input("Enter genre: ")
            rating = float(input("Enter rating (out of 5): "))
            add_book(title, author, genre, rating)


        elif choice == '5':
            print("Exiting Book Recommendation System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
