# Exercise 9-8; Page 173; Privileges

# Write a seperate Privileges class.
#   The class should have one attribute, privileges, that stores a list of strings as described in exercise 9-7.
#   Move the show_privileges() method to this class.
#   Make a Privileges instance as an attribute in the Admin class.
#   Create a new instance of Admin and user your method to show its privileges.

# An extra exercise can be to allow user to input role upon user creation and set privileges based on role.

class User:
    """A simple model reflecting attributes of a user."""

    def __init__(self, first_name, last_name, gender, hometown, current_location, dob):
        """Initialize attributes of a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.hometown = hometown
        self.current_location = current_location
        self.dob = dob
        self.login_attempts = 0

    def describe_user(self):
        """Print a personalized greeting to a user."""
        print(f"Hi {self.first_name} {self.last_name}, you identify as {self.gender}.")
        print(f"You are originally from {self.hometown} but currently live in {self.current_location}.")
        print(f"You were born on {self.dob}. Nice to meet you!")

    def increment_login_attempts(self):
        """
            Increase the value of login_attempts by 1.
            If the user reaches 5 login attempts, lock their account.    
        """
        if self.login_attempts >= 5:
            print("Your account has been locked due to exceeding 5 login attempts. Please contact an admin.")
        else:
            self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts back to 0."""
        self.login_attempts = 0

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

admin_1 = Admin("Diego", "Dominguez", "Male", "Rockport", "Norman", "11/15/1996")

admin_1.privileges.show_privileges()