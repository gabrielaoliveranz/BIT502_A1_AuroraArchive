# ✨ The Aurora Archive - BIT502 Assessment 1 ✨

![Python](https://img.shields.io/badge/Python-3-blue?logo=python&logoColor=white)
![NZ English](https://img.shields.io/badge/Language-NZ%20English-brightgreen)

**File:** `BIT502_AS1_Gabriela_Olivera.py`  
**Author:** Gabriela Olivera  
**Course:** BIT502 – Programming Fundamentals  
**Date:** 2025  

---

## 📝 Overview

The **Aurora Archive** is a **Python console application** simulating a library management system. Users can:

- Explore **membership plans**
- Select **optional extras**
- Participate in a **Kids' Reading Challenge**
- Calculate book rental costs for **Aurora-Picks items**

The application emphasises **user experience**, **input validation**, and **clear navigation**.

---

## 🚀 Features

### 1️⃣ Main Menu
- Central navigation for all sections.  
- Sections included: **Membership Plans**, **Optional Extras**, **Kids' Reading Challenge**, **Aurora-Picks Rental Calculator**.  
- Includes **input validation** and **clean prompts**.

### 2️⃣ Membership Plans (`membership_plans`)
- Available plans: **Standard**, **Premium**, **Kids**  
- Select **duration**: monthly or annual (**annual includes one month free**)  
- Calculates and displays **total cost**

### 3️⃣ Optional Extras (`optional_extras`)
- Additional services:  
  - 📖 **Book rental**  
  - 🛋️ **Private area access**  
  - 📔 **Monthly booklet**  
  - 💻 **Online ebook rental**  
- Provides **detailed descriptions**  
- Calculates **total monthly cost**  
- Includes **yes/no input validation**

### 4️⃣ Kids' Reading Challenge (`reading_challenge`)
- Record pages read **Monday–Friday**  
- Calculates:
  - **Total pages**
  - **Average pages per day**
  - **User ranking**:
    - 🥉 Bronze (≤25 pages)  
    - 🥈 Silver (26–50 pages)  
    - 🥇 Gold (51–100 pages)  
    - 🏆 Platinum (>100 pages)
- Highlights **day(s) with most pages**  
- Indicates **pages needed for next rank**  
- Celebrates if **weekly record (150 pages) is broken**  
- Displays **graphical bar charts** for visualisation

### 5️⃣ Aurora-Picks Rental Calculator (`rental_calculator`)
- Calculates rental cost for hand-picked books  
- **Tiered pricing**:
  - Days 1–3: $1/day  
  - Days 4–8: $0.80/day  
  - Days 9–21: $0.50/day  
- **Maximum rental (21 days)**: fixed cost $12  
- Validates **minimum/maximum days** and ensures **integer input**

### 6️⃣ Utility Function (`clear_console`)
- Clears the terminal for a cleaner, **user-friendly interface**  
- Works across **Windows and Unix-based systems**

---

## 🖥️ Usage

Run the script using Python 3:

```bash
python BIT502_AS1_Gabriela_Olivera.py##

Navigate the main menu by entering numbers 1–5.  

Follow prompts for each section:

1. Choose membership plans and duration  
2. Select optional extras  
3. Enter pages read for the reading challenge  
4. Enter rental period for Aurora-Picks books  
5. Press Enter to return to previous menus or exit

---

## 📸 Screenshots

### Main Menu
![Main Menu](screenshots/01_main_menu.png)

### Membership Plans
![Membership Plan Selection](screenshots/02a_membership_plan_selection.png)
![Membership Plan Details](screenshots/02b_membership_plan_selection.png)

### Optional Extras
![Optional Extras Selection](screenshots/03a_optional_extras_selection.png)
![Optional Extras Calculation](screenshots/03b_optional_extras_selection.png)

### Kids' Reading Challenge
![Reading Challenge Input](screenshots/04a_reading_challenge_input.png)
![Reading Challenge Results](screenshots/04b_reading_challenge_input.png)

### Aurora-Picks Rental Calculator
![Rental Calculator Valid Input](screenshots/06a_rental_calculator_valid.png)
![Rental Calculator Result](screenshots/06b_rental_calculator_valid.png)
![Rental Calculator Error Handling](screenshots/07_rental_calculator_error.png)

### Exit Message
![Exit Message](screenshots/08_exit_message.png)

---

## ⚙️ Technical Details

- Written in **Python 3** using standard libraries: `os`, `time`, `sys`, `textwrap`  
- **ANSI escape codes** used for terminal colours and emphasis  
- **Emoji-based enhancements** for engaging interface  
- Robust **input validation** prevents crashes  
- **Modular design**:
  - Membership plans, extras, and rental prices stored in **dictionaries or lists**  
  - Functions separated by **task** for maintainability

---

## 📝 Notes

- Follows **NZ English** spelling and formatting conventions  
- Designed for **console use**, not GUI deployment  
- Easy to update **prices**, **memberships**, and **ranking thresholds**

---

## 📜 License

This project is for **educational purposes** only and is part of the **BIT502 assessment**  
All rights reserved to the author
