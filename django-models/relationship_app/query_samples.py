import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Example data
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George R.R. Martin")

    book1 = Book.objects.create(title="Harry Potter", author=author1)
    book2 = Book.objects.create(title="Game of Thrones", author=author2)
    book3 = Book.objects.create(title="Fantastic Beasts", author=author1)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2)

    librarian1 = Librarian.objects.create(name="Alice", library=library1)

    # Queries
    print("Books by J.K. Rowling:")
    for book in Book.objects.filter(author=author1):
        print("-", book.title)

    print("\nBooks in Central Library:")
    for book in library1.books.all():
        print("-", book.title)

    print(f"\nLibrarian of {library1.name}: {library1.librarian.name}")

if __name__ == "__main__":
    run_queries()
