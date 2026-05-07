#This class controls the whole system
#It stores all users, facilities, and bookings in one place
class BookingSystem:
    #Create empty lists for users, facilities, and bookings
    def __init__(self):
        self.users = []
        self.facilities = []
        self.bookings = []

    #Getter and setter for users
    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    #Getter and setter for facilities
    def get_facilities(self):
        return self.facilities

    def set_facilities(self, facilities):
        self.facilities = facilities

    #Getter and setter for bookings
    def get_bookings(self):
        return self.bookings

    def set_bookings(self, bookings):
        self.bookings = bookings

    #Add user to the system
    def add_user(self, user):
        self.users.append(user)

    #Add facility to the system
    def add_facility(self, facility):
        self.facilities.append(facility)

    #Login user by checking email and password
    def login_user(self, email, password):
        for user in self.users:
            if user.login(email, password):
                return user

    #Make booking and return Booking if available
    def make_booking(self, booking):
        facility = booking.get_facility()
        time_slot = booking.get_time_slot()

        #If the time slot is available, the booking can continue
        if facility.check_availability(time_slot):
            booking.calculate_cost()
            booking.confirm_booking()
            facility.update_availability(time_slot)
            self.bookings.append(booking)
            return booking

    #Save data using pickle
    #This saves the whole system object into a file
    def save_data(self):
        with open("campus_booking_system.pkl", "wb") as file:
            pickle.dump(self, file)

    #Load data using pickle
    #This loads the old saved data if the file exists
    def load_data(self):
        try:
            with open("campus_booking_system.pkl", "rb") as file:
                saved_system = pickle.load(file)
                self.users = saved_system.users
                self.facilities = saved_system.facilities
                self.bookings = saved_system.bookings
        except FileNotFoundError:
            pass
