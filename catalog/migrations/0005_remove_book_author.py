from django.db import migrations


def authorize_books(apps, schema_editor):
    Author = apps.get_model("catalog", "Author")
    Book = apps.get_model("catalog", "Book")
    BookAuthor = apps.get_model("catalog", "BookAuthor")

    for book in Book.objects.exclude(author=None):
        BookAuthor.objects.get_or_create(
            book=book, author=book.author, defaults={"author_order": 1}
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_bookauthor_book_authors'),
    ]

    operations = [
        migrations.RunPython(authorize_books, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
    ]
