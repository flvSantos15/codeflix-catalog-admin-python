from dataclasses import dataclass
from uuid import UUID
from core.category.domain.category_repository import CategoryRepository
from core.genre.application.exceptions import GenreNotFound, InvalidGenre, RelatedCategoriesNotFound
from core.genre.domain.genre_repository import GenreRepository


class RemoveCategoriesFromGenre:
    def __init__(self, repository: GenreRepository, category_repository: CategoryRepository):
        self.repository = repository
        self.category_repository = category_repository

    @dataclass
    class Input:
        id: UUID
        categories: set[UUID]

    @dataclass
    class Output:
        id: UUID

    def execute(self, request: Input) -> None:
        genre = self.repository.get_by_id(id=request.id)

        if genre is None:
            raise GenreNotFound(f"Genre with {request.id} not found")

        current_categories = request.categories

        try:
            if request.categories is not None:
                category_ids = {
                    category.id for category in self.category_repository.list()
                }
                if not request.categories.issubset(category_ids):
                    raise RelatedCategoriesNotFound(
                        f"Categories not found: {category_ids}"
                    )

                for category_id in current_categories:
                    genre.remove_category(category_id=category_id)

        except ValueError as err:
            raise InvalidGenre(str(err))

        self.repository.update(genre)
        return self.Output(id=genre.id)
