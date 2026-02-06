from dataclasses import dataclass
from uuid import UUID

from core.genre.application.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository


class DeleteGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Input:
        id: UUID

    def execute(self, input: Input) -> None:
        category = self.repository.get_by_id(id=input.id)

        if category is None:
            raise GenreNotFound(f"Genre with {input.id} not found")

        self.repository.delete(category.id)
