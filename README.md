# SkyLogix Pro - Airline Database Management System

A comprehensive database management system for airlines that centralizes all airline-related data including flights, employees, airports, and services.

## Features

- Centralized storage for all airline data
- Flight scheduling and management
- Employee management
- Airport and route management
- Passenger and booking management
- Meal and service management
- Analytics and reporting capabilities

## Project Structure

```
skylogix/
├── models/         # Database models and schemas
├── cli/           # Command-line interface
├── core/          # Core business logic
├── utils/         # Utility functions
└── tests/         # Test cases
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
python -m skylogix.cli setup
```

## Usage

Run the CLI application:
```bash
python -m skylogix.cli
```

## Available CLI Commands

- `python -m skylogix.cli setup` — Initialize the database
- `python -m skylogix.cli add-airport` — Add a new airport
- `python -m skylogix.cli list-airports` — List all airports
- `python -m skylogix.cli add-employee` — Add a new employee
- `python -m skylogix.cli list-employees` — List all employees
- `python -m skylogix.cli add-flight` — Add a new flight
- `python -m skylogix.cli list-flights` — List all flights
- `python -m skylogix.cli add-passenger` — Add a new passenger
- `python -m skylogix.cli list-passengers` — List all passengers
- `python -m skylogix.cli add-booking` — Add a new booking
- `python -m skylogix.cli list-bookings` — List all bookings
- `python -m skylogix.cli add-meal` — Add a new meal
- `python -m skylogix.cli list-meals` — List all meals
- `python -m skylogix.cli add-service` — Add a new service
- `python -m skylogix.cli list-services` — List all services
- `python -m skylogix.cli clear-all-data` — Clear all data stored in the database

## Database Schema

The system includes the following main entities:
- Flights
- Employees
- Airports
- Passengers
- Bookings
- Meals
- Services

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 