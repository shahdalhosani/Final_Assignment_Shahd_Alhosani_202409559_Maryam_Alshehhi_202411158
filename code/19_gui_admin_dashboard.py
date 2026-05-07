#Admin dashboard
def admin_dashboard(admin):
    clear_window()

    #Page title
    tk.Label(window, text="Admin Dashboard", font=("Times New Roman", 16, "bold")).pack()

    #Open all bookings page
    def open_all_bookings():
        view_all_bookings(admin)

    #Open all users page
    def open_all_users():
        view_all_users(admin)

    #Open upgrade user page
    def open_upgrade_user():
        admin_upgrade_user_page(admin)

    #Open update facility page
    def open_update_facility():
        admin_update_facility_page(admin)

    #Open facility usage page
    def open_usage():
        view_facility_usage(admin)

    #Back to normal user dashboard
    def back_to_dashboard():
        user_dashboard(admin)

    #Admin buttons
    tk.Button(window, text="View All Bookings", width=35, command=open_all_bookings).pack()
    tk.Button(window, text="View All Users", width=35, command=open_all_users).pack()
    tk.Button(window, text="Upgrade User Access", width=35, command=open_upgrade_user).pack()
    tk.Button(window, text="Update Facility Availability", width=35, command=open_update_facility).pack()
    tk.Button(window, text="View Facility Usage", width=35, command=open_usage).pack()
    tk.Button(window, text="Back", width=35, command=back_to_dashboard).pack()
