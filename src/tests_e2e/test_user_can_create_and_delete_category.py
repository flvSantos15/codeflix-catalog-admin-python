import pytest

from rest_framework.test import APIClient


@pytest.mark.django_db
class TestCreateAndDeleteCategory:
    def test_user_can_create_and_delete_category(self) -> None:
        api_client = APIClient()

        # Verifica que a lista esta vazia
        list_response = api_client.get("/api/categories/")
        assert list_response.data == {"data": []}

        # Criar uma categoria
        create_response = api_client.post(
            "/api/categories/",
            data={
                "name": "Movie",
                "description": "Movie description"
            }
        )
        assert create_response.status_code == 201
        created_category_id = create_response.data["id"]

        # Verifica que categoria criada aparece na listagem
        list_response = api_client.get("/api/categories/")
        assert list_response.data == {
            "data": [
                {
                    "id": created_category_id,
                    "name": "Movie",
                    "description": "Movie description",
                    "is_active": True
                }
            ]
        }

        # Deleta a categoria
        delete_response = api_client.delete(
            f"/api/categories/{created_category_id}/"
        )
        assert delete_response.status_code == 204

        # Verifica que a categoria deletada não aparece na listagem
        list_response = api_client.get("api/categories")
        assert list_response.data == {"data": []}
