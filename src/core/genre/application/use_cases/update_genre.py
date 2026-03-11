from dataclasses import dataclass
from uuid import UUID
from core.genre.application.exceptions import GenreNotFound, InvalidGenre, RelatedCategoriesNotFound
from core.genre.domain.genre_repository import GenreRepository
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from core.category.domain.category_repository import CategoryRepository


class UpdateGenre:
    def __init__(self, repository: GenreRepository, category_repository: CategoryRepository):
        self.repository = repository
        self.category_repository = category_repository

    @dataclass
    class Input:
        id: UUID
        name: str
        is_active: bool
        categories: set[UUID]

    @dataclass
    class Output:
        id: UUID

    def execute(self, input: Input) -> None:
        genre = self.repository.get_by_id(id=input.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {input.id} not found")

        category_ids = {
            category.id for category in self.category_repository.list()
        }
        if not input.categories.issubset(category_ids):
            raise RelatedCategoriesNotFound(
                f"Categories not found: {category_ids}"
            )

        try:
            if input.is_active is True:
                genre.activate()
            if input.is_active is False:
                genre.deactivate()
            genre.change_name(name=input.name)
            genre.update_categories(input.categories)
        except ValueError as err:
            raise InvalidGenre(str(err))

        self.repository.update(genre)
