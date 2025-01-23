# Exercise 9-11; Imported Admin; Page 180

# Start with your work from Exercise 9-8.
#   Store the classes User, Privileges, and Admin in one module.
#   Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

import users

admin_1 = users.Admin('Test', 'Admin', 'Male', 'Norman', "Rockport", '2024/12/31')

admin_1.privileges.show_privileges()