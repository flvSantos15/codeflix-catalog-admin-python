import uuid
from unittest.mock import MagicMock

import pytest

from src.core.category.application.create_category import (
    InvalidCategoryData,
    create_category,
)
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        category_id = create_category(
            repository=mock_repository,
            name="Filme",
            description="Categoria para filme",
            is_active=True,
        )

        assert category_id is not None
        assert isinstance(category_id, uuid.UUID)

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(InMemoryCategoryRepository)
        with pytest.raises(InvalidCategoryData, match="name cannot be empty"):
            category_id = create_category(
                repository=mock_repository,
                name="",
            )

            assert category_id
