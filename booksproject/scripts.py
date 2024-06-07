# Import necessary modules
import os
import django
import random
from faker import Faker


# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booksproject.settings')
django.setup()
from booklist.models import Publisher, Author, Book
# Your data generation function
fake = Faker()


def generate_data(num_entries=100):
    for _ in range(num_entries):
        publisher_name = fake.company()
        author_name = fake.name()
        additional_author_name = fake.name()  # Generate a new author name

        title = fake.sentence(nb_words=6, variable_nb_words=True)
        revenue = round(random.uniform(100, 1000), 2)
        pages_written = random.randint(50, 500)

        # Create Publisher if not exists
        publisher, _ = Publisher.objects.get_or_create(name=publisher_name)

        # Create Author if not exists
        author, _ = Author.objects.get_or_create(name=author_name)

        # Create additional Author
        additional_author, _ = Author.objects.get_or_create(name=additional_author_name)

        # Create Book
        book = Book.objects.create(title=title, publisher=publisher, revenue=revenue, pages_written=pages_written)
        book.authors.add(author, additional_author)  # Add both authors to the book


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
    import django

    django.setup()

    generate_data()