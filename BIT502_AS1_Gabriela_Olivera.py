# Course Code: BIT502
# Assessment: 1
# Name: Gabriela Olivera
# Student ID: 5141369

"""======================== BIT502 Assessment 1 ========================"""

# ---------- Imports ----------
import os
import time
import textwrap

# ---------- Utility Function ----------
def clear_console():
    """Clears the console screen for a clean user interface."""
    time.sleep(0.2)  # Small delay to avoid input stacking
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------- Task 1: Main Menu ----------
def main_menu():
    """Displays the main menu and navigates to each section based on user choice."""
    while True:
        clear_console()
        print("═" * 50)
        print("       ✨ Welcome to The Aurora Archive ✨       ")
        print("═" * 50 + "\n")
        
        print("1️⃣  Membership Plans")
        print("2️⃣  Optional Extras")
        print("3️⃣  Kids' Reading Challenge")
        print("4️⃣  Aurora-Picks Rental Calculator")
        print("5️⃣  Exit the program\n")
        print("─" * 50)
        
        choice = input("➡️ Please enter your choice (1-5): ").strip()
        
        if choice == "1":
            membership_plans()
        elif choice == "2":
            optional_extras()
        elif choice == "3":
            reading_challenge()
        elif choice == "4":
            rental_calculator()
        elif choice == "5":
            clear_console()
            print("💛 Thank you for visiting The Aurora Archive!")
            print("👋 Goodbye!\n")
            break
        else:
            input("\n❌ Invalid option. Please enter a number between 1 and 5.\nPress Enter to try again...")

# ---------- Task 2: Membership Plans ----------
def membership_plans():
    """Displays membership plan options with descriptions and calculates cost."""
    plans = {
        1: {"name": "Standard", "monthly": 10, "description": "Basic membership for general access."},
        2: {"name": "Premium", "monthly": 15, "description": "Access to book discounts and special sales."},
        3: {"name": "Kids", "monthly": 5, "description": "Same as Standard, but only for children 12 or younger."}
    }

    while True:
        clear_console()
        print("📖 === Membership Plans === 📖\n")
        for key, plan in plans.items():
            print(f"{key}. {plan['name']} - 💲{plan['monthly']}/month")
        print("4. Return to Main Menu")
        print("5. Exit Program\n")
        
        choice = input("➡️ Select a plan (1-5): ").strip()

        if choice == "4":
            break
        elif choice == "5":
            clear_console()
            print("💛 Thank you for visiting The Aurora Archive!")
            print("👋 Goodbye!")
            exit()
        elif choice not in ["1", "2", "3"]:
            input("\n❌ Invalid option. Press Enter to try again...")
            continue

        plan_choice = int(choice)
        plan = plans[plan_choice]

        duration = input("⏳ Enter duration (monthly/annual): ").strip().lower()
        if duration not in ["monthly", "annual"]:
            input("\n❌ Invalid duration. Press Enter to try again...")
            continue

        cost = plan["monthly"] if duration == "monthly" else plan["monthly"] * 11

        clear_console()
        print(f"✨ === {plan['name']} Membership === ✨\n")
        print(f"Description: {plan['description']}")
        print(f"Duration: {duration.capitalize()}")
        print(f"Total cost: 💲{cost:.2f}")

        input("\nPress Enter to return to the main menu...")
        break

# ---------- Task 3: Optional Extras ----------
def optional_extras():

    extras = {
        "Book rental": {
            "price": 5,
            "emoji": "📖",
            "description": ("Borrow one book at a time from a select range of older books. "
                            "Returning the book allows another borrow up to twice per month. "
                            "This rental is separate from the Aurora-Picks rental system.")
        },
        "Private area access": {
            "price": 15,
            "emoji": "🛋️",
            "description": ("Access to the second floor quiet reading area with comfortable seating.")
        },
        "Monthly booklet": {
            "price": 2,
            "emoji": "📔",
            "description": ("Monthly booklet covering news, events, reviews, and upcoming releases.")
        },
        "Online ebook rental": {
            "price": 5,
            "emoji": "💻",
            "description": ("Access a selection of ebooks via e-reader. Only one member can borrow each book at a time. "
                            "Books are automatically returned after 7 days.")
        }
    }

    print("📚 === Optional Extras === 📚\n")
    for name, info in extras.items():
        print(f"{info['emoji']}  {name} - 💲{info['price']}/month")
        wrapped = textwrap.fill(info['description'], width=60, initial_indent="    ", subsequent_indent="    ")
        print(wrapped)
        print("─" * 60)

    selections = {}
    for name in extras:
        while True:
            choice = input(f"Would you like {extras[name]['emoji']} {name} for 💲{extras[name]['price']} (yes/no)? ").strip().lower()
            if choice in ["yes", "y"]:
                selections[name] = True
                break
            elif choice in ["no", "n"]:
                selections[name] = False
                break
            else:
                print("❌ Invalid input. Please enter 'yes' or 'no'.")

    total_cost = sum(extras[name]["price"] for name, selected in selections.items() if selected)

    clear_console()
    print("✅ === Your Optional Extras Selection === ✅\n")
    for name, selected in selections.items():
        status = "Selected ✅" if selected else "Not selected ❌"
        print(f"{extras[name]['emoji']} {name}: {status}")
    print(f"\n💲 Total monthly cost for extras: {total_cost:.2f}")

    input("\nPress Enter to return to the main menu...")

