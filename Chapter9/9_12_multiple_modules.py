# Exercise 9-12; Multiple Modules; Page 180

# Store the User class in one module, and store the Privileges and Admin classes in a separate module.
#   In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

import admin

admin_1 = admin.Admin('Test', 'Admin', 'Male', 'Norman', "Rockport", '2024/12/31')

admin_1.privileges.show_privileges()