from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category import InMemoryCategoryRepository


class TestSave:
    def test_can_save_category(self):
        repository = InMemoryCategoryRepository()
        category = Category(name='Clothes', description='Clothes description')
        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category


class TesteGetById:
    def test_can_get_category_by_id(self):
        repository = InMemoryCategoryRepository()

        category = Category(name='Movie', description='Movie category')
        repository.save(category)
        assert len(repository.categories) == 1
        assert repository.categories[0] == category

        category_id = category.id

        response = repository.get_by_id(category_id)
        assert response.id == category_id
        assert response.name == 'Movie'
        assert response.description == 'Movie category'
        assert response.is_active == True


class TestDelete:
    def test_can_delete_category(self):
        repository = InMemoryCategoryRepository()

        category = Category(name='Movie', description='Movie category')
        repository.save(category)
        assert len(repository.categories) == 1
        assert repository.categories[0] == category

        category_id = category.id

        repository.delete(category_id)
        assert len(repository.categories) == 0
