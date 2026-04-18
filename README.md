# 💸 Expense Tracker Pro

> A sleek and powerful desktop expense management application built with **Python**, **Tkinter**, **SQLite**, and **Matplotlib** to help users track spending, organize transactions, and visualize financial habits.

---

## 📋 Table of Contents

- [Features](#-features)
- [Built With](#-built-with)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [How to Use](#-how-to-use)
- [Default Categories](#-default-categories)
- [Dashboard](#-dashboard-includes)
- [Database Storage](#-database-storage)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 💰 Expense Management
- Add new expenses instantly
- Update existing transactions
- Delete selected records
- Refresh transaction list

### 🔍 Smart Search & Filters
- Search by description
- Filter by category
- Quickly find old transactions

### 📊 Reports & Dashboard
- View spending charts
- Category-wise breakdown
- Expense trend visualization
- Running total tracker

### 💾 Storage
- Local SQLite database
- Fast and lightweight
- No internet required

### 🎨 User Interface
- Modern dark theme
- Clean desktop layout
- Easy-to-use controls

---

## 🛠️ Built With

| Technology  | Role                      |
|-------------|---------------------------|
| Python      | Main programming language |
| Tkinter     | GUI framework             |
| SQLite      | Local database            |
| Matplotlib  | Charts & analytics        |

---

## 📁 Project Structure

```
expense-tracker/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── core/
│   ├── models.py
│   ├── storage.py
│   └── reports.py
│
├── ui/
│   ├── app.py
│   └── charts.py
│
├── assets/
│   └── preview.png
│
└── data/
    └── expenses.db
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/expense-tracker.git
```

### 2️⃣ Move Into Project Folder
```bash
cd expense-tracker
```

### 3️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 4️⃣ Activate Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 5️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Run Application
```bash
python main.py
```

---

## 🧾 How to Use

### ➕ Add Expense
Enter the following, then click **Add**:
- Amount
- Category
- Description

### ✏️ Update Expense
Select any row → Modify values → Click **Update**

### 🗑️ Delete Expense
Select a row → Click **Delete**

### 🔍 Search Expense
Type in the search box to filter results instantly.

### 📊 Open Dashboard
Click **Dashboard** to see charts and reports.

---

## 📂 Default Categories

| Category         | Category        |
|------------------|-----------------|
| 🍔 Food          | 🚗 Transport    |
| 🛍️ Shopping     | 💡 Bills        |
| 🎬 Entertainment | 💊 Health       |
| 📚 Education     | 📦 Other        |

---

## 📊 Dashboard Includes

- Pie chart by category
- Monthly expense trends
- Total spending summary
- Transaction insights

---

## 💾 Database Storage

All records are stored locally inside:

```
data/expenses.db
```

No cloud, no accounts — your data stays on your machine.

---

## 🔮 Future Enhancements

- [ ] CSV / Excel export
- [ ] Monthly budget planning
- [ ] Recurring expense reminders
- [ ] Dark / Light theme switcher
- [ ] Multi-user accounts
- [ ] Cloud sync
- [ ] AI expense insights

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 🐞 Found a Bug?

Open an issue and include:
- Bug details
- Screenshot
- Steps to reproduce

---

## 📜 License

Licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Built with ❤️ using Python · Tkinter · SQLite · Matplotlib</p>