# ---------- Task 4: Kids' Reading Challenge ----------
def reading_challenge():

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    clear_console()
    print(f"{BOLD}{CYAN}=== Welcome to the Kids' Reading Challenge ==={RESET}\n")
    print("📚 Please enter the number of pages you read for each weekday (Monday-Friday).")
    print("Hit Enter to start…")
    input()

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    pages_read = {}

    for day in weekdays:
        while True:
            entry = input(f"📖 {day}: ").strip()
            try:
                value = float(entry)
                if value < 0:
                    print(f"{RED}Please enter a positive number of pages.{RESET}")
                    continue
                pages_read[day] = value
                break
            except ValueError:
                print(f"{RED}Invalid input. Please enter a number (integer or decimal).{RESET}")

    total_pages = sum(pages_read.values())
    average_pages = total_pages / len(weekdays)

    if total_pages <= 25:
        rank = "Bronze"
        rank_color = YELLOW
        next_rank_pages = 26 - total_pages
    elif total_pages <= 50:
        rank = "Silver"
        rank_color = "\033[97m"
        next_rank_pages = 51 - total_pages
    elif total_pages <= 100:
        rank = "Gold"
        rank_color = MAGENTA
        next_rank_pages = 101 - total_pages
    else:
        rank = "Platinum"
        rank_color = BLUE
        next_rank_pages = None

    max_pages = max(pages_read.values())
    top_days = [day for day, pages in pages_read.items() if pages == max_pages]

    clear_console()
    print(f"{BOLD}{CYAN}=== Reading Challenge Results ==={RESET}\n")
    
    print(f"📊 Total pages read: {GREEN}{total_pages}{RESET}")
    print(f"📈 Average pages per day: {GREEN}{average_pages:.1f}{RESET}\n")

    print("📅 Pages read per day:")
    max_bar_length = 40
    for day, pages in pages_read.items():
        bar_len = int((pages / max_pages) * max_bar_length) if max_pages > 0 else 0
        bar = "█" * bar_len
        print(f"{day:<10} | {bar} {pages:.1f}")

    print()
    print(f"🏅 You ranked {rank_color}{rank}{RESET}!")
    if len(top_days) == 1:
        print(f"🌟 {top_days[0]} was your biggest reading day!")
    else:
        print(f"🌟 {', '.join(top_days)} were your biggest reading days!")

    if next_rank_pages is not None:
        print(f"➡️ To reach the next rank you need to read {next_rank_pages:.0f} more pages. Good luck!")
    else:
        print(f"🎉 You are already at the highest rank. Congratulations!")

    weekly_record = 150
    if total_pages > weekly_record:
        print(f"\n🏆 {BOLD}{GREEN}Amazing! You've broken the weekly record!{RESET}")

    input("\nPress Enter to return to the main menu...")

# ---------- Task 5: Aurora-Picks Rental Calculator ----------
def rental_calculator():
    clear_console()
    
    prices = [
        (3, 1.00),
        (5, 0.80),
        (13, 0.50)
    ]
    max_days = 21
    min_days = 3
    fixed_max_cost = 12.0

    while True:
        clear_console()
        print("📚 === Aurora-Picks Rental Calculator === 📚\n")
        print("1️⃣  Enter rental period")
        print("2️⃣  Return to main menu\n")
        choice = input("➡️ Enter your selection (1-2): ").strip()
        
        if choice == "1":
            while True:
                try:
                    days = int(input(f"\nEnter number of days to rent a book ({min_days}-{max_days}): ").strip())
                    if days < min_days:
                        print(f"⚠️ Minimum rental period is {min_days} days.")
                        continue
                    if days > max_days:
                        print(f"⚠️ Maximum rental period is {max_days} days.")
                        continue
                    break
                except ValueError:
                    print("❌ Invalid input. Please enter a whole number (integer).")

            if days == max_days:
                total_cost = fixed_max_cost
            else:
                remaining_days = days
                total_cost = 0
                for period_days, price_per_day in prices:
                    d = min(period_days, remaining_days)
                    total_cost += d * price_per_day
                    remaining_days -= d
                    if remaining_days <= 0:
                        break

            clear_console()
            print(f"📚 You are renting for {days} day(s).")
            print(f"💲 Total cost: {total_cost:.2f}")
            input("\nPress Enter to return to the rental menu...")
        
        elif choice == "2":
            break
        else:
            print("❌ Invalid option. Please select 1 or 2.")
            input("Press Enter to try again...")

# ---------- Run Program ----------
if __name__ == "__main__":
    main_menu()