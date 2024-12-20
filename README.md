Inventory System
A simple inventory management system built using Python's Tkinter library for the graphical user interface (GUI). This application allows users to manage an inventory by adding, removing, and updating items, as well as saving and loading inventory data from a JSON file.

Features
Add Items: Allows users to add new items to the inventory with a specified quantity.
Remove Items: Lets users remove items from the inventory.
Update Item Quantity: Users can update the quantity of an existing item in the inventory.
Save Inventory: Saves the current inventory to a JSON file.
Load Inventory: Loads inventory data from a JSON file into the system.
Requirements
Python 3.x
Tkinter (comes pre-installed with Python)
JSON
Installation
Clone or download the repository.
Ensure you have Python 3.x installed.
Install any necessary dependencies (if needed).
Running the Application
Download and place the project files in your desired directory.
To start the application, run the inventory_system.py script:
bash
Copy code
python inventory_system.py
The GUI will open, and you can interact with the inventory system.
File Structure
inventory_system.py: Main script containing the logic and GUI of the inventory system.
chromehearts_logo.png: Logo image used in the GUI (optional).
chromehearts_crossz.png: Cross image used in the GUI (optional).
How to Use
Add Item: Click the "Add Item" button, enter the item name, and specify the quantity.
Remove Item: Select an item from the inventory list and click "Remove Item" to delete it.
Update Quantity: Select an item, click "Update Quantity", and enter the new quantity.
Save Inventory: Click "Save Inventory" to store the current inventory to a .json file.
Load Inventory: Click "Load Inventory" to load an inventory from a .json file.
Exit: Click "Exit" to close the application.
Error Handling
If the item already exists when trying to add a new item, a message will inform you that the item cannot be added.
If an invalid quantity (non-numeric or negative) is entered, an error message will be shown.
When trying to load or save an inventory file, error messages will be shown in case of issues like incorrect file format, file not found, or issues with saving.
Notes
The application relies on Tkinter's simple dialog boxes for user interaction.
The images chromehearts_logo.png and chromehearts_crossz.png are optional and can be replaced with any other images, or omitted if not needed.
License
This project is open-source and free to use. You can modify or extend it as needed.
