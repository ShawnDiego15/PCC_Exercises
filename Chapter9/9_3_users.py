# Exercise 9-3; Page 162; Users
#   Make a class called User
#   Create two attributes called first_name and last_name.
#   Create several other attributes that are typicall stored in a user profile.
#   Make a method called describe_user() that pritns a personalized greeting to the user.
#   Create several instances representing different users, and call both methods for each user.

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

    def describe_user(self):
        """Print a personalized greeting to a user."""
        print(f"Hi {self.first_name} {self.last_name}, you identify as {self.gender}.")
        print(f"You are originally from {self.hometown} but currently live in {self.current_location}.")
        print(f"You were born on {self.dob}. Nice to meet you!")

user_1 = User('Diego', 'Dominguez', 'Male', 'Rockport', 'Norman', '11/15/1996')

user_2 = User('Rachel', 'Cotten', 'Female', 'Flower Mound', 'Norman', '10/24/1996')

user_3 = User('Hunter', 'Bueno', 'Male', 'Rockport', 'Bastrop', '10/28/1996')

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()