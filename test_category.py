import pytest
import uuid

from category import Category

class TestCategory:
  def test_name_is_required(self):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
      Category()

  def test_name_must_have_less_than_255_characters(self):
    with pytest.raises(TypeError, match="name must have less than 256 characters"):
      Category(name="a" * 256)

  def test_category_must_be_created_with_id_as_uuid_by_default(self):
    category = Category(name="horror")
    assert isinstance(category.id, uuid.UUID)

  def test_created_category_with_default_values(self):
    category = Category("action")
    assert category.name == "action"
    assert category.description == ""
    assert category.is_active is True

  def test_category_is_created_as_active_by_default(self):
    category = Category("name")
    assert category.is_active is True

  def test_category_is_created_as_inactive(self):
    category = Category("name", is_active=False)
    assert category.is_active is False

  def test_category_is_created_with_provided_values(self):
    cat_id = uuid.uuid4()
    category = Category(id=cat_id, name="documentary", description="description", is_active=False)
    assert category.id == cat_id
    assert category.name == "documentary"
    assert category.description == "description"
    assert category.is_active is False

  def test_category_str_method(self):
    cat_id = uuid.uuid4()
    category = Category(id=cat_id, name="documentary", description="description", is_active=False)
    assert str(category) == "documentary - description - (False)"

  def test_category_repr_method(self):
    cat_id = uuid.uuid4()
    category = Category(id=cat_id, name="documentary", description="description", is_active=False)
    assert repr(category) == "documentary - description - (False)"
