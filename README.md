# 💰 Personal Finance Tracker

A **Python application** to track your **income and expenses**, visualize cash flow, and get insights into your spending habits.  
Features both a **CLI interface** and a **modern web interface**. Uses **Pandas** for data handling and **Matplotlib** for visualizing trends.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Features
- 💵 Add income and expense transactions with date, amount, category, and optional description  
- 📊 View transactions within a specific date range  
- 📈 Monthly Income vs Expense plot to visualize cash flow  
- 🧾 Overall summary: total income, total expense, and net balance  
- 🗄️ CSV Data Safety: automatically initializes CSV if missing or empty
- 🌐 **NEW: Modern Web Interface** - Beautiful UI with real-time data visualization  

---

## 🗂️ Project Structure
FinanceTracker/
│
├── main.py           # CLI application logic  
├── app.py            # Web application (Flask)  
├── data_entry.py     # Functions for user input  
├── finance_data.csv  # CSV file storing transactions  
├── templates/        # HTML templates for web interface
│   └── index.html    # Main web page
├── static/           # Static assets for web interface
│   ├── style.css     # Styling
│   └── script.js     # JavaScript functionality
├── README.md         # Project description  
├── requirements.txt  # Dependencies  
└── venv/             # Python virtual environment (optional)  

---

## 🧠 How to Run

### Option 1: Using the Web Interface (Recommended)

1. **Clone the repository**

```bash
git clone https://github.com/Its-PrashantTechie/FinanceTracker.git
cd FinanceTracker
```

2. **Create a Python virtual environment (recommended)**

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # Linux/macOS
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask web application**

```bash
python app.py
```

5. **Open your browser**

Navigate to `http://127.0.0.1:5000` to access the web interface.

### Option 2: Using the CLI Interface

Follow steps 1-3 above, then run:

```bash
python main.py
```

Follow the menu to add transactions, view reports, and plot cash flow.

---

## � Web Interface Features

The modern web interface provides:
- 📝 **Add transactions** with a user-friendly form (auto-fills today's date)
- 📊 **View transactions** in a date range with a beautiful, sortable table
- 💳 **Summary cards** showing total income, expenses, and net balance
- 📈 **Interactive charts** for income vs expense visualization
- 🎯 **Real-time notifications** for success/error messages
- 📱 **Responsive design** that works on mobile and desktop
- 🎨 **Beautiful UI** with modern gradient styling

---

## 🧩 Tech Stack

- **Python 3+** – Application logic
- **Pandas** – Data handling and aggregation
- **Matplotlib** – Data visualization
- **Flask** – Web framework for the interface
- **CSV** – Persistent storage
- **HTML/CSS/JavaScript** – Frontend technologies

---

## 🎓 About

This project is a hands-on Python application for managing personal finances. It helps you understand cash flow, spending patterns, and budgeting, while practicing Python, Pandas, Matplotlib, and Flask in a real-world context.

The project demonstrates both traditional CLI-based applications and modern web-based interfaces, making it suitable for learning full-stack Python development.

---

## ✨ Optional Enhancements (Future Work)

- Category-wise monthly expense breakdown
- Monthly savings calculation and goals
- Automatic CSV backup and corruption prevention
- User authentication and multiple user support
- Export data to Excel or PDF reports
- Budget alerts and notifications
- Database integration (SQLite/PostgreSQL) instead of CSV
- Mobile app version using React Native
- Dark mode theme for web interface
- Data visualization with more chart types (pie charts, bar charts)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.
