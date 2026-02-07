import uuid
import pytest
from core.genre.application.exceptions import GenreNotFound
from core.genre.application.use_cases.get_genre import GetGenre
from core.genre.domain.genre import Genre
from core.genre.infra.in_memory_genre import InMemoryGenreRepository


class TestGetGenre:
    def test_return_found_genre(self):
        genre_drama = Genre(
            name="Filme",
            is_active=True
        )
        genre_horror = Genre(
            name="Horror",
            is_active=True
        )
        repository = InMemoryGenreRepository(
            genres=[genre_horror, genre_drama]
        )
        use_case = GetGenre(repository=repository)
        request = GetGenre.Input(
            id=genre_drama.id
        )

        response = use_case.execute(request)
        assert response.name == genre_drama.name
        assert response.is_active == genre_drama.is_active

    def test_when_genre_does_not_exists_than_raise_exception(self):
        genre_action = Genre(
            name="Action",
            is_active=True
        )
        genre_documentary = Genre(
            name="Documentary",
            is_active=True
        )
        repository = InMemoryGenreRepository(
            genres=[genre_action, genre_documentary]
        )

        use_case = GetGenre(repository=repository)
        request = GetGenre.Input(id=uuid.uuid4)

        with pytest.raises(GenreNotFound) as exc:
            use_case.execute(request)
