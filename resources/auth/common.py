from resources.user.models.user import User
from resources.constants import PHI_FIELDS


def get_current_user():
    # Mock user
    return User(id=1, name="My User", is_admin=True)
