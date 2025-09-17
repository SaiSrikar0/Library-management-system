'''
Library Management System using Supabase (PostgreSQL)
    • List all books with availability.
	• Search books by title/author/category.
	• Show member details and their borrowed books.
'''
import os
from supabase import create_client, Client # pip install supabase
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()
url: str = os.getenv("supabase_url")
key: str = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def list_books():
    resp = sb.table("books").select("*").execute()
    return resp.data
def search_books(keyword):
    resp = sb.table("books").select("*").or_(f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%").execute()
    return resp.data
def get_member_details(member_id):
    member = sb.table("members").select("*").eq("member_id", member_id).execute().data
    borrowed = sb.table("borrow_records").select("book_id, borrow_date, return_date").eq("member_id", member_id).execute().data
    return {"member": member, "borrowed_books": borrowed}
if __name__ == "__main__":
    print("1. List all books")
    print("2. Search books")
    print("3. Get member details")
    choice = input("Enter choice (1-3): ").strip()
    if choice == "1":
        books = list_books()
        for book in books:
            print(book)
    elif choice == "2":
        keyword = input("Enter search keyword: ").strip()
        results = search_books(keyword)
        for book in results:
            print(book)
    elif choice == "3":
        member_id = int(input("Enter member ID: ").strip())
        details = get_member_details(member_id)
        print("Member Info:", details["member"])
        print("Borrowed Books:", details["borrowed_books"])
    else:
        print("Invalid choice.")