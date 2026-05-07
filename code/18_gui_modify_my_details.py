#Modify user details page
#This allows the user to update their name and email
def modify_user_details_page(user):
    clear_window()

    #Page title
    tk.Label(window, text="Modify My Details", font=("Times New Roman", 16, "bold")).pack()

    #New name input
    tk.Label(window, text="New Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack()

    #New email input
    tk.Label(window, text="New Email").pack()
    email_entry = tk.Entry(window, width=35)
    email_entry.pack()

    #Message label
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Save the new user details
    def save_details():
        new_name = name_entry.get()
        new_email = email_entry.get()

        #Make sure both fields are filled
        if new_name == "" or new_email == "":
            result_label.config(text="Please fill all fields.")
            return

        #Update user name and email
        user.set_name(new_name)
        user.set_email(new_email)

        #Save changes
        system.save_data()

        #Show success message
        result_label.config(text="User details updated.")

    #Back to dashboard
    def back_to_dashboard():
        user_dashboard(user)

    #Buttons
    tk.Button(window, text="Save", width=25, command=save_details).pack()
    tk.Button(window, text="Back", width=25, command=back_to_dashboard).pack()

#Delete user account
#This removes the current user from the users list
def delete_user_account(user):
    system.get_users().remove(user)
    system.save_data()
    main_menu()

#Upgrade user access
#This upgrades the current user to Premium
def upgrade_current_user(user):
    user.upgrade_access()
    system.save_data()
    user_dashboard(user)
