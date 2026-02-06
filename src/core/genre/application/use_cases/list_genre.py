from dataclasses import dataclass
from uuid import UUID
from core.genre.domain.genre_repository import GenreRepository


@dataclass
class GenreOutput:
    id: UUID
    name: str
    is_active: bool
    categories: set[UUID]


class ListGenre:
    def __init__(self, repository: GenreRepository):
        self.repository = repository

    @dataclass
    class Input:
        pass

    @dataclass
    class Output:
        data: list[GenreOutput]

    def execute(self, input: Input):
        genres = self.repository.list()

        mapped_genres = [
            GenreOutput(
                id=genre.id,
                name=genre.name,
                is_active=genre.is_active,
                categories=genre.categories
            ) for genre in genres
        ]

        return self.Output(data=mapped_genres)
