import uuid
from core.category.domain.category import Category
from core.genre.application.use_cases.delete_genre import DeleteGenre
from core.genre.domain.genre import Genre
from core.genre.infra.in_memory_genre import InMemoryGenreRepository


class TestDeleteCategory:
    def test_delete_genre_from_repository(self):
        category_serie = Category(
            id=uuid.uuid4(),
            name="Série",
            description="Categoria para series",
            is_active=True
        )

        genre = Genre(
            id=uuid.uuid4(),
            name="Drama",
            is_active=True,
            categories={category_serie.id}
        )

        repository = InMemoryGenreRepository(genres=[genre])

        use_case = DeleteGenre(repository=repository)
        request = DeleteGenre.Input(id=genre.id)

        assert repository.get_by_id(genre.id) is not None
        response = use_case.execute(request)

        assert repository.get_by_id(genre.id) is None
        assert response is None
