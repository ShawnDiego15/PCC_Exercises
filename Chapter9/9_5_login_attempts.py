# Exercise 9-5; Page 167; Login Attempts
#   Add an attribute called login_attempts to the User class from Exercise 9-1.
#   Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
#   Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

#   Make an instance of the User class and call increment_login_attempts() several times.
#   Print the value of login_attempts to make sure it was incremented properly and then call reset_login_attempts().
#   Print login_attempts again to make sure it was reset to 0.

#   As a self-added exercise, disable the users account upon reaching 5 login attempts.

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

user1 = User('Diego', 'Dominguez', 'Male', 'Rockport', 'Norman', '11/15/1996')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)

print("Ensure the user's account locks upon reaching 5 or more login attempts.")
user1.increment_login_attempts() 

print("Reset the users login attempts.")
user1.reset_login_attempts()
print(user1.login_attempts)