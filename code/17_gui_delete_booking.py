#Delete booking page
#The user can delete one of their bookings
def delete_booking_page(user):
    clear_window()

    #Page title
    tk.Label(window, text="Delete Booking", font=("Times New Roman", 16, "bold")).pack()

    #Booking ID input
    tk.Label(window, text="Booking ID").pack()
    booking_id_entry = tk.Entry(window, width=35)
    booking_id_entry.pack()

    #Message label
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Delete booking action
    def delete_booking_action():
        try:
            booking_id = int(booking_id_entry.get())

            #Search for the booking using booking ID and user email
            for booking in system.get_bookings():
                if booking.get_booking_id() == booking_id and booking.get_user().get_email() == user.get_email():

                    #Mark the booking as cancelled
                    booking.cancel_booking()

                    #Add the time slot back to the facility because it is free again
                    booking.get_facility().get_time_slots().append(booking.get_time_slot())

                    #Remove the booking from the system
                    system.get_bookings().remove(booking)

                    #Save the updated data
                    system.save_data()

                    #Show success message
                    result_label.config(text="Booking deleted.")
                    return

            #If booking was not found
            result_label.config(text="Booking not found.")

        #If booking ID is not a number
        except ValueError:
            result_label.config(text="Please enter a correct booking ID.")

    #Back to my bookings page
    def back_to_bookings():
        view_my_bookings(user)

    #Buttons
    tk.Button(window, text="Delete", width=25, command=delete_booking_action).pack()
    tk.Button(window, text="Back", width=25, command=back_to_bookings).pack()
