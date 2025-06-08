import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
from typing import Optional
from ..models.base import Base, engine, SessionLocal
from ..models.models import (
    Airport, Employee, Flight, FlightAssignment,
    Passenger, Booking, Meal, Service
)

app = typer.Typer()
console = Console()

def init_db():
    Base.metadata.create_all(bind=engine)

@app.command()
def setup():
    """Initialize the database."""
    init_db()
    console.print("[green]Database initialized successfully![/green]")

@app.command()
def add_airport(
    code: str = typer.Option(..., prompt=True),
    name: str = typer.Option(..., prompt=True),
    city: str = typer.Option(..., prompt=True),
    country: str = typer.Option(..., prompt=True),
    timezone: str = typer.Option(..., prompt=True)
):
    """Add a new airport to the database."""
    db = SessionLocal()
    airport = Airport(
        code=code.upper(),
        name=name,
        city=city,
        country=country,
        timezone=timezone
    )
    db.add(airport)
    db.commit()
    db.refresh(airport)
    console.print(f"[green]Airport {code} added successfully![/green]")
    db.close()

@app.command()
def list_airports():
    """List all airports in the database."""
    db = SessionLocal()
    airports = db.query(Airport).all()
    
    table = Table(title="Airports")
    table.add_column("Code", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("City", style="green")
    table.add_column("Country", style="yellow")
    
    for airport in airports:
        table.add_row(
            airport.code,
            airport.name,
            airport.city,
            airport.country
        )
    
    console.print(table)
    db.close()

@app.command()
def add_employee(
    employee_id: str = typer.Option(..., prompt=True),
    first_name: str = typer.Option(..., prompt=True),
    last_name: str = typer.Option(..., prompt=True),
    role: str = typer.Option(..., prompt=True),
    email: str = typer.Option(..., prompt=True),
    phone: str = typer.Option(..., prompt=True)
):
    """Add a new employee to the database."""
    db = SessionLocal()
    employee = Employee(
        employee_id=employee_id,
        first_name=first_name,
        last_name=last_name,
        role=role,
        email=email,
        phone=phone
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    console.print(f"[green]Employee {employee_id} added successfully![/green]")
    db.close()

@app.command()
def list_employees():
    """List all employees in the database."""
    db = SessionLocal()
    employees = db.query(Employee).all()
    
    table = Table(title="Employees")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Role", style="green")
    table.add_column("Email", style="yellow")
    
    for employee in employees:
        table.add_row(
            employee.employee_id,
            f"{employee.first_name} {employee.last_name}",
            employee.role.value,
            employee.email
        )
    
    console.print(table)
    db.close()

@app.command()
def add_flight(
    flight_number: str = typer.Option(..., prompt=True),
    departure_airport: str = typer.Option(..., prompt=True),
    arrival_airport: str = typer.Option(..., prompt=True),
    departure_time: str = typer.Option(..., prompt=True),
    arrival_time: str = typer.Option(..., prompt=True),
    aircraft_type: str = typer.Option(..., prompt=True),
    base_price: float = typer.Option(..., prompt=True)
):
    """Add a new flight to the database."""
    db = SessionLocal()
    
    # Get airport IDs
    dep_airport = db.query(Airport).filter(Airport.code == departure_airport.upper()).first()
    arr_airport = db.query(Airport).filter(Airport.code == arrival_airport.upper()).first()
    
    if not dep_airport or not arr_airport:
        console.print("[red]Invalid airport code![/red]")
        return
    
    flight = Flight(
        flight_number=flight_number,
        departure_airport_id=dep_airport.id,
        arrival_airport_id=arr_airport.id,
        departure_time=datetime.fromisoformat(departure_time),
        arrival_time=datetime.fromisoformat(arrival_time),
        aircraft_type=aircraft_type,
        base_price=base_price
    )
    
    db.add(flight)
    db.commit()
    db.refresh(flight)
    console.print(f"[green]Flight {flight_number} added successfully![/green]")
    db.close()

@app.command()
def list_flights():
    """List all flights in the database."""
    db = SessionLocal()
    flights = db.query(Flight).all()
    
    table = Table(title="Flights")
    table.add_column("Number", style="cyan")
    table.add_column("From", style="magenta")
    table.add_column("To", style="green")
    table.add_column("Departure", style="yellow")
    table.add_column("Arrival", style="blue")
    table.add_column("Status", style="red")
    
    for flight in flights:
        table.add_row(
            flight.flight_number,
            flight.departure_airport.code,
            flight.arrival_airport.code,
            flight.departure_time.strftime("%Y-%m-%d %H:%M"),
            flight.arrival_time.strftime("%Y-%m-%d %H:%M"),
            flight.status.value
        )
    
    console.print(table)
    db.close()

@app.command()
def add_passenger(
    passport_number: str = typer.Option(..., prompt=True),
    first_name: str = typer.Option(..., prompt=True),
    last_name: str = typer.Option(..., prompt=True),
    email: str = typer.Option(..., prompt=True),
    phone: str = typer.Option(..., prompt=True)
):
    """Add a new passenger to the database."""
    db = SessionLocal()
    passenger = Passenger(
        passport_number=passport_number,
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone=phone
    )
    db.add(passenger)
    db.commit()
    db.refresh(passenger)
    console.print(f"[green]Passenger {passport_number} added successfully![/green]")
    db.close()

@app.command()
def list_passengers():
    """List all passengers in the database."""
    db = SessionLocal()
    passengers = db.query(Passenger).all()
    
    table = Table(title="Passengers")
    table.add_column("Passport", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Email", style="green")
    table.add_column("Phone", style="yellow")
    
    for passenger in passengers:
        table.add_row(
            passenger.passport_number,
            f"{passenger.first_name} {passenger.last_name}",
            passenger.email,
            passenger.phone
        )
    
    console.print(table)
    db.close()

@app.command()
def add_booking(
    booking_reference: str = typer.Option(..., prompt=True),
    flight_number: str = typer.Option(..., prompt=True),
    passport_number: str = typer.Option(..., prompt=True),
    seat_number: str = typer.Option(..., prompt=True),
    meal_preference: str = typer.Option(..., prompt=True),
    total_price: float = typer.Option(..., prompt=True)
):
    """Add a new booking to the database."""
    db = SessionLocal()
    
    # Get flight and passenger IDs
    flight = db.query(Flight).filter(Flight.flight_number == flight_number).first()
    passenger = db.query(Passenger).filter(Passenger.passport_number == passport_number).first()
    
    if not flight or not passenger:
        console.print("[red]Invalid flight number or passport number![/red]")
        return
    
    booking = Booking(
        booking_reference=booking_reference,
        flight_id=flight.id,
        passenger_id=passenger.id,
        seat_number=seat_number,
        meal_preference=meal_preference,
        total_price=total_price
    )
    
    db.add(booking)
    db.commit()
    db.refresh(booking)
    console.print(f"[green]Booking {booking_reference} added successfully![/green]")
    db.close()

@app.command()
def list_bookings():
    """List all bookings in the database."""
    db = SessionLocal()
    bookings = db.query(Booking).all()
    
    table = Table(title="Bookings")
    table.add_column("Reference", style="cyan")
    table.add_column("Flight", style="magenta")
    table.add_column("Passenger", style="green")
    table.add_column("Seat", style="yellow")
    table.add_column("Meal", style="blue")
    table.add_column("Price", style="red")
    
    for booking in bookings:
        table.add_row(
            booking.booking_reference,
            booking.flight.flight_number,
            f"{booking.passenger.first_name} {booking.passenger.last_name}",
            booking.seat_number,
            booking.meal_preference,
            str(booking.total_price)
        )
    
    console.print(table)
    db.close()

@app.command()
def add_meal(
    name: str = typer.Option(..., prompt=True),
    description: str = typer.Option(..., prompt=True),
    category: str = typer.Option(..., prompt=True),
    price: float = typer.Option(..., prompt=True)
):
    """Add a new meal to the database."""
    db = SessionLocal()
    meal = Meal(
        name=name,
        description=description,
        category=category,
        price=price
    )
    db.add(meal)
    db.commit()
    db.refresh(meal)
    console.print(f"[green]Meal {name} added successfully![/green]")
    db.close()

@app.command()
def list_meals():
    """List all meals in the database."""
    db = SessionLocal()
    meals = db.query(Meal).all()
    
    table = Table(title="Meals")
    table.add_column("Name", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_column("Category", style="green")
    table.add_column("Price", style="yellow")
    
    for meal in meals:
        table.add_row(
            meal.name,
            meal.description,
            meal.category,
            str(meal.price)
        )
    
    console.print(table)
    db.close()

@app.command()
def add_service(
    name: str = typer.Option(..., prompt=True),
    description: str = typer.Option(..., prompt=True),
    price: float = typer.Option(..., prompt=True)
):
    """Add a new service to the database."""
    db = SessionLocal()
    service = Service(
        name=name,
        description=description,
        price=price
    )
    db.add(service)
    db.commit()
    db.refresh(service)
    console.print(f"[green]Service {name} added successfully![/green]")
    db.close()

@app.command()
def list_services():
    """List all services in the database."""
    db = SessionLocal()
    services = db.query(Service).all()
    
    table = Table(title="Services")
    table.add_column("Name", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_column("Price", style="green")
    
    for service in services:
        table.add_row(
            service.name,
            service.description,
            str(service.price)
        )
    
    console.print(table)
    db.close()

@app.command()
def clear_all_data():
    """Clear all data stored in the database."""
    db = SessionLocal()
    db.query(Booking).delete()
    db.query(Passenger).delete()
    db.query(FlightAssignment).delete()
    db.query(Flight).delete()
    db.query(Employee).delete()
    db.query(Airport).delete()
    db.query(Meal).delete()
    db.query(Service).delete()
    db.commit()
    console.print("[green]All data cleared successfully![/green]")
    db.close()

if __name__ == "__main__":
    app() 