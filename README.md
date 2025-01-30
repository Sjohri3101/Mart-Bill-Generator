Bill Generator Application
Overview
This is a simple bill generator application built using Python and the customtkinter library. The application allows users to select products, calculate the total amount, tax, and discount, and generate a bill in PDF format.

Features
User-friendly interface with customtkinter library
Product selection with checkboxes
Automatic calculation of total amount, tax, and discount
Generation of bill in PDF format
Display of bill details in a separate window
Requirements
Python 3.x
customtkinter library
fpdf library
tkinter library
Installation
Install the required libraries using pip:

pip install customtkinter fpdf

2.  Clone the repository or download the code.

**Usage**
-----

1.  Run the application using Python:
python app.py
Select products by checking the corresponding checkboxes.
Enter the bill number, customer name, and customer address.
Enter the discount percentage (optional).
Click the "Continue for Billing" button to calculate the total amount, tax, and discount.
Click the "Print Final Bill" button to generate the bill in PDF format.
Code Structure
The code is organized into a single file, app.py, which contains the following classes and functions:

App class: The main application class that creates the GUI and handles user interactions.
calculate_total method: Calculates the total amount, tax, and discount based on the selected products and discount percentage.
get_selected_products method: Retrieves the selected products and generates the bill in PDF format.
generate_pdf function: Creates a PDF object and adds the bill details to it.
License
This code is released under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

Acknowledgments
customtkinter library: A Python library for creating custom GUI applications.
fpdf library: A Python library for generating PDF files.
tkinter library: A Python library for creating GUI applications.
