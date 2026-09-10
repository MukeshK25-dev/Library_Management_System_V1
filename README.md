# 📚 Library Management System (Version 1)

A simple command-line Library Management System developed using **Python** and **MySQL**. This project demonstrates CRUD (Create, Read, Update, Delete) operations, database connectivity, and a menu-driven interface.

> This is the **initial version** of the project — a straightforward, single-layer implementation. A refactored, more modular version with a layered service-oriented structure is available at [Library_Management_System_V2](https://github.com/MukeshK25-dev/Library_Management_System_V2).

---

## Why this version is still public

This isn't left here by accident. V1 is the first pass — one script per
operation, direct database calls, no service layer. [V2](https://github.com/MukeshK25-dev/Library_Management_System_V2)
is a deliberate rebuild of the same project into a layered architecture
(`config` / `database` / `models` / `services` / `utils`). Keeping both
public shows the actual refactor, not just the end state — V1 is the
"before," V2 is the "after."

---

## 🚀 Features

* Add a new book
* View all books
* Search a book by Book ID
* Update book quantity
* Delete a book
* Menu-driven interface
* MySQL database integration

---

## 🛠️ Technologies Used

* Python 3
* MySQL
* mysql-connector-python

---

## 📂 Project Structure

```text
Library_Management_System_V1/
│
├── database/
│   ├── db_connect.py
│   ├── create_database.py
│   ├── create_table.py
│   ├── add_book.py
│   ├── view_books.py
│   ├── search_book.py
│   ├── update_book.py
│   └── delete_book.py
│
├── .env.example
└── main.py
```

---

## ⚙️ Installation

1. Clone the repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure MySQL credentials:

```bash
cp .env.example .env
# then edit .env and set DB_PASSWORD (and DB_HOST/DB_USER/DB_DATABASE if
# your setup differs from the defaults)
```

4. Create the database:

```bash
python database/create_database.py
```

5. Create the tables:

```bash
python database/create_table.py
```

6. Run the application:

```bash
python main.py
```

---

## 📸 Features Demonstrated

* CRUD Operations
* Python Functions
* Modular Programming
* MySQL Database Connectivity
* Error Handling
* User Input Validation
* Environment-based configuration (no hardcoded credentials)

---

## 🔮 Future Improvements

* Login System
* Book Issue & Return
* Student Management
* Fine Calculation
* GUI using Tkinter or PyQt
* Web Version using Flask or Django

---

## 📝 License
MIT — see [LICENSE](./LICENSE).

## 👨‍💻 Author

Mukesh K

B.Tech Information Technology

Python & MySQL Learning Project
