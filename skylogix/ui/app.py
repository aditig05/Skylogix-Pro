import tkinter as tk
from tkinter import ttk, messagebox
from ..models.base import SessionLocal
from ..models.models import Airport, Employee, Flight, Passenger, Booking, Meal, Service
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from datetime import datetime

class SkyLogixUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SkyLogix Pro")
        self.root.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Create a notebook (tabbed interface)
        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=True, fill='both')

        # Create tabs for different functionalities
        self.create_airport_tab(notebook)
        self.create_employee_tab(notebook)
        self.create_flight_tab(notebook)
        self.create_passenger_tab(notebook)
        self.create_booking_tab(notebook)
        self.create_meal_tab(notebook)
        self.create_service_tab(notebook)
        self.create_analytics_tab(notebook)

    def create_airport_tab(self, notebook):
        airport_frame = ttk.Frame(notebook)
        notebook.add(airport_frame, text="Airports")

        # Add Airport
        ttk.Label(airport_frame, text="Add Airport").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(airport_frame, text="Code:").grid(row=1, column=0, pady=5)
        code_entry = ttk.Entry(airport_frame)
        code_entry.grid(row=1, column=1, pady=5)
        ttk.Label(airport_frame, text="Name:").grid(row=2, column=0, pady=5)
        name_entry = ttk.Entry(airport_frame)
        name_entry.grid(row=2, column=1, pady=5)
        ttk.Label(airport_frame, text="City:").grid(row=3, column=0, pady=5)
        city_entry = ttk.Entry(airport_frame)
        city_entry.grid(row=3, column=1, pady=5)
        ttk.Label(airport_frame, text="Country:").grid(row=4, column=0, pady=5)
        country_entry = ttk.Entry(airport_frame)
        country_entry.grid(row=4, column=1, pady=5)
        ttk.Label(airport_frame, text="Timezone:").grid(row=5, column=0, pady=5)
        timezone_entry = ttk.Entry(airport_frame)
        timezone_entry.grid(row=5, column=1, pady=5)

        def add_airport():
            db = SessionLocal()
            airport = Airport(
                code=code_entry.get().upper(),
                name=name_entry.get(),
                city=city_entry.get(),
                country=country_entry.get(),
                timezone=timezone_entry.get()
            )
            db.add(airport)
            db.commit()
            db.refresh(airport)
            messagebox.showinfo("Success", f"Airport {airport.code} added successfully!")
            db.close()

        ttk.Button(airport_frame, text="Add Airport", command=add_airport).grid(row=6, column=0, columnspan=2, pady=10)

        # List Airports
        ttk.Label(airport_frame, text="List Airports").grid(row=7, column=0, columnspan=2, pady=10)
        airport_listbox = tk.Listbox(airport_frame, width=50, height=10)
        airport_listbox.grid(row=8, column=0, columnspan=2, pady=5)

        def list_airports():
            db = SessionLocal()
            airports = db.query(Airport).all()
            airport_listbox.delete(0, tk.END)
            for airport in airports:
                airport_listbox.insert(tk.END, f"{airport.code} - {airport.name} ({airport.city}, {airport.country})")
            db.close()

        ttk.Button(airport_frame, text="Refresh List", command=list_airports).grid(row=9, column=0, columnspan=2, pady=10)

    def create_employee_tab(self, notebook):
        employee_frame = ttk.Frame(notebook)
        notebook.add(employee_frame, text="Employees")

        # Add Employee
        ttk.Label(employee_frame, text="Add Employee").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(employee_frame, text="Employee ID:").grid(row=1, column=0, pady=5)
        employee_id_entry = ttk.Entry(employee_frame)
        employee_id_entry.grid(row=1, column=1, pady=5)
        ttk.Label(employee_frame, text="First Name:").grid(row=2, column=0, pady=5)
        first_name_entry = ttk.Entry(employee_frame)
        first_name_entry.grid(row=2, column=1, pady=5)
        ttk.Label(employee_frame, text="Last Name:").grid(row=3, column=0, pady=5)
        last_name_entry = ttk.Entry(employee_frame)
        last_name_entry.grid(row=3, column=1, pady=5)
        ttk.Label(employee_frame, text="Role:").grid(row=4, column=0, pady=5)
        role_entry = ttk.Entry(employee_frame)
        role_entry.grid(row=4, column=1, pady=5)
        ttk.Label(employee_frame, text="Email:").grid(row=5, column=0, pady=5)
        email_entry = ttk.Entry(employee_frame)
        email_entry.grid(row=5, column=1, pady=5)
        ttk.Label(employee_frame, text="Phone:").grid(row=6, column=0, pady=5)
        phone_entry = ttk.Entry(employee_frame)
        phone_entry.grid(row=6, column=1, pady=5)

        def add_employee():
            db = SessionLocal()
            employee = Employee(
                employee_id=employee_id_entry.get(),
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                role=role_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get()
            )
            db.add(employee)
            db.commit()
            db.refresh(employee)
            messagebox.showinfo("Success", f"Employee {employee.employee_id} added successfully!")
            db.close()

        ttk.Button(employee_frame, text="Add Employee", command=add_employee).grid(row=7, column=0, columnspan=2, pady=10)

        # List Employees
        ttk.Label(employee_frame, text="List Employees").grid(row=8, column=0, columnspan=2, pady=10)
        employee_listbox = tk.Listbox(employee_frame, width=50, height=10)
        employee_listbox.grid(row=9, column=0, columnspan=2, pady=5)

        def list_employees():
            db = SessionLocal()
            employees = db.query(Employee).all()
            employee_listbox.delete(0, tk.END)
            for employee in employees:
                employee_listbox.insert(tk.END, f"{employee.employee_id} - {employee.first_name} {employee.last_name} ({employee.role})")
            db.close()

        ttk.Button(employee_frame, text="Refresh List", command=list_employees).grid(row=10, column=0, columnspan=2, pady=10)

    def create_flight_tab(self, notebook):
        flight_frame = ttk.Frame(notebook)
        notebook.add(flight_frame, text="Flights")

        # Add Flight
        ttk.Label(flight_frame, text="Add Flight").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(flight_frame, text="Flight Number:").grid(row=1, column=0, pady=5)
        flight_number_entry = ttk.Entry(flight_frame)
        flight_number_entry.grid(row=1, column=1, pady=5)
        ttk.Label(flight_frame, text="Departure Airport:").grid(row=2, column=0, pady=5)
        departure_airport_entry = ttk.Entry(flight_frame)
        departure_airport_entry.grid(row=2, column=1, pady=5)
        ttk.Label(flight_frame, text="Arrival Airport:").grid(row=3, column=0, pady=5)
        arrival_airport_entry = ttk.Entry(flight_frame)
        arrival_airport_entry.grid(row=3, column=1, pady=5)
        ttk.Label(flight_frame, text="Departure Time:").grid(row=4, column=0, pady=5)
        departure_time_entry = ttk.Entry(flight_frame)
        departure_time_entry.grid(row=4, column=1, pady=5)
        ttk.Label(flight_frame, text="Arrival Time:").grid(row=5, column=0, pady=5)
        arrival_time_entry = ttk.Entry(flight_frame)
        arrival_time_entry.grid(row=5, column=1, pady=5)
        ttk.Label(flight_frame, text="Aircraft Type:").grid(row=6, column=0, pady=5)
        aircraft_type_entry = ttk.Entry(flight_frame)
        aircraft_type_entry.grid(row=6, column=1, pady=5)
        ttk.Label(flight_frame, text="Base Price:").grid(row=7, column=0, pady=5)
        base_price_entry = ttk.Entry(flight_frame)
        base_price_entry.grid(row=7, column=1, pady=5)

        def add_flight():
            db = SessionLocal()
            dep_airport = db.query(Airport).filter(Airport.code == departure_airport_entry.get().upper()).first()
            arr_airport = db.query(Airport).filter(Airport.code == arrival_airport_entry.get().upper()).first()
            if not dep_airport or not arr_airport:
                messagebox.showerror("Error", "Invalid airport code!")
                return
            flight = Flight(
                flight_number=flight_number_entry.get(),
                departure_airport_id=dep_airport.id,
                arrival_airport_id=arr_airport.id,
                departure_time=departure_time_entry.get(),
                arrival_time=arrival_time_entry.get(),
                aircraft_type=aircraft_type_entry.get(),
                base_price=float(base_price_entry.get())
            )
            db.add(flight)
            db.commit()
            db.refresh(flight)
            messagebox.showinfo("Success", f"Flight {flight.flight_number} added successfully!")
            db.close()

        ttk.Button(flight_frame, text="Add Flight", command=add_flight).grid(row=8, column=0, columnspan=2, pady=10)

        # List Flights
        ttk.Label(flight_frame, text="List Flights").grid(row=9, column=0, columnspan=2, pady=10)
        flight_listbox = tk.Listbox(flight_frame, width=50, height=10)
        flight_listbox.grid(row=10, column=0, columnspan=2, pady=5)

        def list_flights():
            db = SessionLocal()
            flights = db.query(Flight).all()
            flight_listbox.delete(0, tk.END)
            for flight in flights:
                flight_listbox.insert(tk.END, f"{flight.flight_number} - {flight.departure_airport.code} to {flight.arrival_airport.code} ({flight.departure_time} to {flight.arrival_time})")
            db.close()

        ttk.Button(flight_frame, text="Refresh List", command=list_flights).grid(row=11, column=0, columnspan=2, pady=10)

    def create_passenger_tab(self, notebook):
        passenger_frame = ttk.Frame(notebook)
        notebook.add(passenger_frame, text="Passengers")

        # Add Passenger
        ttk.Label(passenger_frame, text="Add Passenger").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(passenger_frame, text="Passport Number:").grid(row=1, column=0, pady=5)
        passport_number_entry = ttk.Entry(passenger_frame)
        passport_number_entry.grid(row=1, column=1, pady=5)
        ttk.Label(passenger_frame, text="First Name:").grid(row=2, column=0, pady=5)
        first_name_entry = ttk.Entry(passenger_frame)
        first_name_entry.grid(row=2, column=1, pady=5)
        ttk.Label(passenger_frame, text="Last Name:").grid(row=3, column=0, pady=5)
        last_name_entry = ttk.Entry(passenger_frame)
        last_name_entry.grid(row=3, column=1, pady=5)
        ttk.Label(passenger_frame, text="Email:").grid(row=4, column=0, pady=5)
        email_entry = ttk.Entry(passenger_frame)
        email_entry.grid(row=4, column=1, pady=5)
        ttk.Label(passenger_frame, text="Phone:").grid(row=5, column=0, pady=5)
        phone_entry = ttk.Entry(passenger_frame)
        phone_entry.grid(row=5, column=1, pady=5)

        def add_passenger():
            db = SessionLocal()
            passenger = Passenger(
                passport_number=passport_number_entry.get(),
                first_name=first_name_entry.get(),
                last_name=last_name_entry.get(),
                email=email_entry.get(),
                phone=phone_entry.get()
            )
            db.add(passenger)
            db.commit()
            db.refresh(passenger)
            messagebox.showinfo("Success", f"Passenger {passenger.passport_number} added successfully!")
            db.close()

        ttk.Button(passenger_frame, text="Add Passenger", command=add_passenger).grid(row=6, column=0, columnspan=2, pady=10)

        # List Passengers
        ttk.Label(passenger_frame, text="List Passengers").grid(row=7, column=0, columnspan=2, pady=10)
        passenger_listbox = tk.Listbox(passenger_frame, width=50, height=10)
        passenger_listbox.grid(row=8, column=0, columnspan=2, pady=5)

        def list_passengers():
            db = SessionLocal()
            passengers = db.query(Passenger).all()
            passenger_listbox.delete(0, tk.END)
            for passenger in passengers:
                passenger_listbox.insert(tk.END, f"{passenger.passport_number} - {passenger.first_name} {passenger.last_name} ({passenger.email})")
            db.close()

        ttk.Button(passenger_frame, text="Refresh List", command=list_passengers).grid(row=9, column=0, columnspan=2, pady=10)

    def create_booking_tab(self, notebook):
        booking_frame = ttk.Frame(notebook)
        notebook.add(booking_frame, text="Bookings")

        # Add Booking
        ttk.Label(booking_frame, text="Add Booking").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(booking_frame, text="Booking Reference:").grid(row=1, column=0, pady=5)
        booking_reference_entry = ttk.Entry(booking_frame)
        booking_reference_entry.grid(row=1, column=1, pady=5)
        ttk.Label(booking_frame, text="Flight Number:").grid(row=2, column=0, pady=5)
        flight_number_entry = ttk.Entry(booking_frame)
        flight_number_entry.grid(row=2, column=1, pady=5)
        ttk.Label(booking_frame, text="Passport Number:").grid(row=3, column=0, pady=5)
        passport_number_entry = ttk.Entry(booking_frame)
        passport_number_entry.grid(row=3, column=1, pady=5)
        ttk.Label(booking_frame, text="Seat Number:").grid(row=4, column=0, pady=5)
        seat_number_entry = ttk.Entry(booking_frame)
        seat_number_entry.grid(row=4, column=1, pady=5)
        ttk.Label(booking_frame, text="Meal Preference:").grid(row=5, column=0, pady=5)
        meal_preference_entry = ttk.Entry(booking_frame)
        meal_preference_entry.grid(row=5, column=1, pady=5)
        ttk.Label(booking_frame, text="Total Price:").grid(row=6, column=0, pady=5)
        total_price_entry = ttk.Entry(booking_frame)
        total_price_entry.grid(row=6, column=1, pady=5)

        def add_booking():
            db = SessionLocal()
            flight = db.query(Flight).filter(Flight.flight_number == flight_number_entry.get()).first()
            passenger = db.query(Passenger).filter(Passenger.passport_number == passport_number_entry.get()).first()
            if not flight or not passenger:
                messagebox.showerror("Error", "Invalid flight number or passport number!")
                return
            booking = Booking(
                booking_reference=booking_reference_entry.get(),
                flight_id=flight.id,
                passenger_id=passenger.id,
                seat_number=seat_number_entry.get(),
                meal_preference=meal_preference_entry.get(),
                total_price=float(total_price_entry.get())
            )
            db.add(booking)
            db.commit()
            db.refresh(booking)
            messagebox.showinfo("Success", f"Booking {booking.booking_reference} added successfully!")
            db.close()

        ttk.Button(booking_frame, text="Add Booking", command=add_booking).grid(row=7, column=0, columnspan=2, pady=10)

        # List Bookings
        ttk.Label(booking_frame, text="List Bookings").grid(row=8, column=0, columnspan=2, pady=10)
        booking_listbox = tk.Listbox(booking_frame, width=50, height=10)
        booking_listbox.grid(row=9, column=0, columnspan=2, pady=5)

        def list_bookings():
            db = SessionLocal()
            bookings = db.query(Booking).all()
            booking_listbox.delete(0, tk.END)
            for booking in bookings:
                booking_listbox.insert(tk.END, f"{booking.booking_reference} - Flight: {booking.flight.flight_number}, Passenger: {booking.passenger.first_name} {booking.passenger.last_name}")
            db.close()

        ttk.Button(booking_frame, text="Refresh List", command=list_bookings).grid(row=10, column=0, columnspan=2, pady=10)

    def create_meal_tab(self, notebook):
        meal_frame = ttk.Frame(notebook)
        notebook.add(meal_frame, text="Meals")

        # Add Meal
        ttk.Label(meal_frame, text="Add Meal").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(meal_frame, text="Name:").grid(row=1, column=0, pady=5)
        name_entry = ttk.Entry(meal_frame)
        name_entry.grid(row=1, column=1, pady=5)
        ttk.Label(meal_frame, text="Description:").grid(row=2, column=0, pady=5)
        description_entry = ttk.Entry(meal_frame)
        description_entry.grid(row=2, column=1, pady=5)
        ttk.Label(meal_frame, text="Category:").grid(row=3, column=0, pady=5)
        category_entry = ttk.Entry(meal_frame)
        category_entry.grid(row=3, column=1, pady=5)
        ttk.Label(meal_frame, text="Price:").grid(row=4, column=0, pady=5)
        price_entry = ttk.Entry(meal_frame)
        price_entry.grid(row=4, column=1, pady=5)

        def add_meal():
            db = SessionLocal()
            meal = Meal(
                name=name_entry.get(),
                description=description_entry.get(),
                category=category_entry.get(),
                price=float(price_entry.get())
            )
            db.add(meal)
            db.commit()
            db.refresh(meal)
            messagebox.showinfo("Success", f"Meal {meal.name} added successfully!")
            db.close()

        ttk.Button(meal_frame, text="Add Meal", command=add_meal).grid(row=5, column=0, columnspan=2, pady=10)

        # List Meals
        ttk.Label(meal_frame, text="List Meals").grid(row=6, column=0, columnspan=2, pady=10)
        meal_listbox = tk.Listbox(meal_frame, width=50, height=10)
        meal_listbox.grid(row=7, column=0, columnspan=2, pady=5)

        def list_meals():
            db = SessionLocal()
            meals = db.query(Meal).all()
            meal_listbox.delete(0, tk.END)
            for meal in meals:
                meal_listbox.insert(tk.END, f"{meal.name} - {meal.description} ({meal.category}) - ${meal.price}")
            db.close()

        ttk.Button(meal_frame, text="Refresh List", command=list_meals).grid(row=8, column=0, columnspan=2, pady=10)

    def create_service_tab(self, notebook):
        service_frame = ttk.Frame(notebook)
        notebook.add(service_frame, text="Services")

        # Add Service
        ttk.Label(service_frame, text="Add Service").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Label(service_frame, text="Name:").grid(row=1, column=0, pady=5)
        name_entry = ttk.Entry(service_frame)
        name_entry.grid(row=1, column=1, pady=5)
        ttk.Label(service_frame, text="Description:").grid(row=2, column=0, pady=5)
        description_entry = ttk.Entry(service_frame)
        description_entry.grid(row=2, column=1, pady=5)
        ttk.Label(service_frame, text="Price:").grid(row=3, column=0, pady=5)
        price_entry = ttk.Entry(service_frame)
        price_entry.grid(row=3, column=1, pady=5)

        def add_service():
            db = SessionLocal()
            service = Service(
                name=name_entry.get(),
                description=description_entry.get(),
                price=float(price_entry.get())
            )
            db.add(service)
            db.commit()
            db.refresh(service)
            messagebox.showinfo("Success", f"Service {service.name} added successfully!")
            db.close()

        ttk.Button(service_frame, text="Add Service", command=add_service).grid(row=4, column=0, columnspan=2, pady=10)

        # List Services
        ttk.Label(service_frame, text="List Services").grid(row=5, column=0, columnspan=2, pady=10)
        service_listbox = tk.Listbox(service_frame, width=50, height=10)
        service_listbox.grid(row=6, column=0, columnspan=2, pady=5)

        def list_services():
            db = SessionLocal()
            services = db.query(Service).all()
            service_listbox.delete(0, tk.END)
            for service in services:
                service_listbox.insert(tk.END, f"{service.name} - {service.description} - ${service.price}")
            db.close()

        ttk.Button(service_frame, text="Refresh List", command=list_services).grid(row=7, column=0, columnspan=2, pady=10)

    def create_analytics_tab(self, notebook):
        analytics_frame = ttk.Frame(notebook)
        notebook.add(analytics_frame, text="Analytics")

        # Create a frame for the plots
        plots_frame = ttk.Frame(analytics_frame)
        plots_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Create buttons for different analytics
        ttk.Button(analytics_frame, text="Flight Distribution by Route", 
                  command=lambda: self.show_flight_distribution(plots_frame)).pack(pady=5)
        ttk.Button(analytics_frame, text="Booking Trends", 
                  command=lambda: self.show_booking_trends(plots_frame)).pack(pady=5)
        ttk.Button(analytics_frame, text="Revenue by Route", 
                  command=lambda: self.show_revenue_by_route(plots_frame)).pack(pady=5)
        ttk.Button(analytics_frame, text="Employee Distribution", 
                  command=lambda: self.show_employee_distribution(plots_frame)).pack(pady=5)

    def show_flight_distribution(self, parent):
        # Clear previous plot
        for widget in parent.winfo_children():
            widget.destroy()

        db = SessionLocal()
        flights = db.query(Flight).all()
        
        # Create route counts
        routes = {}
        for flight in flights:
            dep = db.query(Airport).filter(Airport.id == flight.departure_airport_id).first()
            arr = db.query(Airport).filter(Airport.id == flight.arrival_airport_id).first()
            route = f"{dep.code}-{arr.code}"
            routes[route] = routes.get(route, 0) + 1

        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        routes_list = list(routes.keys())
        counts = list(routes.values())
        
        ax.bar(routes_list, counts)
        ax.set_title("Flight Distribution by Route")
        ax.set_xlabel("Route")
        ax.set_ylabel("Number of Flights")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Embed plot in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        db.close()

    def show_booking_trends(self, parent):
        # Clear previous plot
        for widget in parent.winfo_children():
            widget.destroy()

        db = SessionLocal()
        bookings = db.query(Booking).all()
        
        # Create booking dates
        dates = [booking.booking_date for booking in bookings]
        date_counts = pd.Series(dates).value_counts().sort_index()

        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        date_counts.plot(kind='line', marker='o', ax=ax)
        ax.set_title("Booking Trends Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Number of Bookings")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Embed plot in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        db.close()

    def show_revenue_by_route(self, parent):
        # Clear previous plot
        for widget in parent.winfo_children():
            widget.destroy()

        db = SessionLocal()
        flights = db.query(Flight).all()
        
        # Calculate revenue by route
        route_revenue = {}
        for flight in flights:
            dep = db.query(Airport).filter(Airport.id == flight.departure_airport_id).first()
            arr = db.query(Airport).filter(Airport.id == flight.arrival_airport_id).first()
            route = f"{dep.code}-{arr.code}"
            bookings = db.query(Booking).filter(Booking.flight_id == flight.id).all()
            revenue = sum(booking.total_price for booking in bookings)
            route_revenue[route] = route_revenue.get(route, 0) + revenue

        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        routes = list(route_revenue.keys())
        revenue = list(route_revenue.values())
        
        ax.bar(routes, revenue)
        ax.set_title("Revenue by Route")
        ax.set_xlabel("Route")
        ax.set_ylabel("Revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Embed plot in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        db.close()

    def show_employee_distribution(self, parent):
        # Clear previous plot
        for widget in parent.winfo_children():
            widget.destroy()

        db = SessionLocal()
        employees = db.query(Employee).all()
        
        # Count employees by role
        roles = {}
        for employee in employees:
            roles[employee.role] = roles.get(employee.role, 0) + 1

        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        role_list = list(roles.keys())
        counts = list(roles.values())
        
        ax.pie(counts, labels=role_list, autopct='%1.1f%%')
        ax.set_title("Employee Distribution by Role")
        plt.tight_layout()

        # Embed plot in tkinter
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        db.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = SkyLogixUI(root)
    root.mainloop() 