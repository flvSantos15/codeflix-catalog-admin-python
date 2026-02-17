from uuid import UUID
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from core.category.application.use_cases.create_category import CreateCategory, CreateCategoryRequest
from core.category.application.use_cases.delete_category import DeleteCategory, DeleteCategoryRequest
from core.genre.application.use_cases.list_genre import ListGenre
from django_project.genre_app.repository import DjangoORMGenreRepository
from django_project.genre_app.serializers import ListGenreOutputSerializer
from src.core.category.application.use_cases.exceptions import CategoryNotFound
from core.category.application.use_cases.get_category import GetCategory, GetCategoryRequest
from core.category.application.use_cases.list_category import ListCategory, ListCategoryRequest
from core.category.application.use_cases.update_category import UpdateCategory, UpdateCategoryRequest
from src.django_project.category_app.repository import DjangoORMCategoryRepository
from src.django_project.category_app.serializers import CreateCategoryRequestSerializer, CreateCategoryResponseSerializer, DeleteCategoryRequestSerializer, ListCategoryResponseSerializer, RetrieveCategoryRequestSerializer, RetrieveCategoryResponseSerializer, UpdateCategoryRequestSerializer


class GenreViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        use_case = ListGenre(repository=DjangoORMGenreRepository())
        output: ListGenre.Output = use_case.execute(input=ListGenre.Input())

        serializer = ListGenreOutputSerializer(output)

        return Response(
            status=HTTP_200_OK,
            data=serializer.data
        )

    # def retrieve(self, request: Request, pk=None):
    #     serializer = RetrieveCategoryRequestSerializer(data={"id": pk})
    #     serializer.is_valid(raise_exception=True)

    #     use_case = GetCategory(repository=DjangoORMCategoryRepository())

    #     try:
    #         result = use_case.execute(
    #             request=GetCategoryRequest(
    #                 id=serializer.validated_data["id"]
    #             )
    #         )
    #     except CategoryNotFound:
    #         return Response(status=HTTP_404_NOT_FOUND)

    #     category_output = RetrieveCategoryResponseSerializer(result)

    #     return Response(
    #         status=HTTP_200_OK,
    #         data=category_output.data
    #     )

    # def create(self, request: Request) -> Response:
    #     serializer = CreateCategoryRequestSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     input = CreateCategoryRequest(**serializer.validated_data)
    #     use_case = CreateCategory(repository=DjangoORMCategoryRepository())
    #     output = use_case.execute(request=input)

    #     return Response(
    #         status=HTTP_201_CREATED,
    #         data=CreateCategoryResponseSerializer(instance=output).data
    #     )

    # def update(self, request: Request, pk: UUID = None) -> Response:
    #     serializer = UpdateCategoryRequestSerializer(
    #         data={
    #             **request.data,
    #             "id": pk
    #         }
    #     )
    #     serializer.is_valid(raise_exception=True)

    #     input = UpdateCategoryRequest(**serializer.validated_data)
    #     use_case = UpdateCategory(repository=DjangoORMCategoryRepository())

    #     try:
    #         use_case.execute(request=input)
    #     except CategoryNotFound:
    #         return Response(status=HTTP_404_NOT_FOUND)

    #     return Response(status=HTTP_204_NO_CONTENT)

    # def destroy(self, request: Request, pk=None) -> Response:
    #     serializer = DeleteCategoryRequestSerializer(data={"id": pk})
    #     serializer.is_valid(raise_exception=True)

    #     input = DeleteCategoryRequest(**serializer.validated_data)
    #     use_case = DeleteCategory(repository=DjangoORMCategoryRepository())

    #     try:
    #         use_case.execute(request=input)
    #     except CategoryNotFound:
    #         return Response(status=HTTP_404_NOT_FOUND)

    #     return Response(status=HTTP_204_NO_CONTENT)

    # def partial_update(self, request, pk: UUID = None) -> Response:
    #     serializer = UpdateCategoryRequestSerializer(data={
    #         **request.data,
    #         "id": pk,
    #     }, partial=True)
    #     serializer.is_valid(raise_exception=True)

    #     input = UpdateCategoryRequest(**serializer.validated_data)
    #     use_case = UpdateCategory(repository=DjangoORMCategoryRepository())

    #     try:
    #         use_case.execute(request=input)
    #     except CategoryNotFound:
    #         return Response(status=HTTP_404_NOT_FOUND)

    #     return Response(status=HTTP_204_NO_CONTENT)
