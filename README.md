# Exercise Tracker 🏋️‍♂️

A simple command-line application for tracking exercise routines using SQLite database. Perfect for logging workouts, setting targets, and monitoring your fitness progress.

## Features ✨

- **Create Database Table** - Initialize or reset your exercise database
- **Insert Records** - Add completed workouts or plan future exercises
- **View Records** - Filter and display your exercise history
- **Update Records** - Modify existing workout data
- **Delete Records** - Delete existing workout data
- **Interactive Menu** - User-friendly command-line interface

## Installation 🚀

### Prerequisites
- Python 3.6+
- Required Python packages:
  ```bash
  pip install tabulate
  ```

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Mmathieus/exercise-tracker.git
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Create table/database:
   ```bash
   : table
   ```

## Usage 💻

### Available Commands

When you run the program, you can use these commands:

- `table` - Create a new empty table (⚠️ existing data will be lost)
- `select` - Filter and retrieve existing records
- `insert` - Insert new record(s) into the table
- `update` - Update existing record values
- `delete` - Delete existing record(s) from the table
- `help` - Show available commands
- `q` - Exit the program

### Database Schema

The application uses a SQLite table with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| exercise | TEXT | Name of the exercise |
| actual_reps | INTEGER | Number of reps completed |
| target_reps | INTEGER | Target number of reps |
| date | TEXT | Date of exercise (YYYY-MM-DD) |
| time | TEXT | Time of exercise (HH:MM:SS) |
| created_at | TEXT | Record creation timestamp |
| updated_at | TEXT | Last update timestamp |

## Examples 📝

### Adding a Completed Workout
```
: insert
--- INSERT RECORD MENU ---
[1] - Full (exercise done!)
[0] - Partial (exercise in future)

choice: 1
date (YYYY-MM-DD): 2024-01-15
time (HH:MM:SS) (optional): 14:30:00
exercise: Push-ups
reps: 25
expected reps (optional): 30
-> ✅ RECORD INSERTED
```

### Planning a Future Workout
```
: insert
--- INSERT RECORD MENU ---
[1] - Full (exercise done!)
[0] - Partial (exercise in future)

choice: 0
date (YYYY-MM-DD): 2024-01-20
time (HH:MM:SS) (optional): 16:00:00
exercise: Squats
expected reps (optional): 50
-> ✅ RECORD INSERTED
```

### Viewing Records with Filters
```
: select
--- FILTER RECORDS? ---
[1] - Yes
[0] - No

choice: 1
--- COLUMNS FILTER ---
[1] - Exercise
[2] - Date
[3] - Exercise & Date

filter choice: 1
exercise: Push-ups
```

### Updating a Record
```
: update
Column to update: actual_reps
Updated value: 30
Key column: id
Key value: 1
-> ✅ RECORD(S) UPDATED
```

### Deleting a Record
```
: delete
Column: id
Value: 5
-> ✅ RECORD(S) DELETED
```

## File Structure 📁

```
exercise-tracker/
├── main.py          # Main application entry point
├── create.py        # Database table creation
├── insert.py        # Record insertion functionality
├── get.py           # Record retrieval and filtering
├── update.py        # Record update functionality
├── delete.py        # Record deletion functionality
├── utils.py         # Utility functions
├── data/
│   └── exercise.db  # SQLite database file (empty)
└── README.md        # This file
```

## Features in Detail 🔍

### Record Types
- **Full Records**: For completed exercises with actual rep counts
- **Partial Records**: For planning future workouts with target reps only

### Filtering Options
- View all records
- Filter by exercise name
- Filter by date
- Filter by both exercise name and date

### Data Validation
- Automatic timestamp generation
- Simple but not perfect and sophisticated input validation
- Basic error handling with user-friendly messages

## Future Enhancements 🚀

- Data export/import functionality
- Input validation (type, format, value)

## Support 💬

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---

**Happy exercising! 💪**