import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from collections import Counter

# Load Supabase
load_dotenv()
url = os.getenv("supabase_url")
key = os.getenv("supabase_key")
sb: Client = create_client(url, key)

# 1. Top 5 most borrowed books
def top_5_books():
    resp = (
        sb.table("borrow_records")
        .select("book_id, books(title)")   # book_id + join to books
        .execute()
    )
    titles = [r["books"]["title"] for r in resp.data if r.get("books")]
    return Counter(titles).most_common(5)


# 2. Members with overdue books (>14 days)
def overdue_members():
    cutoff = (datetime.now(timezone.utc) - timedelta(days=14)).isoformat()

    resp = (
        sb.table("borrow_records")
        .select("member_id, members(name,email), books(title), borrow_date")
        .is_("return_date", None)          # None is better than "null"
        .lt("borrow_date", cutoff)         # Borrowed before cutoff
        .execute()
    )
    return resp.data


# 3. Total books borrowed per member
def books_per_member():
    resp = (
        sb.table("borrow_records")
        .select("member_id, members(name)")   # join with members
        .execute()
    )
    names = [r["members"]["name"] for r in resp.data if r.get("members")]
    return Counter(names).most_common()


# --------- Main ---------
if __name__ == "__main__":
    print(" Top 5 Borrowed Books:", top_5_books())
    print(" Overdue Members:", overdue_members())
    print(" Books Per Member:", books_per_member())
