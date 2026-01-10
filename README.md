# 💰 Personal Finance Tracker (Python CLI App)

A simple **Python CLI application** to track your **income and expenses**, visualize cash flow, and get insights into your spending habits.  
Uses **Pandas** for data handling and **Matplotlib** for visualizing trends.

---

## 🚀 Features
- 💵 Add income and expense transactions with date, amount, category, and optional description  
- 📊 View transactions within a specific date range  
- 📈 Monthly Income vs Expense plot to visualize cash flow  
- 🧾 Overall summary: total income, total expense, and net balance  
- 🗄️ CSV Data Safety: automatically initializes CSV if missing or empty  

---

## 🗂️ Project Structure
FinanceTracker/
│
├── main.py           # Main application logic  
├── data_entry.py     # Functions for user input  
├── finance_data.csv  # CSV file storing transactions  
├── README.md         # Project description  
├── requirements.txt  # Dependencies  
└── venv/             # Python virtual environment (optional)  

---

## 🧠 How to Run
1. **Clone the repository**

```bash
git clone https://github.com/your-username/personal-finance-tracker.git
cd personal-finance-tracker
Create a Python virtual environment (optional but recommended)
```
```bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies
```

```bash
Copy code
pip install -r requirements.txt
# OR
pip install pandas matplotlib
Run the app
```

```bash
Copy code
python main.py
Follow the menu to add transactions, view reports, and plot cash flow.
```

🧩 Tech Stack
Python 3+ – Application logic

Pandas – Data handling and aggregation

Matplotlib – Data visualization

CSV – Persistent storage

CLI – Command-line interface

🎓 About
This project is a hands-on Python project for managing personal finances.
It helps you understand cash flow, spending patterns, and budgeting, while practicing Python, Pandas, and Matplotlib in a real-world context.

✨ Optional Enhancements (Future Work)
Category-wise monthly expense breakdown

Monthly savings calculation

Automatic CSV backup and corruption prevention

Convert to a proper CLI tool with commands using argparse or click
