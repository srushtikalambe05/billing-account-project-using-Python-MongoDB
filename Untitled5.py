#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pymongo')


# In[ ]:


from pymongo import MongoClient
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# MongoDB Connection Setup
client = MongoClient("mongodb://localhost:27017/")
db = client['cloths_database']
collection = db['accounts']

# Global variables to store cart items and total
cart = []
total_amount = 0

# Function to add items to the cart
def add_to_cart(item_name, item_price):
    global total_amount
    cart.append({'name': item_name, 'price': item_price})
    total_amount += item_price
    messagebox.showinfo("Added", f"{item_name} added to cart. Total: ₹{total_amount}")

# Function to generate the bill and store it in MongoDB
def generate_bill():
    if not cart:
        messagebox.showerror("Error", "No items in the cart!")
        return

    # Display bill details
    bill_window = tk.Toplevel()
    bill_window.title("Bill")

    total_label = tk.Label(bill_window, text="Bill Details", font=("Arial", 18))
    total_label.pack()

    for item in cart:
        item_label = tk.Label(bill_window, text=f"{item['name']} - ₹{item['price']}")
        item_label.pack()

    total_label = tk.Label(bill_window, text=f"Total Amount: ₹{total_amount}", font=("Arial", 16))
    total_label.pack()

    # Store the bill in MongoDB
    bill_data = {'items': cart, 'total': total_amount}
    collection.insert_one(bill_data)

    messagebox.showinfo("Bill", "Bill generated and stored in MongoDB successfully!")

# Function to create the items form (Form 1)
def open_items_form():
    items_window = tk.Toplevel()
    items_window.title("Add Items to Cart")

    items = [
        ("tshirt", 500),
        ("jeans", 1500),
        ("shirt", 2500),
        ("jacket", 3500),
        ("socks", 200)
    ]

    label = tk.Label(items_window, text="Select an item to add to the cart", font=("Arial", 14))
    label.pack()

    for item_name, item_price in items:
        button = tk.Button(items_window, text=f"{item_name} - ₹{item_price}", command=lambda i=item_name, p=item_price: add_to_cart(i, p))
        button.pack()

# Main window setup
root = tk.Tk()
root.title("Clothing store")

label = tk.Label(root, text="Clothing store", font=("Arial", 20))
label.pack(pady=10)

add_items_button = tk.Button(root, text="Add Items to Cart", command=open_items_form, font=("Arial", 14))
add_items_button.pack(pady=10)

generate_bill_button = tk.Button(root, text="Proceed To Bill", command=generate_bill, font=("Arial", 14))
generate_bill_button.pack(pady=10)

root.mainloop()


# In[ ]:




