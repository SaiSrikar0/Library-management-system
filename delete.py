'''	• Delete a member (only if no borrowed books).
	• Delete a book (only if not borrowed).
'''
import os
from supabase import create_client, Client # pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()
url: str = os.getenv("supabase_url")
key: str = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def delete_book(book_id):
    # Check if book is borrowed
    borrowed = sb.table("borrow_records").select("book_id").eq("book_id", book_id).execute().data
    if borrowed:
        print("Cannot delete book; it is currently borrowed.")
        return None
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    return resp.data
def delete_member(member_id):
    # Check if member has borrowed books
    borrowed = sb.table("borrow_records").select("book_id").eq("member_id", member_id).execute().data
    if borrowed:
        print("Cannot delete member; they have borrowed books.")
        return None
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data
if __name__ == "__main__":
    print("1. Delete a book")
    print("2. Delete a member")
    choice = input("Enter choice (1-2): ").strip()
    if choice == "1":
        book_id = int(input("Enter book ID to delete: ").strip())
        deleted = delete_book(book_id)
        if deleted:
            print("Deleted Book:", deleted)
    elif choice == "2":
        member_id = int(input("Enter member ID to delete: ").strip())
        deleted = delete_member(member_id)
        if deleted:
            print("Deleted Member:", deleted)
    else:
        print("Invalid choice.")