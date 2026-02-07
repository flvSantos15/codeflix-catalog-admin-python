from unittest.mock import create_autospec

import pytest
from core.genre.application.use_cases.list_genre import GenreOutput, ListGenre
from core.genre.domain.genre import Genre
from core.genre.domain.genre_repository import GenreRepository
from src.core.category.domain.category import Category


class TestListGenres:
    @pytest.fixture
    def category_movie(self) -> Category:
        return Category(
            name="Filme",
            description="Categoria de filmes",
        )

    @pytest.fixture
    def category_series(self) -> Category:
        return Category(
            name="Séries",
            description="Categoria de séries",
        )

    @pytest.fixture
    def genre_horror(self, category_movie: Category, category_series: Category) -> Genre:
        return Genre(
            name="Horror",
            categories={category_series.id, category_movie.id}
        )

    @pytest.fixture
    def genre_action(self, category_movie: Category, category_series: Category) -> Genre:
        return Genre(
            name="Action",
            categories={category_series.id, category_movie.id}
        )

    @pytest.fixture
    def mock_empty_repository(self) -> GenreRepository:
        repository = create_autospec(GenreRepository)
        repository.list.return_value = []
        return repository

    @pytest.fixture
    def mock_populated_repository(
        self,
        genre_action: Genre,
        genre_horror: Genre
    ) -> GenreRepository:
        repository = create_autospec(GenreRepository)
        repository.list.return_value = [
            genre_action,
            genre_horror,
        ]
        return repository

    def test_when_no_genres_then_return_empty_list(
        self,
        mock_empty_repository: GenreRepository,
    ) -> None:
        use_case = ListGenre(repository=mock_empty_repository)
        response = use_case.execute(input=ListGenre.Input())

        assert response == ListGenre.Output(data=[])

    def test_when_genres_exist_then_return_mapped_list(
        self,
        mock_populated_repository: GenreRepository,
        genre_action: Genre,
        genre_horror: Genre
    ) -> None:
        use_case = ListGenre(repository=mock_populated_repository)
        response = use_case.execute(input=ListGenre.Input())

        assert response == ListGenre.Output(
            data=[
                GenreOutput(
                    id=genre_action.id,
                    name=genre_action.name,
                    is_active=genre_action.is_active,
                    categories=genre_action.categories
                ),
                GenreOutput(
                    id=genre_horror.id,
                    name=genre_horror.name,
                    is_active=genre_horror.is_active,
                    categories=genre_horror.categories
                ),
            ]
        )
