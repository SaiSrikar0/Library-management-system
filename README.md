# Library Management System

This is a simple Library Management System built with Python and Supabase (PostgreSQL). It allows you to manage books, members, borrowing, returning, and reporting operations from the command line.

## Features
- Add, update, and delete books and members
- Borrow and return books (with stock management)
- List/search books and view member details
- Generate reports (top borrowed books, overdue members, etc.)
- All operations accessible from a single menu (`library.py`)

## Requirements
- Python 3.8+
- Supabase account and project
- Required Python packages:
  - supabase
  - python-dotenv

## Setup
1. Clone this repository:
   ```
   git clone https://github.com/SaiSrikar0/Library-management-system.git
   cd Library-management-system
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Supabase credentials:
   ```
   supabase_url=YOUR_SUPABASE_URL
   supabase_key=YOUR_SUPABASE_KEY
   ```
4. Run the main program:
   ```
   python library.py
   ```

## Streamlit Frontend

There is a simple Streamlit frontend in `app.py` that wraps the same functionality as the CLI.

To run the Streamlit app (recommended during development):
```powershell
pip install -r requirements.txt
streamlit run app.py
```

## Usage
- Follow the on-screen menu to perform any operation.
- Each menu option corresponds to a specific script for modularity.

## File Structure
- `library.py` - Main menu and entry point
- `add_books.py`, `add_members.py` - Add new books/members
- `borrow.py`, `return_book.py` - Borrow and return books
- `read_book.py` - List/search books, view member details
- `update.py` - Update book/member info
- `delete.py` - Delete books/members
- `report.py` - Generate reports