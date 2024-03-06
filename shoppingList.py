import mysql.connector
import tkinter as tk


# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kalisql24",
    database="shoppingList"
)
# create the main window
root = tk.Tk()
root.geometry("400x300")

# Create labels and text boxes for user input
date_label = tk.Label(root, text="Purchase Date (YYYY-MM-DD):")
date_entry = tk.Entry(root)
brand_label = tk.Label(root, text="Brand:")
brand_entry = tk.Entry(root)
item_label = tk.Label(root, text="Item:")
item_entry = tk.Entry(root)
price_label = tk.Label(root, text="Price:")
price_entry = tk.Entry(root)

# Create a button to add the shopping list item to the database
add_button = tk.Button(root, text="Add Item")

# Function to add the shopping list item to the database

def add_item():
    date = date_entry.get()
    brand = brand_entry.get()
    item = item_entry.get()
    price = float(price_entry.get())
    cursor = cnx.cursor()
    query = "INSERT INTO purchases (date,brand,item, price) VALUES (%s, %s,%s,%s)"
    cursor.execute(query, (date, brand,item, price))
    cnx.commit()
    print(f"Successfully added '{item}' to the shopping list.")

 # Clear the input fields
    date_entry.delete(0, tk.END)
    brand_entry.delete(0, tk.END)
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# Bind the "Add Item" button to the add_item() function
add_button.config(command=add_item)

# Layout the widgets in the main window
date_label.grid(row=0, column=0)
date_entry.grid(row=0, column=1)
brand_label.grid(row=1, column=0)
brand_entry.grid(row=1, column=1)
item_label.grid(row=2, column=0)
item_entry.grid(row=2, column=1)
price_label.grid(row=3, column=0)
price_entry.grid(row=3, column=1)
add_button.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
# Close the database connection
cnx.close()
