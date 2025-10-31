import pytest
import uuid

from category import Category

class TestCategory:
  def test_name_is_required(self):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
      Category()

  def test_name_must_have_less_than_255_characters(self):
    with pytest.raises(ValueError, match="name cannot be longer than 255"):
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

  def test_cannot_create_category_with_empty_name(self):
    with pytest.raises(ValueError, match="name cannot be empty"):
      Category(name="")

  def test_category_str_method(self):
    cat_id = uuid.uuid4()
    category = Category(id=cat_id, name="documentary", description="description", is_active=False)
    assert str(category) == "documentary - description - (False)"

  def test_category_repr_method(self):
    cat_id = uuid.uuid4()
    category = Category(id=cat_id, name="documentary", description="description", is_active=False)
    assert repr(category) == "documentary - description - (False)"

class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
      category = Category(name="Filme", description="Descrição")

      category.update_category(name="Série", description="Descrição atualizada")

      assert category.name == "Série"
      assert category.description == "Descrição atualizada"

    def test_update_category_with_invalid_name_raises_expection(self):
      category = Category(name="Filme", description="Descrição")

      with pytest.raises(ValueError, match="name cannot be longer than 255"):
        category.update_category(name="a" * 256, description="Descrição atualizada")

    def test_cannot_update_category_with_empty_name(self):
      category = Category(name="Filme", description="Descrição")

      with pytest.raises(ValueError, match="name cannot be empty"):
        category.update_category(name="", description="Descrição atualizada")

class TestActivateCategory:
    def test_activate_inactive_category(self):
      category = Category(name="Filme", description="Descrição", is_active=False)

      category.activate()

      assert category.is_active is True

    def test_activate_active_category(self):
      category = Category(name="Filme", description="Descrição", is_active=True)

      category.activate()

      assert category.is_active is True

class TestDeactivateCategory:
    def test_deactivate_active_category(self):
      category = Category(name="Filme", description="Descrição", is_active=True)

      category.deactivate()

      assert category.is_active is False

    def test_activate_inactive_category(self):
      category = Category(name="Filme", description="Descrição", is_active=False)

      category.deactivate()

      assert category.is_active is False


class TestEquality:
    def test_when_categories_have_same_id_they_are_equal(self):
      common_id = uuid.uuid4()
      category_1 = Category(id=common_id, name="Filme", description="Descrição", is_active=True)
      category_2 = Category(id=common_id, name="Filme", description="Descrição", is_active=True)

      assert category_1 == category_2

    def test_when_categories_have_different_id_they_are_not_equal(self):
      class Dymmy:
        pass
      
      common_id = uuid.uuid4()
      category = Category(id=uuid.uuid4(), name="Filme")
      dummy = Dymmy()
      dummy.id = common_id

      assert category != dummy
