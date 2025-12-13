from uuid import UUID
from src.core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestGetCategory:
  def test_get_category_by_id(self):
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

    assert response == GetCategoryRequest(
      id=category_filme.id,
      name="Filme",
      description="Categoria para filmes",
      is_active=True
    )