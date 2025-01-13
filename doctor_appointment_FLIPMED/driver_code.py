from repo import DoctorsRepo,  PatientsRepo, BookingRepo
from service import DoctorService, PatientService, BookingService
from entity import Specialization, BookingStatus

def main():
    doc_repo = DoctorsRepo()
    pat_repo = PatientsRepo()
    booking_repo = BookingRepo()

    doc_service = DoctorService(doc_repo)
    pat_service = PatientService(pat_repo)
    booking_service = BookingService(pat_repo, doc_repo, booking_repo)

    '''
i: registerPatient ->PatientA
i: bookAppointment: (PatientA, Dr.Curious, 12:00)
i:showAvailByspeciality: Cardiologist
i: cancelBookingId: 1234
i: showAvailByspeciality: Cardiologist
i: bookAppointment: (PatientB, Dr.Curious, 12:00)
i:registerDoc -> Daring-> Dermatologist
i: markDocAvail: Daring 11:00-12:00 14:00-15:00
i: showAvailByspeciality: Dermatologist
i: bookAppointment: (PatientF, Dr.Daring, 11:00)
i: bookAppointment: (PatientA, Dr.Curious, 12:00)
i: bookAppointment: (PatientF, Dr.Curious, 9:00)
i: bookAppointment: (PatientC, Dr.Curious, 16:00)
i: showAvailByspeciality: Cardiologist
i: bookAppointment: (PatientD, Dr.Curious, 16:00, waitlist=true)
i: cancelBookingId: 5701
i: showAppointmentsBooked(PatientF)
    '''
    doc_service.register_doc(1, 'Curious', Specialization.CARDIOLOGIST)
    doc_service.mark_avail(1, [('09:00', '10:30')])
    doc_service.mark_avail(1, [('09:00', '10:00'), ('12:00', '13:00'), ('16:00', '17:00')])
    doc_service.showAvailByspeciality(Specialization.CARDIOLOGIST)

    pat_service.register_patient(1, 'PatientA')
    booking_service.book_appointment(1, 1, '12:00')

    booking_service.cancel_booking(2)
    booking_service.book_appointment(1, 2, '12:00')

    booking_service.show_all_booking(1)


if __name__ == "__main__":
    main()