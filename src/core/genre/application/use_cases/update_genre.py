from dataclasses import dataclass
from uuid import UUID
from core.genre.application.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from core.category.domain.category_repository import CategoryRepository


class UpdateGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Input:
        id: UUID
        name: str | None = None
        is_active: bool | None = None
        categories: set[UUID] | None = None

    def execute(self, request: Input) -> None:
        genre = self.repository.get_by_id(id=request.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {request.id} not found")

        current_name = genre.name
        current_categories = genre.categories

        if request.name is not None:
            current_name = request.name

        if request.categories is not None:
            for category_id in current_categories:
                genre.remove_category(category_id=category_id)
            for category_id in request.categories:
                genre.add_category(category_id=category_id)

        if request.is_active is True:
            genre.activate()

        if request.is_active is False:
            genre.deactivate()

        genre.change_name(
            name=current_name,
        )

        self.repository.update(genre)
