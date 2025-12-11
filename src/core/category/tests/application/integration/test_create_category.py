from uuid import UUID
from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestCreateCategory:
  def test_create_category_with_valida_data(self):
    repository = InMemoryCategoryRepository()
    use_case = CreateCategory(repository=repository)
    request = CreateCategoryRequest(
      name="Filme",
      description="Categoria para filmes",
      is_active=True
    )

    category_id = use_case.execute(request)

    assert category_id
    assert isinstance(category_id, UUID)
    assert len(repository.categories) == 1
    
    persisted_category = repository.categories[0]
    assert persisted_category.id == category_id
    assert persisted_category.name == "Filme"
    assert persisted_category.description == "Categoria para filmes"
    assert persisted_category.is_active == True