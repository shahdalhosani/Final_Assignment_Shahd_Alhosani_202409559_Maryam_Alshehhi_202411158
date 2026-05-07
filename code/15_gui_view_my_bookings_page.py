#Show bookings for the logged-in user
def view_my_bookings(user):
    clear_window()

    #Page title
    tk.Label(window, text="My Bookings", font=("Times New Roman", 16, "bold")).pack()

    #Text box to display bookings
    text_box = tk.Text(window, width=75, height=16)
    text_box.pack()

    #This checks if the user has bookings or not
    found = False

    #Go through all bookings in the system
    for booking in system.get_bookings():

        #Show only the bookings that belong to this user
        if booking.get_user().get_email() == user.get_email():
            found = True
            text_box.insert(tk.END, "Booking ID: " + str(booking.get_booking_id()) + "\n")
            text_box.insert(tk.END, "Facility: " + booking.get_facility().get_name() + "\n")
            text_box.insert(tk.END, "Date: " + booking.get_date() + "\n")
            text_box.insert(tk.END, "Time: " + booking.get_time_slot() + "\n")
            text_box.insert(tk.END, "Cost: " + str(booking.get_total_cost()) + " AED\n")
            text_box.insert(tk.END, "Status: " + booking.get_status() + "\n")
            text_box.insert(tk.END, "------------------------------\n")

     #If the user has no bookings, show this message
    if not found:
        text_box.insert(tk.END, "You have no bookings yet.")

    #Open modify booking page
    def open_modify_booking():
        modify_booking_page(user)

    #Open delete booking page
    def open_delete_booking():
        delete_booking_page(user)

    #Back to dashboard
    def back_to_dashboard():
        user_dashboard(user)

    #Buttons for booking actions
    tk.Button(window, text="Modify Booking Date", width=30, command=open_modify_booking).pack()
    tk.Button(window, text="Delete Booking", width=30, command=open_delete_booking).pack()
    tk.Button(window, text="Back", width=30, command=back_to_dashboard).pack()
