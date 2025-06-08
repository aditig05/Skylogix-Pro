from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .base import Base

class EmployeeRole(enum.Enum):
    PILOT = "pilot"
    FLIGHT_ATTENDANT = "flight_attendant"
    GROUND_STAFF = "ground_staff"
    ADMINISTRATIVE = "administrative"

class FlightStatus(enum.Enum):
    SCHEDULED = "scheduled"
    DELAYED = "delayed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(3), unique=True, index=True)
    name = Column(String(100))
    city = Column(String(100))
    country = Column(String(100))
    timezone = Column(String(50))

    # Relationships
    departure_flights = relationship("Flight", foreign_keys="Flight.departure_airport_id", back_populates="departure_airport")
    arrival_flights = relationship("Flight", foreign_keys="Flight.arrival_airport_id", back_populates="arrival_airport")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(10), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    role = Column(Enum(EmployeeRole))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    hire_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)

    # Relationships
    flight_assignments = relationship("FlightAssignment", back_populates="employee")

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String(10), unique=True, index=True)
    departure_airport_id = Column(Integer, ForeignKey("airports.id"))
    arrival_airport_id = Column(Integer, ForeignKey("airports.id"))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    aircraft_type = Column(String(50))
    status = Column(Enum(FlightStatus), default=FlightStatus.SCHEDULED)
    base_price = Column(Float)

    # Relationships
    departure_airport = relationship("Airport", foreign_keys=[departure_airport_id], back_populates="departure_flights")
    arrival_airport = relationship("Airport", foreign_keys=[arrival_airport_id], back_populates="arrival_flights")
    assignments = relationship("FlightAssignment", back_populates="flight")
    bookings = relationship("Booking", back_populates="flight")

class FlightAssignment(Base):
    __tablename__ = "flight_assignments"

    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey("flights.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    assignment_date = Column(DateTime, default=datetime.utcnow)

    # Relationships
    flight = relationship("Flight", back_populates="assignments")
    employee = relationship("Employee", back_populates="flight_assignments")

class Passenger(Base):
    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)
    passport_number = Column(String(20), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    loyalty_points = Column(Integer, default=0)

    # Relationships
    bookings = relationship("Booking", back_populates="passenger")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    booking_reference = Column(String(10), unique=True, index=True)
    flight_id = Column(Integer, ForeignKey("flights.id"))
    passenger_id = Column(Integer, ForeignKey("passengers.id"))
    booking_date = Column(DateTime, default=datetime.utcnow)
    seat_number = Column(String(10))
    meal_preference = Column(String(50))
    total_price = Column(Float)

    # Relationships
    flight = relationship("Flight", back_populates="bookings")
    passenger = relationship("Passenger", back_populates="bookings")

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(200))
    category = Column(String(50))  # e.g., vegetarian, non-vegetarian, special
    price = Column(Float)
    is_available = Column(Boolean, default=True)

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(200))
    price = Column(Float)
    is_available = Column(Boolean, default=True) 