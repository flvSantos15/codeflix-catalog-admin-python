import pytest

from rest_framework.test import APIClient


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.mark.django_db
class TestCreateAndEditCategory:
    def test_user_can_create_and_edit_category(self, api_client: APIClient) -> None:
        # verifica que lista esta vazia
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

        # Edita categorua criada
        update_request = api_client.put(
            f"/api/categories/{created_category_id}/",
            data={
                "name": "Documentary",
                "description": "Documentary description",
                "is_active": False
            }
        )
        assert update_request.status_code == 204

        # Verifica que categoria editada aparece na listagem
        list_response = api_client.get("/api/categories/")
        assert list_response.data == {
            "data": [
                {
                    "id": created_category_id,
                    "name": "Documentary",
                    "description": "Documentary description",
                    "is_active": False
                }
            ]
        }
