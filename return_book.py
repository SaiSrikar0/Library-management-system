'''When a member returns a book:
	1. Update the borrow_records.return_date.
	2. Increase book stock by 1.
👉 Again, both must happen in a single transaction.
'''

import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timezone
load_dotenv()
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def return_book(record_id):
    # Return a borrowed book
    # Step 1: Get borrow record
    borrow = sb.table("borrow_records").select("*").eq("record_id", record_id).execute()
    if not borrow.data:
        return {"error": "Borrow record not found"}

    record = borrow.data[0]
    if record["return_date"]:
        return {"error": "Book already returned"}

    book_id = record["book_id"]

    # Step 2: Update return_date
    sb.table("borrow_records").update({"return_date": datetime.now(timezone.utc).isoformat()}).eq("record_id", record_id).execute()

    # Step 3: Increase stock
    book = sb.table("books").select("stock").eq("book_id", book_id).execute()
    stock = book.data[0]["stock"]
    sb.table("books").update({"stock": stock + 1}).eq("book_id", book_id).execute()

    return {"success": "Book returned successfully"}

# ---------------- MAIN ----------------
if __name__ == "__main__":
    record_id = int(input("Enter Borrow Record ID: "))
    print(return_book(record_id))