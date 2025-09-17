import os
from supabase import create_client, Client # pip install supabase
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv()
url: str = os.getenv("supabase_url")
key: str = os.getenv("supabase_key")
sb: Client = create_client(url, key)

def add_member(name, email, join_date):
    payload = {"name": name, "email": email, "join_date": join_date}
    resp = sb.table("members").insert(payload).execute()
    return resp.data

if __name__ == "__main__":
    name = input("Enter member name: ").strip()
    email = input("Enter member email: ").strip()
    date_of_membership = input("Enter date of membership (YYYY-MM-DD): ").strip()
 
    created_member = add_member(name, email, date_of_membership)
    print("Inserted Member:", created_member)