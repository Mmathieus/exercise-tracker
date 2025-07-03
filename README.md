# Exercise Tracker 🏋️‍♂️

A simple command-line application for tracking exercise routines using SQLite database. Perfect for logging workouts, setting targets, and monitoring your fitness progress.

## Features ✨

- **Create Database Table** - Initialize or reset your exercise database
- **Insert Records** - Add past, completed or planned exercises
- **View Records** - Filter and display your exercise history
- **Update Records** - Modify existing exercise records
- **Delete Records** - Delete existing exercise records
- **Interactive Menu** - User-friendly command-line interface

## Installation 🚀

### Prerequisites
- [Python 3.6+](https://www.python.org/downloads/)
- Required Python packages:

#### Direct installation
```bash
pip install tabulate
```

#### Using requirements.txt
```bash
pip install -r requirements.txt
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

3. Initialize database:
   ```bash
   ➤ table
   ```

## Usage 💻

### Available Commands

When you run the program, you can use these commands:

- `table` - Create a new empty database (⚠️ existing data will be lost)
- `select` - Filter and retrieve existing records
- `insert` - Insert new record
- `update` - Update existing record(s)
- `delete` - Delete existing record(s)
- `q` - Exit the program
- `help` - Show available commands

### Database Schema

The application uses a SQLite table with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| exercise | TEXT | Name of the exercise |
| reps | INTEGER | Number of reps completed |
| target_reps | INTEGER | Target number of reps |
| date | TEXT | Date of exercise (YYYY-MM-DD) |
| time | TEXT | Time of exercise (HH:MM:SS) |
| created_at | TEXT | Record creation timestamp |
| updated_at | TEXT | Last update timestamp |

## Examples 🧑‍💻

### ✚ `INSERT` - Adding a Completed Workout
```
➤ insert

╭─── SELECT INSERT ───
│ [1]  » Exercise from the past
│ [2]  » Just completed exercise
│ [3]  » Upcoming exercise
│
│─── Info ───
│ ⭐  Required field
│ ⚪  Optional field

 Insert ▶ 2
⭐ Exercise ▶ Push-ups
⭐ Reps (done) ▶ 30
⚪ Reps (target) ▶ 25
-> ✅ RECORD INSERTED
```

### 👁️ `SELECT` - Retrieving Records Using Filter
```
➤ select

╭─── FILTER RECORDS? ───
│ [0]  » No
│ [1]  » Yes

 Filter ▶ 1

╭─── SELECT COLUMN(S) ───
│ [1]  » Exercise
│ [2]  » Date
│ [3]  » Exercise & Date
│
│─── Info ───
│ ⭐  Required field
│ ⚪  Optional field

 Column ▶ 1
⭐ Exercise ▶ Push-ups
+------+------------+--------+---------------+------------+----------+---------------------+---------------------+
|  id  |  exercise  |  reps  |  target_reps  |    date    |   time   |     created_at      |     updated_at      |
|------+------------+--------+---------------+------------+----------+---------------------+---------------------|
|  1   |  Push-ups  |   30   |      25       | 2025-07-04 | 00:10:21 | 2025-07-04 00:10:21 | 2025-07-04 00:10:21 |
+------+------------+--------+---------------+------------+----------+---------------------+---------------------+
```

### ✏️ `UPDATE` - Updating Record
```
➤ update
╭─── Info ───
│ ⭐  Required field
│ ⚪  Optional field

⭐ Updating column ▶ reps
⭐ Updated value ▶ 28
⭐ Searching column ▶ id
⭐ Searching value ▶ 1
-> ✅ RECORD(S) UPDATED
```

### 🗑️ `DELETE` - Deleting Record
```
➤ delete
╭─── Info ───
│ ⭐  Required field
│ ⚪  Optional field

⭐ Searching column ▶ id
⭐ Searching value ▶ 1
-> ✅ RECORD(S) DELETED
```

## File Structure 📁

```
exercise-tracker/
├── common/
│   ├── utils.py         # General utility functions used across the application
│   └── validator.py     # Input validation functions
├── core/
│   ├── create.py        # Database table creation and refresh operations
│   ├── delete.py        # Database delete operations
│   ├── get.py           # Database read/select operations
│   ├── insert.py        # Database insert operations
│   └── update.py        # Database update operations
├── data/
│   └── exercise.db      # SQLite database file
├── LICENSE              # Project license
├── main.py              # Main application entry point
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## Support 💬

If you encounter any issues or have questions: 
1. Check the existing issues on GitHub 
2. Create a new issue with detailed description 
3. Include error messages and steps to reproduce
4. Provide system information (OS, Python version, etc.)
5. Attach screenshots if applicable

---

# **Happy exercising! 💪**