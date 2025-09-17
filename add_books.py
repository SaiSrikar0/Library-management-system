import os
from supabase import create_client, Client # pip install supabase
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv()
url: str = os.getenv("supabase_url")
key: str = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def add_book(title, author, category, stock):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data
if __name__ == "__main__":
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    category = input("Enter book category: ").strip()
    stock = int(input("Enter book stock: ").strip())
 
    created_book = add_book(title, author, category, stock)
    print("Inserted Book:", created_book)