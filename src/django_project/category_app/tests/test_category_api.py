import pytest
from rest_framework import status
from rest_framework.test import APIClient
from core.category.domain.category import Category

from django_project.category_app.repository import DjangoORMCategoryRepository


@pytest.mark.django_db
class TestCategoryAPI:
    @pytest.fixture
    def category_movie(self):
        return Category(
            name="Movie",
            description="Movie category"
        )

    @pytest.fixture
    def category_documentary(self):
        return Category(
            name="DOcumentary",
            description="Documentary category"
        )

    @pytest.fixture
    def category_repository(self) -> DjangoORMCategoryRepository:
        return DjangoORMCategoryRepository()

    def test_list_categories(
        self,
        category_movie: Category,
        category_documentary: Category,
        category_repository: DjangoORMCategoryRepository,
    ) -> None:
        category_repository.save(category_movie)
        category_repository.save(category_documentary)

        url = "/api/categories/"
        response = APIClient().get(url)

        expected_data = [
            {
                "id": str(category_movie.id),
                "name": category_movie.name,
                "description": category_movie.description,
                "is_active": category_movie.is_active
            },
            {
                "id": str(category_documentary.id),
                "name": category_documentary.name,
                "description": category_documentary.description,
                "is_active": category_documentary.is_active
            }
        ]

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data == expected_data
