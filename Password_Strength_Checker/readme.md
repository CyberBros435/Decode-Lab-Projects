# 🔒 Password Security Checker (Python CLI)

![Python](https://img.shields.io/badge/Language-Python-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)
![Security](https://img.shields.io/badge/Cybersecurity-Password_Security-red)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)

A Python command-line application that analyzes password strength using multiple security checks, including **password length**, **character diversity**, and **common password detection**. The tool provides a detailed breakdown of the password's security characteristics and classifies it as **Weak**, **Medium**, or **Strong**.

> **Note:** This project is designed for **educational purposes** to demonstrate password security concepts and rule-based password analysis.

---

# 📖 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Evaluation Workflow](#-evaluation-workflow)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Output](#-example-output)
- [Strength Evaluation Rules](#-strength-evaluation-rules)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Concepts Demonstrated](#-concepts-demonstrated)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Skills Demonstrated](#-skills-demonstrated)
- [Author](#-author)

---

# 🎯 Project Overview

| Item | Description |
|------|-------------|
| Project | Password Security Checker |
| Category | Password Security |
| Language | Python 3 |
| Interface | Command-Line Interface (CLI) |
| Evaluation Method | Rule-Based Password Analysis |
| Output | Weak / Medium / Strong |
| Status | Completed |

---

# 🎯 Objectives

The objectives of this project are to:

- Evaluate password strength using security best practices.
- Detect commonly used and insecure passwords.
- Check password length requirements.
- Verify character diversity.
- Demonstrate password validation logic using Python.
- Learn secure password creation principles.

---

# ✨ Features

- Password strength evaluation.
- Common password detection.
- Password length validation.
- Uppercase letter detection.
- Lowercase letter detection.
- Numeric digit detection.
- Special character detection.
- Colorized terminal output.
- ASCII banner using **PyFiglet**.
- Detailed password analysis report.
- Continuous password checking until user exits.

---

# ⚙️ How It Works

The application evaluates passwords through multiple validation stages.

## 1. User Input

The user enters a password.

```text
Enter Your Password

Str0ng!Password
```

The user can exit the application by entering:

```text
0
```

---

## 2. Common Password Detection

The entered password is first compared against a predefined list of commonly used passwords.

Example blocked passwords:

```text
password

password123

admin

admin123

123456

qwerty
```

If a match is found, the password is immediately classified as **Weak**, regardless of its complexity.

---

## 3. Password Analysis

If the password is not found in the common-password list, the application evaluates:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special symbols

Character detection is performed using Python's `any()` function and regular expressions.

---

## 4. Strength Classification

Based on the evaluation results, the password is categorized as:

```text
Weak

Medium

Strong
```

A detailed breakdown of every detected property is displayed.

---

# 🔄 Evaluation Workflow

```text
User Input
      │
      ▼
Common Password Check
      │
      ▼
Length Validation
      │
      ▼
Uppercase Check
      │
      ▼
Lowercase Check
      │
      ▼
Digit Check
      │
      ▼
Special Character Check
      │
      ▼
Strength Classification
      │
      ▼
Display Detailed Report
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/CyberBros435/<repository-name>.git
```

Navigate to the project folder

```bash
cd <repository-name>
```

Install dependencies

```bash
pip install colorama pyfiglet
```

---

# ▶️ Usage

Run the application

```bash
python Password_Security_checker.py
```

The application will:

- Prompt for a password.
- Evaluate password security.
- Display a detailed analysis.
- Continue accepting passwords until the user enters:

```text
0
```

---

# 🖥️ Example Output

```text
======================================

Password Security Checker

======================================

Enter Your Password (0 -> Exit)

Str0ng!Passw0rd

Password Strength

Strong

Password Details

Length                  : 15

Uppercase Letters       : True

Lowercase Letters       : True

Digits                  : True

Special Symbols         : True
```

---

# 📊 Strength Evaluation Rules

| Strength | Criteria |
|----------|----------|
| **Weak** | Password matches a common password or contains fewer than 6 characters |
| **Medium** | Password meets some security requirements but not all |
| **Strong** | Password is at least 12 characters long and contains uppercase, lowercase, numbers, and special symbols |

---

# 📂 Project Structure

```text
Password-Security-Checker/
│
├── Password_Security_checker.py
├── README.md
└── LICENSE
```

---

# 📦 Requirements

| Dependency | Purpose |
|------------|---------|
| Python 3.x | Programming Language |
| colorama | Colored Terminal Output |
| pyfiglet | ASCII Banner Generation |

Install dependencies

```bash
pip install colorama pyfiglet
```

---

# 📚 Concepts Demonstrated

This project demonstrates the following cybersecurity and programming concepts:

- Password Security Fundamentals
- Rule-Based Password Analysis
- Common Password Detection
- Character Diversity Validation
- Regular Expressions (Regex)
- Python `any()` Function
- Conditional Logic
- Command-Line Interface (CLI)
- Object-Oriented Programming (OOP)
- Secure Password Best Practices

---

# ⚠️ Limitations

This project is intended for educational purposes and has several limitations.

- Uses a small hardcoded common-password list.
- Does not calculate password entropy.
- Does not estimate resistance against brute-force attacks.
- Does not integrate with breached-password databases.
- Rule-based evaluation only.
- Pattern-based passwords (e.g., `Password123!`) may still receive a high score despite being predictable.
- Does not analyze keyboard patterns or repeated sequences.

---

# 🚀 Future Improvements

Potential enhancements include:

- Integrate the **Have I Been Pwned** API.
- Add entropy-based password scoring.
- Estimate brute-force cracking time.
- Detect repeated characters and keyboard patterns.
- Support batch password auditing from files.
- Export password audit reports.
- Add password generation functionality.
- Build a graphical user interface (GUI).
- Create a web-based version using Flask or Django.

---

# 💡 Skills Demonstrated

- Python Programming
- Cybersecurity Fundamentals
- Password Security
- Secure Authentication Concepts
- Input Validation
- Regular Expressions
- Rule-Based Security Analysis
- CLI Application Development
- Object-Oriented Programming
- Software Documentation

---

# 👨‍💻 Author

**Mudasir Zia**

**GitHub:**  
https://github.com/CyberBros435

---

⭐ If you found this project useful, consider giving the repository a **Star**.