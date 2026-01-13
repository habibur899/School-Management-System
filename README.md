# School Management System (Python)

A simple **School Management System** built using **Python**, focusing on **OOP concepts**, **File Handling**, and **Encapsulation**.
This project stores student data permanently using a text file, so data is not lost even after the program is closed.

---

## Features

-  Object-Oriented Programming (OOP)
-  Student & Course class design
-  File handling using `.txt` file
-  Persistent data storage
-  Encapsulation with private variables
-  Getter method for secure data access

---

##  Technologies Used

- Python 3
- File Handling (`open`, `read`, `write`, `append`)
- OOP (Class, Object, Method)
- Encapsulation (Private variable)

---

##  Project Structure

```
school-management-system/
│
├── school_management.py   # Main Python program
├── students.txt           # Stored student data (auto-created)
└── README.md              # Project documentation
```

---

##  OOP Design

### 🔹 Course Class
- Stores course name
- Uses `__str__()` method for readable output

### 🔹 Student Class
- Stores student name, roll, and enrolled courses
- Uses **private password** (`__password`)
- Uses **getter method** to access password securely

---

##  File Handling

- Student data is stored in `students.txt`
- Data is saved using **append mode**
- Data remains even after program restart

---

##  How to Run the Project

1. Clone the repository
   ```bash
   git clone https://github.com/habibur899/School-Management-System.git
   ```

2. Navigate to the project folder
   ```bash
   cd school-management-system
   ```

3. Run the Python file
   ```bash
   python school_management.py
   ```

---

##  Encapsulation Example

```python
self.__password = password  # Private variable
```

Access using getter method:

```python
def get_password(self):
    return self.__password
```

