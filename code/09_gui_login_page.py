#Show login page
#This page allows users and admins to log in
def login_page():
    clear_window()

    #Page title
    tk.Label(window, text="Login", font=("Times New Roman", 16, "bold")).pack()

    #Email input
    tk.Label(window, text="Email").pack()
    email_entry = tk.Entry(window, width=35)
    email_entry.pack()

    #Password input
    #Show="*" hides the password while typing
    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, width=35, show="*")
    password_entry.pack()

    #This label shows messages like errors or success
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Check login details
    def login_action():
        email = email_entry.get()
        password = password_entry.get()

        #Make sure the user filled both fields
        if email == "" or password == "":
            result_label.config(text="Please enter email and password.")
            return

        #Check if the email and password match a saved user
        user = system.login_user(email, password)

        #If the user exists, open their dashboard
        if user:
            user_dashboard(user)

        #If not, show an error message
        else:
            result_label.config(text="Wrong email or password.")

    #Login button runs login_action
    tk.Button(window, text="Login", width=25, command=login_action).pack()

    #Back button returns to main menu
    tk.Button(window, text="Back", width=25, command=main_menu).pack()
