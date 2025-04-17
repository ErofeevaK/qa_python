from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_length_40_chars_added_successfully(self):
        collector = BooksCollector()
        long_name = 'a' * 40
        collector.add_new_book(long_name)
        assert long_name in collector.get_books_genre()

    def test_add_new_book_name_length_41_chars_not_added(self):
        collector = BooksCollector()
        too_long_name = 'a' * 41
        collector.add_new_book(too_long_name)
        assert too_long_name not in collector.get_books_genre()

    def test_add_new_book_empty_name_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert '' not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        book_name = 'Книга'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre_set_successfully(self):
        collector = BooksCollector()
        book_name = 'Книга'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        book_name = 'Книга'
        invalid_genre = 'Несуществующий жанр'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, invalid_genre)
        assert collector.get_book_genre(book_name) == ''

    def test_set_book_genre_nonexistent_book_genre_not_set(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        book1 = 'Фантастическая книга'
        book2 = 'Еще фантастика'
        genre = 'Фантастика'
        collector.add_new_book(book1)
        collector.add_new_book(book2)
        collector.set_book_genre(book1, genre)
        collector.set_book_genre(book2, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book1 in books and book2 in books and len(books) == 2

    def test_get_books_with_specific_genre_invalid_genre_returns_empty_list(self):
        collector = BooksCollector()
        books = collector.get_books_with_specific_genre('Несуществующий жанр')
        assert books == []

    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()
        child_book = 'Мультфильм'
        adult_book = 'Ужастик'
        collector.add_new_book(child_book)
        collector.add_new_book(adult_book)
        collector.set_book_genre(child_book, 'Мультфильмы')
        collector.set_book_genre(adult_book, 'Ужасы')
        children_books = collector.get_books_for_children()
        assert child_book in children_books and adult_book not in children_books

    def test_add_book_in_favorites_adds_only_existing_books(self):
        collector = BooksCollector()
        book = 'Книга'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_non_existent_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_duplicate_not_added(self):
        collector = BooksCollector()
        book = 'Книга'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        book = 'Книга'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert book not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_non_existent_book_no_error(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Несуществующая книга')
        # Проверяем, что не возникло исключения
        assert True

    def test_get_list_of_favorites_books_returns_all_favorites(self):
        collector = BooksCollector()
        books = ['Книга1', 'Книга2', 'Книга3']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert all(book in favorites for book in books)