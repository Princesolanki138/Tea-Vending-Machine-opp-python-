🫖 Tea Vending Machine (OOP Python Project)
This is a command-line tea vending machine built using Object-Oriented Programming (OOP) principles in Python. It simulates ordering different types of tea, handling payments, tracking resources (ingredients), and managing profits with admin controls.

📂 Features
✅ Order from 3 types of tea:

green_tea

black_tea

milk_tea

✅ Optional sugar (user selects how many teaspoons).
✅ Ingredient sufficiency check.
✅ Coin-based payment simulation using ₹20, ₹10, ₹5, and ₹1 coins.
✅ Inventory refill system.
✅ Admin-only profit reset protected by password.
✅ Clean modular structure using OOP.

🚀 How to Run
1. Clone the repository or download the code
bash
Copy
Edit
git https://github.com/Princesolanki138/Tea-Vending-Machine-opp-python-.git
cd tea-vending-machine
Or download as .zip and extract.

2. Run the main script
bash
Copy
Edit
python main.py
Note: You must have Python 3.x installed.

🧾 Example Usage
text
Copy
Edit
What would you like?: green_tea/black_tea/milk_tea :
> milk_tea

How much sugar do you need? (if No then type 0 else type number of tsp): 
> 2

Please insert coins.
How many ₹20 coin?: 1
How many ₹10 coin?: 0
How many ₹5 coin?: 0
How many ₹1?: 0

Here is ₹5.0 in change.
Here is your milk_tea ☕️. Enjoy!
🔒 Admin Features
Check Resources & Profit:

markdown
Copy
Edit
> report
Refill Ingredients (adds +100 to each):

markdown
Copy
Edit
> refill
Reset Profit (Password Protected):

perl
Copy
Edit
> reset profit
Enter admin password to reset profit:
Default password is: Admin123

Shut down machine:

markdown
Copy
Edit
> off
🧱 Project Structure
graphql
Copy
Edit
tea-vending-machine/
├── main.py              # Main CLI logic (MakeTea class)
├── tea_maker.py         # Handles tea making and ingredients
├── menu.py              # Menu and MenuItem classes
├── money_machine.py     # Handles payment, coin processing
└── README.md            # Project overview
🧠 OOP Concepts Used
Encapsulation: Separate classes for TeaMaker, Menu, MoneyMachine

Abstraction: Users interact via clean CLI; internals are hidden

Modularity: Easy to extend new teas or features

Inheritance: (Not yet used, but code is structured to allow it)

📈 Future Enhancements
Save user preferences (e.g., always 2 tsp sugar)

Add masala/spice selection

Store data persistently (using file or DB)

GUI version using Tkinter or PyQt

💡 Author
Prince Solanki
