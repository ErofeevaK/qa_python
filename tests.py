from main import BooksCollector

class TestBooksCollector:
    def setup(self):
        """Инициализация коллектора перед каждым тестом"""
        self.collector = BooksCollector()
        # Подготовка тестовых данных
        self.test_books = {
            'Фантастическая книга': 'Фантастика',
            'Ужастик': 'Ужасы', 
            'Мультфильм': 'Мультфильмы',
            'Комедия': 'Комедии',
            'Книга без жанра': ''
        }
        for book, genre in self.test_books.items():
            self.collector.add_new_book(book)
            if genre:
                self.collector.set_book_genre(book, genre)

    # Тесты для add_new_book
    def test_add_new_book_add_two_books(self):
        initial_count = len(self.collector.get_books_genre())
        self.collector.add_new_book('Новая книга 1')
        self.collector.add_new_book('Новая книга 2')
        assert len(self.collector.get_books_genre()) == initial_count + 2

    def test_add_new_book_name_length_40_chars_added(self):
        long_name = 'a' * 40
        self.collector.add_new_book(long_name)
        assert long_name in self.collector.get_books_genre()

    def test_add_new_book_name_length_41_chars_not_added(self):
        too_long_name = 'a' * 41
        self.collector.add_new_book(too_long_name)
        assert too_long_name not in self.collector.get_books_genre()

    def test_add_new_book_empty_name_not_added(self):
        self.collector.add_new_book('')
        assert '' not in self.collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self):
        initial_count = len(self.collector.get_books_genre())
        self.collector.add_new_book('Фантастическая книга')
        assert len(self.collector.get_books_genre()) == initial_count

    # Тесты для set_book_genre
    def test_set_book_genre_valid_genre(self):
        self.collector.set_book_genre('Книга без жанра', 'Фантастика')
        assert self.collector.get_book_genre('Книга без жанра') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        self.collector.set_book_genre('Фантастическая книга', 'Несуществующий жанр')
        assert self.collector.get_book_genre('Фантастическая книга') == 'Фантастика'  # Жанр не изменился

    def test_set_book_genre_nonexistent_book(self):
        initial_books = self.collector.get_books_genre()
        self.collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert self.collector.get_books_genre() == initial_books

    # Тесты для get_book_genre
    def test_get_book_genre_existing_book_with_genre(self):
        assert self.collector.get_book_genre('Фантастическая книга') == 'Фантастика'

    def test_get_book_genre_existing_book_without_genre(self):
        assert self.collector.get_book_genre('Книга без жанра') == ''

    def test_get_book_genre_nonexistent_book(self):
        assert self.collector.get_book_genre('Несуществующая книга') == ''

    # Тесты для get_books_genre
    def test_get_books_genre_returns_all_books(self):
        books = self.collector.get_books_genre()
        assert len(books) == len(self.test_books)
        for book in self.test_books:
            assert book in books

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre(self):
        fantasy_books = self.collector.get_books_with_specific_genre('Фантастика')
        assert len(fantasy_books) == 1
        assert 'Фантастическая книга' in fantasy_books

    def test_get_books_with_specific_genre_invalid_genre(self):
        books = self.collector.get_books_with_specific_genre('Несуществующий жанр')
        assert books == []

    # Тесты для get_books_for_children
    def test_get_books_for_children(self):
        children_books = self.collector.get_books_for_children()
        assert 'Мультфильм' in children_books
        assert 'Ужастик' not in children_books
        assert 'Комедия' in children_books  # Предполагаем, что комедии подходят детям

    # Тесты для работы с избранным
    def test_add_book_in_favorites(self):
        self.collector.add_book_in_favorites('Фантастическая книга')
        assert 'Фантастическая книга' in self.collector.get_list_of_favorites_books()

    def test_add_non_existent_book_in_favorites(self):
        initial_favorites = self.collector.get_list_of_favorites_books()
        self.collector.add_book_in_favorites('Несуществующая книга')
        assert self.collector.get_list_of_favorites_books() == initial_favorites

    def test_add_duplicate_book_in_favorites(self):
        self.collector.add_book_in_favorites('Фантастическая книга')
        initial_count = len(self.collector.get_list_of_favorites_books())
        self.collector.add_book_in_favorites('Фантастическая книга')
        assert len(self.collector.get_list_of_favorites_books()) == initial_count

    def test_delete_book_from_favorites(self):
        self.collector.add_book_in_favorites('Фантастическая книга')
        self.collector.delete_book_from_favorites('Фантастическая книга')
        assert 'Фантастическая книга' not in self.collector.get_list_of_favorites_books()

    def test_delete_non_existent_book_from_favorites(self):
        initial_favorites = self.collector.get_list_of_favorites_books()
        self.collector.delete_book_from_favorites('Несуществующая книга')
        assert self.collector.get_list_of_favorites_books() == initial_favorites

    def test_get_list_of_favorites_books(self):
        favorites = ['Фантастическая книга', 'Мультфильм']
        for book in favorites:
            self.collector.add_book_in_favorites(book)
        result = self.collector.get_list_of_favorites_books()
        assert len(result) == len(favorites)
        for book in favorites:
            assert book in result