#Admin updates facility page
#Admin can add a new available time slot to a facility
def admin_update_facility_page(admin):
    clear_window()

    #Page title
    tk.Label(window, text="Update Facility", font=("Times New Roman", 16, "bold")).pack()

    #Facility ID input
    tk.Label(window, text="Facility ID").pack()
    facility_id_entry = tk.Entry(window, width=35)
    facility_id_entry.pack()

    #New time slot input
    tk.Label(window, text="New Time Slot").pack()
    new_slot_entry = tk.Entry(window, width=35)
    new_slot_entry.pack()

    #Message label
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Update facility action
    def update_facility_action():
        try:
            facility_id = int(facility_id_entry.get())
            new_slot = new_slot_entry.get()

            #Make sure the new time slot is entered
            if new_slot == "":
                result_label.config(text="Please enter new time slot.")
                return

            #Find the facility by ID
            facility = find_facility(facility_id)

            #If facility exists, add the new slot
            if facility:
                slots = facility.get_time_slots()
                slots.append(new_slot)
                admin.update_facility(facility, slots)
                system.save_data()
                result_label.config(text="Facility availability updated.")

            #If facility does not exist
            else:
                result_label.config(text="Facility not found.")
         #If facility ID is not a number
        except ValueError:
            result_label.config(text="Please enter a correct facility ID.")

    #Back to admin dashboard
    def back_to_admin():
        admin_dashboard(admin)

    #Buttons
    tk.Button(window, text="Update", width=25, command=update_facility_action).pack()
    tk.Button(window, text="Back", width=25, command=back_to_admin).pack()
