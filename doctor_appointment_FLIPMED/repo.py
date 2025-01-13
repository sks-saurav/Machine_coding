class DoctorsRepo:
    def __init__(self):
        self.doctors = {}
    
    def get(self, doc_id):
        return self.doctors.get(doc_id)
    
    def get_all_doctors(self):
        return self.doctors.values()
    
    def add(self, doctor):
        self.doctors[doctor.id] = doctor

class PatientsRepo:
    def __init__(self):
        self.patients = {}

    def get(self, patient_id):
        return self.patients.get(patient_id)
    
    def add(self, patient):
        self.patients[patient.id] = patient

class BookingRepo:
    def __init__(self):
        self.bookings = {}

    def add(self, booking):
        self.bookings[booking.id] = booking

    def get(self, booking_id):
        return self.bookings.get(booking_id)
    
    def get_all_bookings(self):
        return self.bookings.values()