// Add Transaction Form Handler
document.getElementById('addTransactionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const date = document.getElementById('date').value;
    const amount = document.getElementById('amount').value;
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;
    
    try {
        const response = await fetch('/api/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ date, amount, category, description })
        });
        
        const data = await response.json();
        
        if (data.success) {
            showNotification('Transaction added successfully!', 'success');
            document.getElementById('addTransactionForm').reset();
            document.getElementById('date').value = new Date().toLocaleDateString('en-GB').replace(/\//g, '-');
        } else {
            showNotification(data.error || 'Failed to add transaction', 'error');
        }
    } catch (error) {
        showNotification('Error adding transaction', 'error');
    }
});

// View Transactions Button Handler
document.getElementById('viewTransactions').addEventListener('click', async () => {
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    
    if (!startDate || !endDate) {
        showNotification('Please enter both start and end dates', 'error');
        return;
    }
    
    // Validate date format
    const dateRegex = /^\d{2}-\d{2}-\d{4}$/;
    if (!dateRegex.test(startDate) || !dateRegex.test(endDate)) {
        showNotification('Please use DD-MM-YYYY format', 'error');
        return;
    }
    
    try {
        // Fetch transactions
        const transactionsResponse = await fetch(`/api/transactions?start_date=${startDate}&end_date=${endDate}`);
        const transactions = await transactionsResponse.json();
        
        // Fetch summary
        const summaryResponse = await fetch(`/api/summary?start_date=${startDate}&end_date=${endDate}`);
        const summary = await summaryResponse.json();
        
        // Display summary
        document.getElementById('totalIncome').textContent = `₹${summary.total_income.toFixed(2)}`;
        document.getElementById('totalExpense').textContent = `₹${summary.total_expense.toFixed(2)}`;
        document.getElementById('netBalance').textContent = `₹${summary.net_balance.toFixed(2)}`;
        document.getElementById('summarySection').style.display = 'grid';
        
        // Display transactions
        const tbody = document.getElementById('transactionsBody');
        tbody.innerHTML = '';
        
        if (transactions.length === 0) {
            tbody.innerHTML = '<tr><td colspan="4" style="text-align: center;">No transactions found</td></tr>';
        } else {
            transactions.forEach(transaction => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${transaction.date}</td>
                    <td>₹${parseFloat(transaction.amount).toFixed(2)}</td>
                    <td class="category-${transaction.category}">${transaction.category}</td>
                    <td>${transaction.description || '-'}</td>
                `;
                tbody.appendChild(row);
            });
        }
        
        document.getElementById('transactionsSection').style.display = 'block';
        document.getElementById('plotSection').style.display = 'none';
        
        showNotification('Transactions loaded successfully!', 'success');
    } catch (error) {
        showNotification('Error loading transactions', 'error');
    }
});

// Show Plot Button Handler
document.getElementById('showPlot').addEventListener('click', async () => {
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    
    try {
        const response = await fetch(`/api/plot?start_date=${startDate}&end_date=${endDate}`);
        const data = await response.json();
        
        if (data.plot_url) {
            document.getElementById('plotImage').src = `data:image/png;base64,${data.plot_url}`;
            document.getElementById('plotSection').style.display = 'block';
            showNotification('Plot generated successfully!', 'success');
        } else {
            showNotification(data.error || 'No data to plot', 'error');
        }
    } catch (error) {
        showNotification('Error generating plot', 'error');
    }
});

// Notification Function
function showNotification(message, type) {
    const notification = document.getElementById('notification');
    notification.textContent = message;
    notification.className = `notification ${type}`;
    notification.classList.add('show');
    
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

// Set default date format on page load
document.addEventListener('DOMContentLoaded', () => {
    const today = new Date();
    const formattedDate = today.toLocaleDateString('en-GB').replace(/\//g, '-');
    document.getElementById('date').value = formattedDate;
});
