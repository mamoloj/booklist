from django.shortcuts import render
from .models import Publisher, Author, Book
from django.db.models import Count, Q, Sum, F, FloatField
from django.db.models.functions import Cast

def book_list(request):
    filter_by = request.GET.get('filter_by',None)
    custom_filter = request.GET.get('custom_filter',None)
    filter_2 = request.GET.get('filter_2',None)
    sort_by = request.GET.get('sort_by',None)
    sort_order = request.GET.get('sort_order',None)
    table_columns = ['Title','Publisher','Authors','Revenue','Page Written']
    books = None
    publishers = None
    authors = None
    books_with_top_publishers = None
    if filter_by and custom_filter:
        if filter_by == 'publisher':
            table_columns = ['Publisher','Number of Authors','Total Pages Written','Total Revenue','Total Revenue Per Page']

            if custom_filter == 'more_author':
                publishers = Publisher.objects.annotate(
                    total_authors=Count('book__authors', distinct=True)).filter(total_authors__gt=1)
            elif custom_filter == '1_author':
                publishers = Publisher.objects.annotate(
                    total_authors=Count('book__authors', distinct=True)).filter(total_authors=1)
            elif custom_filter == 'high_rev_per_page':
                publishers = Publisher.objects.all()
                table_columns.remove('Number of Authors')

            publishers = publishers.annotate(
                total_revenue=Sum('book__revenue'),
                total_pages_written=Sum('book__pages_written')
            )
            publishers = publishers.annotate(
                revenue_per_page=Cast(F('total_revenue'), FloatField()) / F('total_pages_written')
            )

            if sort_by and sort_order:
                if sort_order == 'desc':
                    publishers = publishers.order_by("-revenue_per_page")
                else:
                    publishers = publishers.order_by("revenue_per_page")

        elif filter_by == 'author':
            authors = Author.objects.all()
            table_columns = ['Authors', 'Total Pages Written', 'Total Revenue', 'Total Revenue Per Page']
            if custom_filter == 'high_rev_per_page':
                authors = authors.annotate(
                    total_revenue=Sum('book__revenue'),
                    total_pages_written=Sum('book__pages_written')
                ).annotate(
                    revenue_per_page=Cast(F('total_revenue'), FloatField()) / F('total_pages_written')
                )

                if sort_by and sort_order:
                    if sort_order == 'desc':
                        authors = authors.order_by("-revenue_per_page")
                    else:
                        authors = authors.order_by("revenue_per_page")
        elif filter_by == 'book':
            books_filtered = Book.objects.all()
            if custom_filter == '1_author':
                books_filtered = books_filtered.annotate(
                    author_count=Count('authors')
                ).filter(author_count=1)
            elif custom_filter == 'more_author':
                books_filtered = books_filtered.annotate(
                    author_count=Count('authors')
                ).filter(author_count__gt=1)

            if filter_2 == 'pub_most_rev':
                publishers_with_revenue = Publisher.objects.annotate(
                    total_revenue=Sum('book__revenue')
                )
                publisher_revenue_dict = {publisher.id: publisher.total_revenue for publisher in
                                          publishers_with_revenue}
                books_with_top_publishers = []
                for book in books_filtered:
                    publisher_id = book.publisher_id
                    if publisher_id in publisher_revenue_dict:
                        top_publisher = Publisher.objects.get(id=publisher_id)
                        books_with_top_publishers.append({
                            'book': book,
                            'top_publisher': top_publisher,
                            'publisher_revenue': publisher_revenue_dict[publisher_id]
                        })
                table_columns = ['Title','Top Publisher','Publisher Revenue']
    else :
        books = Book.objects.all()


    template = 'index.html'
    data = {
        'table_columns': table_columns,
        'filter_by': filter_by,
        'custom_filter': custom_filter,
        'filter_2': filter_2,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'publishers': publishers,
        'authors': authors,
        'books': books,
        'books_filtered' : books_with_top_publishers,

    }
    return render(request, template, data)
