from entity import Doctor, Patient, Booking, Slot, BookingStatus
from datetime import datetime

class DoctorService:
    def __init__(self, doc_repo):
        self.doc_repo = doc_repo

    def register_doc(self, id, name, specaialization):
        doctor = Doctor(id, name, specaialization)
        self.doc_repo.add(doctor)
        print(f'Welcome, Dr. {name}!')

    def mark_avail(self, doc_id, time_slots):
        doc = self.doc_repo.get(doc_id)

        for st_time, end_time in time_slots:
            st_time = datetime.strptime(st_time,  '%H:%M')
            end_time = datetime.strptime(end_time,  '%H:%M')
            time_diff = end_time-st_time
            if time_diff.seconds != 3600:
                print(f'Sorry Dr. {doc.name} slots are 60 mins only')
                continue

            slot = Slot(st_time, end_time)
            doc.avl_slots.add(slot)
            print(f'Dr. {doc.name}, slot added from {st_time.time()} to {end_time.time()}')

        print('Done! Doc.')

    def showAvailByspeciality(self, specaialization):
        for doc in self.doc_repo.get_all_doctors():
            if doc.specialization == specaialization:
                for slot in doc.avl_slots:
                    print(f'{doc.id}, Dr. {doc.name} ({slot.start_time} - {slot.end_time})')

class PatientService:
    def __init__(self, patients_repo):
        self.patients_repo = patients_repo

    def register_patient(self, id, name):
        patient = Patient(id, name)
        self.patients_repo.add(patient)

class BookingService:
    def __init__(self, patient_repo, doc_repo, booking_repo):
        self.patient_repo = patient_repo
        self.doc_repo = doc_repo
        self.booking_repo = booking_repo
        self.curr_bid = 1
    
    def _get_bid(self):
        self.curr_bid += 1
        return self.curr_bid

    def book_appointment(self, doc_id, patient_id, time):
        doctor = self.doc_repo.get(doc_id)

        # check of slot is available
        booking = None
        time = datetime.strptime(time, '%H:%M')
        for slot in doctor.avl_slots:
            if slot.start_time == time:
                bid = self._get_bid()
                booking = Booking(bid, doc_id, patient_id, slot, 'PENDING')
                break

        if booking is not None:
            self.booking_repo.add(booking)
            doctor.avl_slots.remove(booking.slot)
            print(f'Booking Confirmed!, Booking id: {bid}')
        else:
            print('Slot not available')     

    def cancel_booking(self, booking_id):
        booking = self.booking_repo.get(booking_id)
        booking.booking_status = BookingStatus.CANCELLED
        doc = self.doc_repo.get(booking.doctor_id)
        doc.avl_slots.add(booking.slot)
        print('Booking Cancelled!')

    def show_all_booking(self, patient_id):
        for booking in self.booking_repo.get_all_bookings():
            if booking.patient_id == patient_id:
                print(f'{booking.id}, Dr. {booking.doctor_id}, {booking.slot.start_time} - {booking.slot.end_time}')

