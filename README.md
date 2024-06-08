# Project Name
List of Book App

## Introduction
The **List of Book App** is developed for assessment purposes. This application queries a database and applies custom logic to provide specific results based on user requests.

## Features / URL 
- list all the books : http://127.0.0.1:8000/
- Show publisher has more than 1 author and sort it by high revenue per author : http://127.0.0.1:8000/?filter_by=publisher&custom_filter=more_author&filter_2=&sort_by=revenue&sort_order=desc
- Show publisher has more than 1 author and sort it by the lowest revenue per author : http://127.0.0.1:8000/?filter_by=publisher&custom_filter=more_author&filter_2=&sort_by=revenue&sort_order=asc
- Show Authors with highest revenue per page written : http://127.0.0.1:8000/?filter_by=author&custom_filter=high_rev_per_page&filter_2=&sort_by=revenue&sort_order=desc
- list of all the books written by 1 author and publisher attached to that book, who has the most revenue : http://127.0.0.1:8000/?filter_by=book&custom_filter=1_author&filter_2=pub_most_rev&sort_by=revenue&sort_order=desc

## Installation

### Prerequisites
- Python version (e.g., Python 3.8+)
- Django version (e.g., Django 3.2+)


### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/mamoloj/booklist.git
    cd booklist
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Cd to the app:
    ```bash
    cd booksproject
    ```
5. Run the development server:
    ```bash
    python manage.py runserver
    ```

