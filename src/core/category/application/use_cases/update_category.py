from abc import abstractmethod
from uuid import UUID
from core.category.application.category_repository import CategoryRepository


@abstractmethod
class UpdateCategoryRequest:
    id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class UpdateCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: UpdateCategoryRequest) -> None:
        category = self.respository.get_by_id(request)

        current_name = category.name
        current_description = category.description

        if request.name is not None:
            current_name = request.name

        if request.description is not None:
            current_description = request.description

        if request.is_active is True:
            category.activate()

        if request.is_active is False:
            category.deactivate()

        category.update_category(
            name=current_name,
            description=current_description
        )

        self.repository.update(category)
