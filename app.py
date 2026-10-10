from flask import Flask, render_template, request, jsonify
import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

CSV_FILE = "finance_data.csv"
COLUMNS = ["date", "amount", "category", "description"]
FORMAT = "%d-%m-%Y"


def initialize_csv():
    try:
        pd.read_csv(CSV_FILE)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(CSV_FILE, index=False)


def add_entry(date, amount, category, description):
    new_entry = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    with open(CSV_FILE, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=COLUMNS)
        writer.writerow(new_entry)


def get_transactions(start_date, end_date):
    df = pd.read_csv(CSV_FILE)
    df["date"] = pd.to_datetime(df["date"], format=FORMAT)
    start_date = datetime.strptime(start_date, FORMAT)
    end_date = datetime.strptime(end_date, FORMAT)
    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    filtered_df = df.loc[mask]
    
    if not filtered_df.empty:
        filtered_df = filtered_df.sort_values("date", ascending=False)
        filtered_df["date"] = filtered_df["date"].dt.strftime(FORMAT)
    
    return filtered_df.to_dict(orient="records")


def get_summary(start_date, end_date):
    df = pd.read_csv(CSV_FILE)
    df["date"] = pd.to_datetime(df["date"], format=FORMAT)
    start_date = datetime.strptime(start_date, FORMAT)
    end_date = datetime.strptime(end_date, FORMAT)
    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    filtered_df = df.loc[mask]
    
    if filtered_df.empty:
        return {"total_income": 0, "total_expense": 0, "net_balance": 0}
    
    total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
    total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
    
    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "net_balance": float(total_income - total_expense)
    }


def create_plot(start_date, end_date):
    df = pd.read_csv(CSV_FILE)
    df["date"] = pd.to_datetime(df["date"], format=FORMAT)
    start_date = datetime.strptime(start_date, FORMAT)
    end_date = datetime.strptime(end_date, FORMAT)
    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    filtered_df = df.loc[mask].copy()
    
    if filtered_df.empty:
        return None
    
    filtered_df.set_index("date", inplace=True)
    income_df = filtered_df[filtered_df["category"] == "Income"].resample("D").sum().reindex(filtered_df.index, fill_value=0)
    expense_df = filtered_df[filtered_df["category"] == "Expense"].resample("D").sum().reindex(filtered_df.index, fill_value=0)
    
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="blue")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="red")
    plt.xlabel("Date")
    plt.ylabel("Amount (₹)")
    plt.title("Income and Expense Over Time")
    plt.legend()
    plt.grid(True)
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url


@app.route('/')
def index():
    initialize_csv()
    return render_template('index.html', today_date=datetime.today().strftime(FORMAT))


@app.route('/api/transactions', methods=['GET'])
def api_get_transactions():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not start_date or not end_date:
        return jsonify({"error": "Please provide start_date and end_date"}), 400
    
    transactions = get_transactions(start_date, end_date)
    return jsonify(transactions)


@app.route('/api/summary', methods=['GET'])
def api_get_summary():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not start_date or not end_date:
        return jsonify({"error": "Please provide start_date and end_date"}), 400
    
    summary = get_summary(start_date, end_date)
    return jsonify(summary)


@app.route('/api/plot', methods=['GET'])
def api_get_plot():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    if not start_date or not end_date:
        return jsonify({"error": "Please provide start_date and end_date"}), 400
    
    plot_url = create_plot(start_date, end_date)
    if plot_url:
        return jsonify({"plot_url": plot_url})
    else:
        return jsonify({"error": "No data to plot"}), 404


@app.route('/api/add', methods=['POST'])
def api_add_transaction():
    data = request.json
    date = data.get('date')
    amount = data.get('amount')
    category = data.get('category')
    description = data.get('description', '')
    
    if not date or not amount or not category:
        return jsonify({"error": "Please provide date, amount, and category"}), 400
    
    try:
        amount = float(amount)
        if amount <= 0:
            return jsonify({"error": "Amount must be positive"}), 400
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400
    
    add_entry(date, amount, category, description)
    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(debug=True)
