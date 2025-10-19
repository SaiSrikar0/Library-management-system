import streamlit as st
from datetime import datetime

# Import project functions
from add_books import add_book
from add_members import add_member
from borrow import borrow_book
from return_book import return_book
from read_book import list_books, search_books, get_member_details
from update import update_book_stock, update_member_info
from delete import delete_book, delete_member
from report import top_5_books, overdue_members, books_per_member

st.set_page_config(page_title="Library Management", layout="centered")

st.title("Library Management System")

menu = st.sidebar.selectbox("Choose action", [
    "Home",
    "Add Book",
    "Add Member",
    "List/Search Books",
    "Member Details",
    "Borrow Book",
    "Return Book",
    "Update",
    "Delete",
    "Reports",
])

def show_home():
    st.write("Use the sidebar to navigate the library operations.")

def show_add_book():
    st.header("Add Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    category = st.text_input("Category")
    stock = st.number_input("Stock", min_value=0, value=1, step=1)
    if st.button("Add Book"):
        resp = add_book(title, author, category, int(stock))
        st.success(f"Inserted: {resp}")

def show_add_member():
    st.header("Add Member")
    name = st.text_input("Name")
    email = st.text_input("Email")
    join_date = st.date_input("Join Date", value=datetime.now().date())
    if st.button("Add Member"):
        resp = add_member(name, email, join_date.isoformat())
        st.success(f"Inserted: {resp}")

def show_list_search_books():
    st.header("Books")
    q = st.text_input("Search (title/author/category)")
    if q:
        results = search_books(q)
        st.write(f"Found {len(results)} books")
        for b in results:
            st.json(b)
    else:
        books = list_books()
        st.write(f"Total books: {len(books)}")
        for b in books:
            st.json(b)

def show_member_details():
    st.header("Member Details")
    member_id = st.number_input("Member ID", min_value=1, step=1)
    if st.button("Get Details"):
        details = get_member_details(int(member_id))
        st.json(details)

def show_borrow():
    st.header("Borrow Book")
    member_id = st.number_input("Member ID", min_value=1, step=1, key="bmid")
    book_id = st.number_input("Book ID", min_value=1, step=1, key="bbid")
    if st.button("Borrow"):
        borrow_book(int(member_id), int(book_id))
        st.success("Borrow attempted (check logs for details)")

def show_return():
    st.header("Return Book")
    record_id = st.number_input("Borrow Record ID", min_value=1, step=1)
    if st.button("Return"):
        resp = return_book(int(record_id))
        st.json(resp)

def show_update():
    st.header("Update")
    choice = st.selectbox("Update", ["Book Stock", "Member Email"]) 
    if choice == "Book Stock":
        book_id = st.number_input("Book ID", min_value=1, step=1, key="ubid")
        stock = st.number_input("New Stock", min_value=0, step=1, key="ustock")
        if st.button("Update Stock"):
            resp = update_book_stock(int(book_id), int(stock))
            st.success(f"Updated: {resp}")
    else:
        member_id = st.number_input("Member ID", min_value=1, step=1, key="umid")
        email = st.text_input("New Email", key="uemail")
        if st.button("Update Email"):
            resp = update_member_info(int(member_id), email)
            st.success(f"Updated: {resp}")

def show_delete():
    st.header("Delete")
    choice = st.selectbox("Delete", ["Book", "Member"]) 
    if choice == "Book":
        book_id = st.number_input("Book ID", min_value=1, step=1, key="dbid")
        if st.button("Delete Book"):
            resp = delete_book(int(book_id))
            st.success(f"Deleted: {resp}")
    else:
        member_id = st.number_input("Member ID", min_value=1, step=1, key="dmid")
        if st.button("Delete Member"):
            resp = delete_member(int(member_id))
            st.success(f"Deleted: {resp}")

def show_reports():
    st.header("Reports")
    st.subheader("Top 5 Borrowed Books")
    st.write(top_5_books())
    st.subheader("Overdue Members")
    st.json(overdue_members())
    st.subheader("Books Per Member")
    st.write(books_per_member())

page_map = {
    "Home": show_home,
    "Add Book": show_add_book,
    "Add Member": show_add_member,
    "List/Search Books": show_list_search_books,
    "Member Details": show_member_details,
    "Borrow Book": show_borrow,
    "Return Book": show_return,
    "Update": show_update,
    "Delete": show_delete,
    "Reports": show_reports,
}

page_map[menu]()
