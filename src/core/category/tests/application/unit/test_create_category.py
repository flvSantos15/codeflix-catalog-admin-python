import uuid
from unittest.mock import MagicMock

import pytest

from src.core.category.application.create_category import (
    CreateCategory,
    CreateCategoryRequest,
    CreateCategoryResponse,
    InvalidCategoryData,
)
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
          name="Filme",
          description="Categoria para filme",
          is_active=True,
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response, CreateCategoryResponse)
        assert mock_repository.save.called

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(name="")

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            use_case.execute(request)

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"
