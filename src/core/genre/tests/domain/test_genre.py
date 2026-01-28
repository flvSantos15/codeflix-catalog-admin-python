import uuid
import pytest
from src.core.genre.domain.genre import Genre


class TestGenre:
    def test_name_is_required(self):
        with pytest.raises(
            TypeError, match="missing 1 required positional argument: 'name'"
        ):
            Genre()

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name cannot be longer than 255"):
            Genre(name="a" * 256)

    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            Genre(name="")

    def test_created_genre_with_default_values(self):
        genre = Genre("Romance")
        assert genre.name == "Romance"
        assert genre.is_active is True
        assert isinstance(genre.id, uuid.UUID)
        assert genre.categories == set()

    def test_genre_is_created_with_provided_values(self):
        genre_id = uuid.uuid4()
        categories = {uuid.uuid4(), uuid.uuid4()}
        genre = Genre(
            id=genre_id,
            name="Romance",
            is_active=False,
            categories=categories
        )
        assert genre.id == genre_id
        assert genre.name == "Romance"
        assert genre.is_active is False
        assert genre.categories == categories


class TestActivateGenre:
    def test_activate_inactive_genre(self):
        genre = Genre(
            name="Romance",
            is_active=False
        )

        genre.activate()

        assert genre.is_active is True

    def test_activate_active_genre(self):
        genre = Genre(
            name="Romance",
            is_active=True
        )

        genre.activate()

        assert genre.is_active is True


class TestDeactivateGenre:
    def test_deactivate_active_genre(self):
        genre = Genre(
            name="Romance",
            is_active=True
        )

        genre.deactivate()

        assert genre.is_active is False

    def test_activate_inactive_genre(self):
        genre = Genre(
            name="Romance",
            is_active=False
        )

        genre.deactivate()

        assert genre.is_active is False


class TestEquality:
    def test_when_genres_have_same_id_they_are_equal(self):
        common_id = uuid.uuid4()
        genre_1 = Genre(
            id=common_id,
            name="Horror",
            is_active=True
        )
        genre_2 = Genre(
            id=common_id,
            name="Horror",
            is_active=True
        )

        assert genre_1 == genre_2

    def test_when_genres_have_different_id_they_are_not_equal(self):
        class Dymmy:
            pass

        common_id = uuid.uuid4()
        genre = Genre(id=uuid.uuid4(), name="Drama")
        dummy = Dymmy()
        dummy.id = common_id

        assert genre != dummy
