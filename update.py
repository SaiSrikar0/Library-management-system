'''	• Update book stock (e.g., when more copies are purchased).
	• Update member info (e.g., change email).
'''
import os
from supabase import create_client, Client # pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()
url: str = os.getenv("supabase_url")
key: str = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def update_book_stock(book_id, stock):
    payload = {"stock": stock}
    resp = sb.table("books").update(payload).eq("book_id", book_id).execute()
    return resp.data
def update_member_info(member_id, email):
    payload = {"email": email}
    resp = sb.table("members").update(payload).eq("member_id", member_id).execute()
    return resp.data
if __name__ == "__main__":
    print("1. Update book stock")
    print("2. Update member email")
    choice = input("Enter choice (1-2): ").strip()
    if choice == "1":
        book_id = int(input("Enter book ID to update: ").strip())
        stock = int(input("Enter new stock value: ").strip())
        updated = update_book_stock(book_id, stock)
        print("Updated Book:", updated)
    elif choice == "2":
        member_id = int(input("Enter member ID to update: ").strip())
        email = input("Enter new email: ").strip()
        updated = update_member_info(member_id, email)
        print("Updated Member:", updated)
    else:
        print("Invalid choice.")