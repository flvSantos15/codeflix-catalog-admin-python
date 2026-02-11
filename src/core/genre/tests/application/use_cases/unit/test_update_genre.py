from unittest.mock import create_autospec
import uuid

import pytest
from core.category.domain.category_repository import CategoryRepository
from core.category.domain.category import Category
from core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from core.genre.application.use_cases.update_genre import UpdateGenre
from core.genre.domain.genre import Genre
from core.genre.domain.genre_repository import GenreRepository


@pytest.fixture
def movie_category() -> Category:
    return Category(name="Movie")


@pytest.fixture
def documentary_category() -> Category:
    return Category(name="Documentary")


@pytest.fixture
def mock_category_repository_with_categories(movie_category, documentary_category) -> CategoryRepository:
    repository = create_autospec(CategoryRepository)
    repository.list.return_value = [movie_category]

    return repository


class TestUpdateGenre:
    def test_update_genre_name(self):
        genre = Genre(
            id=uuid.uuid4(),
            name="Drama",
            is_active=True
        )

        mock_category_repository = create_autospec(CategoryRepository)
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = genre

        use_case = UpdateGenre(
            repository=mock_repository,
            category_repository=mock_category_repository
        )
        request = UpdateGenre.Input(
            id=genre.id,
            name="Horror"
        )
        use_case.execute(request)

        assert genre.name == "Horror"
        mock_repository.update.assert_called_once_with(genre)

    def test_can_deactivate_genre(self):
        genre = Genre(
            id=uuid.uuid4(),
            name="Action",
            is_active=True
        )

        mock_category_repository = create_autospec(CategoryRepository)
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = genre

        use_case = UpdateGenre(
            repository=mock_repository,
            category_repository=mock_category_repository
        )
        request = UpdateGenre.Input(
            id=genre.id,
            is_active=False
        )

        use_case.execute(request)

        assert genre.name == "Action"
        assert genre.is_active == False

    def test_can_activate_genre(self):
        genre = Genre(
            id=uuid.uuid4(),
            name="Romance",
            is_active=False
        )

        mock_category_repository = create_autospec(CategoryRepository)
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = genre

        use_case = UpdateGenre(
            repository=mock_repository,
            category_repository=mock_category_repository
        )
        request = UpdateGenre.Input(
            id=genre.id,
            is_active=True
        )

        use_case.execute(request)

        assert genre.name == "Romance"
        assert genre.is_active == True

    def test_when_categories_do_not_exist_then_raise_related_categories_not_found(
            self
    ):
        pass

    def test_can_add_categories(
        self,
        documentary_category,
        movie_category,
        mock_category_repository_with_categories
    ):
        genre = Genre(
            id=uuid.uuid4(),
            name="Drama",
            categories={movie_category.id}
        )
        mock_repository = create_autospec(GenreRepository)
        mock_repository.get_by_id.return_value = genre

        use_case = UpdateGenre(
            repository=mock_repository,
            category_repository=mock_category_repository_with_categories
        )

        input = UpdateGenre.Input(
            id=genre.id,
            name="Drama"
        )
        output = use_case.execute(input)

        assert genre.name == "Drama"
        assert genre.is_active == True
        mock_repository.update.assert_called_once_with(
            Genre(
                id=output.id,
                name="Drama",
                is_active=True,
                categories={movie_category.id, documentary_category.id}
            )
        )
        assert genre.categories == mock_category_repository_with_categories

    def test_can_remove_categories(self):
        pass
