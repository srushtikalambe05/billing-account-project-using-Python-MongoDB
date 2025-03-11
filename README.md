# Clothing Store Billing System with MongoDB

## 📜 Overview
This project is a **Clothing Store Billing System** developed using **Python (Tkinter)** for the GUI and **MongoDB** for storing billing data. The system allows users to add clothing items to a cart, generate a bill, and store the billing details in a MongoDB database.

The GUI provides an easy-to-use interface where customers can select items, add them to the cart, and generate a bill. The generated bill is also stored in a MongoDB database for record-keeping.

---

## 💻 Technologies Used
- **Python 3.11+**
- **Tkinter** for GUI development.
- **MongoDB** for database management.
- **Pymongo** to connect MongoDB with Python.

---

## 📊 Features
- ✅ **Add items to cart**: Allows users to add clothing items to the cart with price details.
- ✅ **Generate Bill**: Provides a detailed bill of items added to the cart along with the total price.
- ✅ **Store Data in MongoDB**: Saves the bill and item details in MongoDB.
- ✅ **User-Friendly GUI**: Built with Tkinter for an intuitive interface.

---

## 📂 Project Structure
```
Clothing-Store-Billing-System
│
├── Untitled5.py                   # Python code for the GUI and MongoDB connectivity
├── ASSIGNMENT mongodb.docx        # Assignment documentation
├── README.md                      # Project documentation
```

---

## 📜 Setup and Installation
### Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/Clothing-Store-Billing-System.git
```

### Navigate to the Project Folder
```bash
cd Clothing-Store-Billing-System
```

### Install Required Libraries
```bash
pip install pymongo
tkinter
```

### Start MongoDB Server
Make sure your MongoDB server is running locally.
```bash
mongod
```

### Run the Python Script
Run the Python script to launch the GUI.
```bash
python Untitled5.py
```

---

## 💾 Database Details
- **Database Name**: `cloths_database`
- **Collection Name**: `accounts`
- **Stored Data Format**:
```json
{
  "items": [
    {"name": "tshirt", "price": 500},
    {"name": "jeans", "price": 1500}
  ],
  "total": 2000
}
```

---

## 🎉 Usage
1. Run the Python script.
2. Click **Add Items to Cart** and select items.
3. Once done, click **Proceed To Bill**.
4. The bill will be generated and saved to MongoDB.
5. Verify the bill in MongoDB under the `accounts` collection.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

