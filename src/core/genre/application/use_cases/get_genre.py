from dataclasses import dataclass
from uuid import UUID

from core.genre.application.exceptions import GenreNotFound
from core.genre.domain.genre_repository import GenreRepository


class GetGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Input:
        id: UUID

    @dataclass
    class Output:
        id: UUID
        name: str
        is_active: bool
        categories: set[UUID]

    def execute(self, request: Input) -> Output:
        genre = self.repository.get_by_id(id=request.id)

        if genre is None:
            raise GenreNotFound(f"Genere with {request.id} not found")

        return self.Output(
            id=genre.id,
            name=genre.name,
            is_active=genre.is_active,
            categories=genre.categories
        )
