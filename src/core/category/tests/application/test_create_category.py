import uuid
from unittest.mock import MagicMock

import pytest

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.create_category import (
    CreateCategory,
    CreateCategoryRequest,
    InvalidCategoryData,
)


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
          name="Filme",
          description="Categoria para filme",
          is_active=True,
        )

        category_id = use_case.execute(request)

        assert category_id is not None
        assert isinstance(category_id, uuid.UUID)
        assert mock_repository.save.called

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(name="")

        with pytest.raises(InvalidCategoryData, match="name cannot be empty") as exc_info:
            category_id = use_case.execute(request)

        assert exc_info.type is InvalidCategoryData
        assert str(exc_info.value) == "name cannot be empty"
