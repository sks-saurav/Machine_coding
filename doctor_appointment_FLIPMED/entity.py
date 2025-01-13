from abc import ABC
from enum import Enum

class Specialization(Enum):
    CARDIOLOGIST = 1
    DERMATOLOGIST = 2
    GENERAL_PHYSICIAN = 3
    GYNECOLOGIST = 4
    NEUROLOGIST = 5
    ORTHOPEDIC = 6
    PEDIATRICIAN = 7
    PSYCHIATRIST = 8
    UROLOGIST = 9

class BookingStatus(Enum):
    PENDING = 1
    BOOKED = 3
    CANCELLED = 4

class User(ABC):
    def __init__(self, id, name=None):
        self.id = id
        self.name = name

class Doctor(User):
    def __init__(self, id, name, specialization):
        super().__init__(id, name)
        self.specialization = specialization
        self.avl_slots = set()

class Patient(User):
    def __init__(self, id, name):
        super().__init__(id, name)

class Slot:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f'{self.start_time} - {self.end_time}'

class Booking:
    def __init__(self, id, doctor_id, patient_id, slot, booking_status):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.slot = slot
        self.booking_status = booking_status

