from core.genre.application.use_cases.update_genre import UpdateGenre
from core.genre.domain.genre import Genre
from core.genre.infra.in_memory_genre import InMemoryGenreRepository


class TestUpdateCategory:
    def test_can_update_genre_name(self):
        repository = InMemoryGenreRepository()
        genre = Genre(
            name="Horror",
        )

        repository.save(genre)
        category_id = genre.id

        created_genre = repository.get_by_id(category_id)
        assert created_genre.id == genre.id
        assert created_genre.name == genre.name

        use_case = UpdateGenre(repository=repository)
        request = UpdateGenre.Input(
            id=genre.id,
            name="Action"
        )
        use_case.execute(request)

        updated_genre = repository.get_by_id(genre.id)
        assert updated_genre.name == "Action"
        assert updated_genre.is_active == True
