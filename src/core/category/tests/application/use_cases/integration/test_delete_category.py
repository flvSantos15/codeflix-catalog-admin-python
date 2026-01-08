import uuid
from core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from core.category.application.use_cases.get_category import GetCategory
from core.category.domain.category import Category
from core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestDeleteCategory:
    def test_delete_category_from_repository(self):
        category_filme = Category(
            id=uuid.uuid4(),
            name="Filme",
            description="Categoria para filmes",
            is_active=True
        )
        category_serie = Category(
            id=uuid.uuid4(),
            name="Série",
            description="Categoria para series",
            is_active=True
        )

        repository = InMemoryCategoryRepository(
            categories=[
                category_filme,
                category_serie
            ]
        )

        use_case = DeleteCategory(repository=repository)
        request = DeleteCategoryRequest(id=category_filme.id)

        assert repository.get_by_id(category_filme.id) is not None
        response = use_case.execute(request)

        assert repository.get_by_id(category_filme.id) is None
        assert response is None
