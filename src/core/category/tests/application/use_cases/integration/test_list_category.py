from core.category.application.category_repository import CategoryRepository
from core.category.application.use_cases.list_category import CategoryOutput, ListCategory, ListCategoryRequest, ListCategoryResponse
from core.category.domain.category import Category
from core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestListCategory:
    def test_return_empty_list(self):
        category = Category(
            name="Filme",
            description="Categoria para filmes"
        )

        repository = InMemoryCategoryRepository(categories=[])

        use_case = ListCategory(repository=repository)
        request = ListCategoryRequest()
        response = use_case.execute(request)

        assert response == ListCategoryResponse(data=[])

    def test_return_existing_categorie(self):
        category_filme = Category(
            name="Filme",
            description="Categoria para filme"
        )
        category_serie = Category(
            name="Série",
            description="Categoria para série"
        )

        repository = InMemoryCategoryRepository(categories=[
            category_filme,
            category_serie
        ])
        repository.save(category=category_filme)
        repository.save(category=category_serie)

        use_case = ListCategory(repository=repository)
        request = ListCategoryRequest()
        response = use_case.execute(request)

        assert response == ListCategoryResponse(data=[
            CategoryOutput(
                id=category_filme.id,
                name=category_filme.name,
                description=category_filme.description,
                is_active=category_filme.is_active
            ),
            CategoryOutput(
                id=category_serie.id,
                name=category_serie.name,
                description=category_serie.description,
                is_active=category_serie.is_active
            ),
        ])
