from unittest.mock import create_autospec
import uuid

import pytest
from core.genre.application.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository
from src.core.genre.application.use_cases.get_genre import GetGenre
from src.core.genre.domain.genre import Genre

from src.core.category.domain.category import Category


class TestGetGenre:
    def test_when_genre_exists_then_return_response_dto(self):
        movie_category = Category(name="Movie")
        serie_category = Category(name="Serie")

        mock_genre = Genre(
            id=uuid.uuid4(),
            name="Horror",
            is_active=True,
            categories={movie_category.id, serie_category.id}
        )
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = mock_genre

        use_case = GetGenre(repository=mock_repository)
        request = GetGenre.Input(id=mock_genre.id)

        response = use_case.execute(request)

        assert response == GetGenre.Output(
            id=mock_genre.id,
            name="Horror",
            is_active=True,
            categories={movie_category.id, serie_category.id}
        )

    def test_when_genre_not_found_then_raise_exception(self):
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = None

        use_case = GetGenre(repository=mock_repository)
        request = GetGenre.Input(id=uuid.uuid4())

        with pytest.raises(GenreNotFound):
            use_case.execute(request)
