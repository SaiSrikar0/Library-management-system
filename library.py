import subprocess
import sys

def run_script(script_name):
	result = subprocess.run([sys.executable, script_name])
	return result.returncode

def main():
	print("Library Management System")
	print("1. Add Member")
	print("2. Add Book")
	print("3. Borrow Book")
	print("4. Return Book")
	print("5. List/Search/Member Details")
	print("6. Update Book/Member Info")
	print("7. Delete Book/Member")
	print("8. Reports")
	print("9. Exit")
	choice = input("Enter your choice (1-9): ").strip()
	if choice == "1":
		run_script("add_members.py")
	elif choice == "2":
		run_script("add_books.py")
	elif choice == "3":
		run_script("borrow.py")
	elif choice == "4":
		run_script("return_book.py")
	elif choice == "5":
		run_script("read_book.py")
	elif choice == "6":
		run_script("update.py")
	elif choice == "7":
		run_script("delete.py")
	elif choice == "8":
		run_script("report.py")
	elif choice == "9":
		print("Exiting...")
		sys.exit(0)
	else:
		print("Invalid choice.")

if __name__ == "__main__":
	while True:
		main()
