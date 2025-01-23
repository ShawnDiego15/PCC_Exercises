# Exercise 9-12; Separating the users module.

# adding an import since the Admin class relies on the parent, user.

from user import User

class Privileges:
    """A model representing privileges of accounts."""

    def __init__(self):
        self.privileges = ['can add posts', 'can delete posts', 'can edit posts', 'can reset user login']

    def show_privileges(self):
        """Show privileges available to admin users."""
        print(f"{self.privileges}")

class Admin(User):
    """An attempt to represent an Administrator user."""

    def __init__(self, first_name, last_name, gender, hometown, current_location, dob):
        """Initalize an instance of an Admin"""
        super().__init__(first_name, last_name, gender, hometown, current_location, dob)
        self.privileges = Privileges()