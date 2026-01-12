from core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from core.category.domain.category import Category
from core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestUpdateCategory:
    def test_can_update_category_name_and_description(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="Série",
            description="Categoria para séries"
        )
        use_case.execute(request)

        updated_category = repository.get_by_id(category.id)
        assert updated_category.name == "Série"
        assert updated_category.description == "Categoria para séries"
