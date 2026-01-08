from uuid import UUID
import uuid
import pytest
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound


class TestGetCategory:
  def test_return_found_category(self):
    category_filme = Category(
      name="Filme",
      description="Categoria para filmes",
      is_active=True
    )
    category_series = Category(
      name="Serie",
      description="Categoria para series",
      is_active=True
    )
    repository = InMemoryCategoryRepository(
      categories=[category_filme, category_series]
    )
    use_case = GetCategory(repository=repository)
    request = GetCategoryRequest(
      id=category_filme.id
    )

    response = use_case.execute(request)
    print(response, "test_get_category")
    assert response.name == category_filme.name
    assert response.description == category_filme.description
    assert response.is_active == category_filme.is_active

  def test_when_category_does_not_exists_than_raise_exception(self):
    category_filme = Category(
      name="Filme",
      description="Categoria para filmes",
      is_active=True
    )
    category_series = Category(
      name="Series",
      description="Categoria para series",
      is_active=True
    )
    repository = InMemoryCategoryRepository(
      categories=[category_filme, category_series]
    )

    use_case = GetCategory(repository=repository)
    request = GetCategoryRequest(id=uuid.uuid4)

    with pytest.raises(CategoryNotFound) as exc:
      use_case.execute(request)



