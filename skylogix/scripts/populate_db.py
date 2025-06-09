from ..models.base import SessionLocal, Base, engine
from ..models.models import Airport, Employee, Flight, Passenger, Booking, Meal, Service
from datetime import datetime, timedelta
import random

def clear_database():
    """Clear all existing data from the database"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def populate_airports():
    """Add sample airports"""
    airports = [
        Airport(code="JFK", name="John F. Kennedy International", city="New York", country="USA", timezone="America/New_York"),
        Airport(code="LAX", name="Los Angeles International", city="Los Angeles", country="USA", timezone="America/Los_Angeles"),
        Airport(code="LHR", name="Heathrow Airport", city="London", country="UK", timezone="Europe/London"),
        Airport(code="CDG", name="Charles de Gaulle Airport", city="Paris", country="France", timezone="Europe/Paris"),
        Airport(code="DXB", name="Dubai International", city="Dubai", country="UAE", timezone="Asia/Dubai"),
        Airport(code="SIN", name="Changi Airport", city="Singapore", country="Singapore", timezone="Asia/Singapore"),
        Airport(code="HKG", name="Hong Kong International", city="Hong Kong", country="China", timezone="Asia/Hong_Kong"),
        Airport(code="SYD", name="Sydney Airport", city="Sydney", country="Australia", timezone="Australia/Sydney")
    ]
    return airports

def populate_employees():
    """Add sample employees"""
    employees = [
        Employee(employee_id="PIL001", first_name="John", last_name="Smith", role="PILOT", email="john.smith@skylogix.com", phone="+1-555-0101"),
        Employee(employee_id="PIL002", first_name="Sarah", last_name="Johnson", role="PILOT", email="sarah.j@skylogix.com", phone="+1-555-0102"),
        Employee(employee_id="FA001", first_name="Emma", last_name="Davis", role="FLIGHT_ATTENDANT", email="emma.d@skylogix.com", phone="+1-555-0103"),
        Employee(employee_id="FA002", first_name="Michael", last_name="Brown", role="FLIGHT_ATTENDANT", email="michael.b@skylogix.com", phone="+1-555-0104"),
        Employee(employee_id="MECH001", first_name="David", last_name="Wilson", role="GROUND_STAFF", email="david.w@skylogix.com", phone="+1-555-0105"),
        Employee(employee_id="MECH002", first_name="Lisa", last_name="Anderson", role="GROUND_STAFF", email="lisa.a@skylogix.com", phone="+1-555-0106"),
        Employee(employee_id="ADMIN001", first_name="Robert", last_name="Taylor", role="ADMINISTRATIVE", email="robert.t@skylogix.com", phone="+1-555-0107"),
        Employee(employee_id="ADMIN002", first_name="Jennifer", last_name="Martinez", role="ADMINISTRATIVE", email="jennifer.m@skylogix.com", phone="+1-555-0108")
    ]
    return employees

def populate_flights(airports):
    """Add sample flights"""
    flights = []
    aircraft_types = ["Boeing 737", "Boeing 777", "Airbus A320", "Airbus A350"]
    
    # Create more sample routes
    routes = [
        (airports[0], airports[1]),  # JFK-LAX
        (airports[0], airports[2]),  # JFK-LHR
        (airports[1], airports[3]),  # LAX-CDG
        (airports[2], airports[4]),  # LHR-DXB
        (airports[3], airports[5]),  # CDG-SIN
        (airports[4], airports[6]),  # DXB-HKG
        (airports[5], airports[7]),  # SIN-SYD
        (airports[6], airports[0]),  # HKG-JFK
        (airports[0], airports[3]),  # JFK-CDG
        (airports[1], airports[4]),  # LAX-DXB
        (airports[2], airports[5]),  # LHR-SIN
        (airports[3], airports[6]),  # CDG-HKG
        (airports[4], airports[7]),  # DXB-SYD
        (airports[5], airports[0]),  # SIN-JFK
        (airports[6], airports[1])   # HKG-LAX
    ]
    
    for i, (dep, arr) in enumerate(routes, 1):
        # Create daily flights for each route for 14 days
        for day in range(14):  # Increased from 7 to 14 days
            departure_time = datetime.now() + timedelta(days=day, hours=random.randint(6, 20))
            flight_time = timedelta(hours=random.randint(2, 12))
            arrival_time = departure_time + flight_time
            
            flight = Flight(
                flight_number=f"SK{i:03d}-{day+1}",
                departure_airport_id=dep.id,
                arrival_airport_id=arr.id,
                departure_time=departure_time,
                arrival_time=arrival_time,
                aircraft_type=random.choice(aircraft_types),
                base_price=random.randint(300, 1500)
            )
            flights.append(flight)
    
    return flights

def populate_passengers():
    """Add sample passengers"""
    passengers = [
        Passenger(passport_number="US123456", first_name="Alice", last_name="Cooper", email="alice.c@email.com", phone="+1-555-0201"),
        Passenger(passport_number="UK789012", first_name="Bob", last_name="Wilson", email="bob.w@email.com", phone="+44-555-0202"),
        Passenger(passport_number="FR345678", first_name="Claire", last_name="Dubois", email="claire.d@email.com", phone="+33-555-0203"),
        Passenger(passport_number="AE901234", first_name="Mohammed", last_name="Al-Farsi", email="m.al-farsi@email.com", phone="+971-555-0204"),
        Passenger(passport_number="SG567890", first_name="Wei", last_name="Chen", email="wei.c@email.com", phone="+65-555-0205"),
        Passenger(passport_number="HK123789", first_name="Yuki", last_name="Tanaka", email="y.tanaka@email.com", phone="+852-555-0206"),
        Passenger(passport_number="AU456123", first_name="James", last_name="Thompson", email="j.thompson@email.com", phone="+61-555-0207"),
        Passenger(passport_number="CA789456", first_name="Maria", last_name="Garcia", email="m.garcia@email.com", phone="+1-555-0208")
    ]
    return passengers

def populate_meals():
    """Add sample meals"""
    meals = [
        Meal(name="Vegetarian Pasta", description="Fresh pasta with seasonal vegetables", category="Vegetarian", price=15.00),
        Meal(name="Chicken Curry", description="Spiced chicken curry with rice", category="Non-Vegetarian", price=18.00),
        Meal(name="Salmon Fillet", description="Grilled salmon with steamed vegetables", category="Non-Vegetarian", price=20.00),
        Meal(name="Vegan Buddha Bowl", description="Quinoa bowl with roasted vegetables", category="Vegan", price=16.00),
        Meal(name="Beef Steak", description="Grilled beef steak with mashed potatoes", category="Non-Vegetarian", price=25.00),
        Meal(name="Mediterranean Salad", description="Fresh salad with feta cheese", category="Vegetarian", price=14.00)
    ]
    return meals

def populate_services():
    """Add sample services"""
    services = [
        Service(name="Priority Boarding", description="Early boarding access", price=25.00),
        Service(name="Extra Baggage", description="Additional 10kg baggage allowance", price=50.00),
        Service(name="Airport Transfer", description="Luxury car transfer to/from airport", price=75.00),
        Service(name="Lounge Access", description="Access to airport lounges", price=40.00),
        Service(name="Seat Selection", description="Choose your preferred seat", price=15.00),
        Service(name="Travel Insurance", description="Comprehensive travel insurance", price=30.00)
    ]
    return services

def populate_bookings(flights, passengers):
    """Add sample bookings"""
    bookings = []
    seat_numbers = [f"{row}{col}" for row in range(1, 31) for col in "ABCDEF"]
    
    # Ensure we have valid flights and passengers
    if not flights or not passengers:
        print("Warning: No flights or passengers available for bookings")
        return bookings
    
    for flight in flights:
        # Create 3-8 random bookings for each flight (increased from 2-5)
        num_bookings = random.randint(3, 8)
        for _ in range(num_bookings):
            passenger = random.choice(passengers)
            seat = random.choice(seat_numbers)
            meal = random.choice(["Vegetarian", "Non-Vegetarian", "Vegan"])
            total_price = flight.base_price + random.randint(50, 200)  # Add some random additional charges
            
            booking = Booking(
                booking_reference=f"BK{random.randint(100000, 999999)}",
                flight_id=flight.id,
                passenger_id=passenger.id,
                seat_number=seat,
                meal_preference=meal,
                total_price=total_price,
                booking_date=datetime.now()
            )
            booking.flight = flight
            booking.passenger = passenger
            bookings.append(booking)
    
    return bookings

def populate_employee_info(employees):
    """Add additional employee information"""
    for employee in employees:
        employee.hire_date = datetime.now() - timedelta(days=random.randint(30, 365))
        employee.salary = random.randint(50000, 120000)
        employee.department = random.choice(["Operations", "Maintenance", "Customer Service", "Administration"])
    return employees

def update_existing_employee_roles():
    """Update existing employee roles to match enum values"""
    db = SessionLocal()
    try:
        employees = db.query(Employee).all()
        for employee in employees:
            if employee.role == "Pilot":
                employee.role = "PILOT"
            elif employee.role == "Flight Attendant":
                employee.role = "FLIGHT_ATTENDANT"
            elif employee.role == "Aircraft Mechanic":
                employee.role = "GROUND_STAFF"
            elif employee.role == "Administrative":
                employee.role = "ADMINISTRATIVE"
        db.commit()
    except Exception as e:
        print(f"Error updating employee roles: {e}")
        db.rollback()
    finally:
        db.close()

def main():
    """Main function to populate the database"""
    print("Clearing existing data...")
    clear_database()
    
    print("Creating database session...")
    db = SessionLocal()
    
    try:
        print("Adding airports...")
        airports = populate_airports()
        db.add_all(airports)
        db.commit()
        
        print("Adding employees...")
        employees = populate_employees()
        employees = populate_employee_info(employees)
        db.add_all(employees)
        db.commit()
        
        print("Adding flights...")
        flights = populate_flights(airports)
        db.add_all(flights)
        db.commit()
        
        print("Adding passengers...")
        passengers = populate_passengers()
        db.add_all(passengers)
        db.commit()
        
        print("Adding meals...")
        meals = populate_meals()
        db.add_all(meals)
        db.commit()
        
        print("Adding services...")
        services = populate_services()
        db.add_all(services)
        db.commit()
        
        print("Adding bookings...")
        bookings = populate_bookings(flights, passengers)
        db.add_all(bookings)
        db.commit()
        
        print("Database populated successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main() 