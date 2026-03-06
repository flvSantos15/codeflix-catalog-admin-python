import uuid

from rest_framework.test import APIClient
from rest_framework import status
import pytest

from core.category.domain.category import Category
from core.genre.domain.genre import Genre
from django_project.category_app.repository import DjangoORMCategoryRepository
from django_project.genre_app.repository import DjangoORMGenreRepository


@pytest.fixture
def category_movie():
    return Category(
        name="Movie",
        description="Movie description"
    )


@pytest.fixture
def category_documentary():
    return Category(
        name="Documentary",
        description="Documentary description"
    )


@pytest.fixture
def category_repository() -> DjangoORMCategoryRepository:
    return DjangoORMCategoryRepository()


@pytest.fixture
def genre_romance(category_movie, category_documentary) -> Genre:
    return Genre(
        name="Romance",
        is_active=True,
        categories={category_documentary.id, category_movie.id}
    )


@pytest.fixture
def genre_drama() -> Genre:
    return Genre(
        name="Drama",
        is_active=True,
        categories=set()
    )


@pytest.fixture
def genre_repository() -> DjangoORMGenreRepository:
    return DjangoORMGenreRepository()


@pytest.mark.django_db
class TestListAPI:
    def test_list_genres_and_categories(
        self,
        genre_romance,
        genre_drama,
        genre_repository,
        category_repository,
        category_documentary,
        category_movie
    ):
        category_repository.save(category_movie)
        category_repository.save(category_documentary)

        genre_repository.save(genre_romance)
        genre_repository.save(genre_drama)

        url = "/api/genres/"
        response = APIClient().get(url)

        # expected_response = {
        #     "data": [
        #         {
        #             "id": str(genre_romance.id),
        #             "name": "Romance",
        #             "is_active": True,
        #             "categories": [
        #                 str(category_documentary.id),
        #                 str(category_movie.id),
        #             ]
        #         },
        #         {
        #             "id": str(genre_drama.id),
        #             "name": "Drama",
        #             "is_active": True,
        #             "categories": []
        #         }
        #     ]
        # }

        assert response.status_code == status.HTTP_200_OK
        # assert response.data == expected_response

        assert response.data["data"]
        assert response.data["data"][0]["id"] == str(genre_romance.id)
        assert response.data["data"][0]["name"] == "Romance"
        assert response.data["data"][0]["is_active"] is True
        assert set(response.data["data"][0]["categories"]) == {
            str(category_documentary.id),
            str(category_movie.id),
        }

        assert response.data["data"]
        assert response.data["data"][1]["id"] == str(genre_drama.id)
        assert response.data["data"][1]["name"] == "Drama"
        assert response.data["data"][1]["is_active"] is True
        assert response.data["data"][1]["categories"] == []


@pytest.mark.django_db
class TestCreateAPI:
    def test_create_genre_with_associated_categories(
        self,
        category_movie,
        category_documentary,
        category_repository,
        genre_repository
    ):
        category_repository.save(category_movie)
        category_repository.save(category_documentary)

        url = "/api/genres/"
        data = {
            "name": "Drama",
            "categories": [
                str(category_movie.id),
                str(category_documentary.id)
            ]
        }
        response = APIClient().post(url, data)

        assert response.status_code == 201
        assert response.data["id"]
        created_genre_id = response.data["id"]

        saved_genre = genre_repository.get_by_id(created_genre_id)
        assert saved_genre.name == "Drama"
        assert saved_genre.categories == {
            category_movie.id,
            category_documentary.id
        }


@pytest.mark.django_db
class TestUpdateAPI:
    def test_when_request_data_is_valid_then_update_genre(self):
        pass

    def test_when_request_data_is_invalid_then_return_400(self):
        pass

    def test_when_related_categories_do_not_exist_then_return_400(
        self,
        category_movie: Category,
        category_documentary: Category,
        category_repository: DjangoORMCategoryRepository,
        genre_drama: Genre,
        genre_repository: DjangoORMGenreRepository
    ):
        category_repository.save(category_movie)
        category_repository.save(category_documentary)
        genre_repository.save(genre_drama)

        url = f"/api/genres/{str(genre_drama.id)}/"
        data = {
            "name": "Drama",
            "is_active": True,
            "categories": [uuid.uuid4()]
        }
        response = APIClient().put(url, data)

        assert response.status_code == 400

    def test_when_genre_does_not_exist_then_return_404(self):
        url = f"/api/genres/{uuid.uuid4()}/"
        data = {
            "name": "Drama",
            "is_active": True,
            "categories": []
        }
        response = APIClient().put(url, data)

        assert response.status_code == 404


@pytest.mark.django_db
class TestDeleteAPI:
    def test_when_genre_does_not_exists_then_raise_404(self):
        url = f"/api/genres/{uuid.uuid4()}/"
        response = APIClient().delete(url)

        assert response.status_code == 404

    def test_when_pk_is_invalid_then_return_400(self):
        url = "/api/genres/invalid_pk/"
        response = APIClient().delete(url)

        assert response.status_code == 400

    def test_delete_genre_from_respository(self):
        # me certificar que existe no repo
        # deletar e me cerfiticar que não esta mais no repo
        pass
