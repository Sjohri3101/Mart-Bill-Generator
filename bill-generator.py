import customtkinter as ctk
import tkinter as tk
from fpdf import FPDF
from datetime import date
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")            
            
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1060x800+0+0")
        self.title("Bill Generator")
        self.resizable(False,False)
        
        headinglabel = ctk.CTkLabel(self, text="Welcome to Billing", text_color="#ffffff", font=("Arial", 26, "bold"), fg_color="#660066")
        headinglabel.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        billnumberlabel = ctk.CTkLabel(self, text="Bill Number", text_color="#660066", font=("Arial", 14, "bold"))
        billnumberlabel.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.billnumber = ctk.CTkEntry(self, placeholder_text="Bill Number", width=800)
        self.billnumber.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        
        customernamelabel = ctk.CTkLabel(self, text="Customer Name", text_color="#660066", font=("Arial", 14, "bold"))
        customernamelabel.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.customername = ctk.CTkEntry(self, placeholder_text="Customer Name", width=800)
        self.customername.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        
        customeraddresslabel = ctk.CTkLabel(self, text="Customer Address", text_color="#660066", font=("Arial", 14, "bold"))
        customeraddresslabel.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.customeraddress = ctk.CTkEntry(self, placeholder_text="Customer Address", width=800)
        self.customeraddress.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        self.products = [
            {"name": "Mens Jeans", "price": 799.00},
            {"name": "Mens T-Shirt", "price": 499.00},
            {"name": "Mens Shoes", "price": 1999.00},
            {"name": "Womens Dress", "price": 1299.00},
            {"name": "Womens Top", "price": 899.00},
            {"name": "Womens Pants", "price": 1099.00},
            {"name": "Kids T-Shirt", "price": 399.00},
            {"name": "Kids Shorts", "price": 599.00},
            {"name": "Kids Shoes", "price": 1499.00},
            {"name": "Home Decor", "price": 1999.00},
            {"name": "Kitchen Utensils", "price": 999.00},
            {"name": "Bedding Set", "price": 2999.00},
            {"name": "Bath Towels", "price": 699.00},
            {"name": "Mens Watch", "price": 4999.00},
            {"name": "Womens Handbag", "price": 3999.00},
            {"name": "Kids Toy", "price": 999.00},
            {"name": "Home Office Chair", "price": 9999.00},
            {"name": "Gaming Console", "price": 29999.00},
            {"name": "Smartphone", "price": 49999.00},
            {"name": "Laptop", "price": 69999.00},
            {"name": "Tablet", "price": 29999.00},
            {"name": "Smart TV", "price": 99999.00},
            {"name": "Soundbar", "price": 19999.00},
            {"name": "Wireless Headphones", "price": 9999.00},
            {"name": "Fitness Tracker", "price": 4999.00},
            {"name": "Smart Speaker", "price": 9999.00},
            {"name": "Coffee Maker", "price": 4999.00},
            {"name": "Toaster", "price": 2999.00},
            {"name": "Blender", "price": 3999.00},
            {"name": "Stand Mixer", "price": 9999.00},
            {"name": "Slow Cooker", "price": 4999.00},
            {"name": "Rice Cooker", "price": 2999.00},
            {"name": "Food Processor", "price": 6999.00},
            {"name": "Electric Kettle", "price": 2999.00},
            {"name": "Microwave", "price": 4999.00},
            {"name": "Dishwasher", "price": 49999.00},
            {"name": "Washing Machine", "price": 69999.00},
            {"name": "Dryer", "price": 69999.00},
            {"name": "Refrigerator", "price": 99999.00},
            {"name": "Air Conditioner", "price": 99999.00},
            {"name": "Heater", "price": 9999.00},
            {"name": "Fan", "price": 2999.00},
            {"name": "Vacuum Cleaner", "price": 9999.00},
            {"name": "Mop", "price": 1999.00},
            {"name": "Broom", "price": 999.00},
            {"name": "Dustpan", "price": 499.00},
        ]
        
        products_frame = ctk.CTkFrame(self)
        products_frame.grid(row=8, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        
        self.product_checkboxes = []
        column = 0
        row = 0
        for i, product in enumerate(self.products):
            if i % 10 == 0 and i != 0:
                column += 1
                row = 0
            frame = ctk.CTkFrame(products_frame)
            frame.grid(row=row, column=column, padx=5, pady=5, sticky="ew")
            
            checkbox_var = tk.BooleanVar()
            checkbox = ctk.CTkCheckBox(frame, text=product["name"], variable=checkbox_var, command=self.calculate_total)
            checkbox.pack(side="left")
            
            label = ctk.CTkLabel(frame, text=f"Rs. {product['price']:.2f}")
            label.pack(side="right")
            
            self.product_checkboxes.append((checkbox_var, product))
            row += 1
        
        totalamountlabel = ctk.CTkLabel(self, text="Total Amount", text_color="#660066", font=("Arial", 14, "bold"))
        totalamountlabel.grid(row=4, column=0, pady=5, padx=5, sticky="w")
        self.totalamount = ctk.CTkLabel(self, text="Rs. 0.00", font=("Arial", 14, "bold"))
        self.totalamount.grid(row=4, column=1, padx=5, pady=5, sticky="w")
       
        
        taxamountlabel = ctk.CTkLabel(self, text="Tax Amount", text_color="#660066", font=("Arial", 14, "bold"))
        taxamountlabel.grid(row=5, column=0, pady=5, padx=5, sticky="w")
        self.taxamount = ctk.CTkLabel(self, text="Rs. 0.00", font=("Arial", 14, "bold"))
        self.taxamount.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        
        discountpercentlabel = ctk.CTkLabel(self, text="Discount (%)", text_color="#660066", font=("Arial", 14, "bold"))
        discountpercentlabel.grid(row=6, column=0, pady=5, padx=5, sticky="w")
        self.DiscountPercent = ctk.CTkEntry(self, placeholder_text="Discount(%)", width=800)
        self.DiscountPercent.insert(0, "0")
        self.DiscountPercent.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.DiscountPercent.bind("<KeyRelease>", self.calculate_total)
        
        grandtotallabel = ctk.CTkLabel(self, text="Grand Total Amount", text_color="#660066", font=("Arial", 14, "bold"))
        grandtotallabel.grid(row=7, column=0, pady=5, padx=5, sticky="w")
        self.grandtotal = ctk.CTkLabel(self, text="Rs. 0.00", font=("Arial", 14, "bold"))
        self.grandtotal.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        
        button = ctk.CTkButton(self, text="Continue for Billing", command=self.get_selected_products, fg_color="#660066", height=50)
        button.grid(row=9, column=0, padx=10, pady=10, sticky="ew")
        
    def calculate_total(self, event=None):
        total = sum(product['price'] for var, product in self.product_checkboxes if var.get())
        self.totalamount.configure(text=f"Rs. {total:.2f}")
        
        tax = total * 0.18
        self.taxamount.configure(text=f"Rs. {tax:.2f}")
        
        discount_percentage = self.DiscountPercent.get()
        if not discount_percentage:
            discount_amount = 0
        else:
            discount_amount = (total + tax) * float(discount_percentage) / 100
        
        self.discount_amount = discount_amount  # Assign the discount amount to an attribute
        # self.discount_amount_label.configure(text=f"Rs. {discount_amount:.2f}")  # Update the label
    
        grand_total = (total + tax) - self.discount_amount
        self.grandtotal.configure(text=f"Rs. {grand_total:.2f}")
        
    def get_selected_products(self):
        billwindow = ctk.CTkToplevel(self)
        billwindow.transient(self)
        billwindow.title("Bill Generated") 
        billwindow.geometry("800x600")
        billwindow.resizable(False, False)
        billwindow.configure(bg_color="#000000") 
        
        
        bill_number = self.billnumber.get()
        customer_name = self.customername.get()
        customer_address = self.customeraddress.get()
        total_amount = self.totalamount.cget("text")
        tax_amount = self.taxamount.cget("text")
        discount = self.DiscountPercent.get()
        discount_amount = f"Rs. {self.discount_amount:.2f}"
        grand_total = self.grandtotal.cget("text")

        selected_products = [product for var, product in self.product_checkboxes if var.get()]
        def generate_pdf():
            # Create a PDF object
            pdf = FPDF(format='letter')

            # Add a page
            pdf.add_page()

            # Set the font for the heading
            pdf.set_font("Arial", style='B', size=8)

            # Set the text color for the heading
            pdf.set_text_color(0, 0, 255)

            # Add the heading
            pdf.cell(0, 10, txt="COMPUTERISED GENERATED BILL", ln=True, align='C')

            # Set the font for the date
            pdf.set_font("Arial", size=12)

            # Set the text color for the date
            pdf.set_text_color(0, 0, 0)

            # Add the date
            pdf.set_font("Arial", style="B", size=8)
            pdf.cell(0, 10, txt="Date : " + str(date.today()), ln=True, align='R')

            # Set the font for the bill details
            pdf.set_font("Arial", size=8)
            
            # Create table rows
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="Bill Number", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=bill_number, ln=True, align='R', border=1)
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="Customer Name", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=customer_name, ln=True, align='R', border=1)
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="Customer Address", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=customer_address, ln=True, align='R', border=1)
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="Total Amount", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=total_amount, ln=True, align='R', border=1)
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="(+)" + " Tax Amount", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=tax_amount, ln=True, align='R', border=1)
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="(-)" + " Discount (" + str(discount) + "%)", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=discount_amount, ln=True, align='R', border=1)
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(100, 10, txt="Grand Total", ln=False, align='L', border=1)
            pdf.set_font("Arial", size=8)
            pdf.cell(100, 10, txt=grand_total, ln=True, align='R', border=1)
            

            # Add a line break
            pdf.ln(5)

            # Set the font for the product details
            pdf.set_font("Arial", size=8)

            # Set the text color for the product details
            pdf.set_text_color(0, 100, 0)

            # Add the product details
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(200, 10, txt="Items:", ln=True, align='L')
            pdf.set_font("Arial", size=8)
            # Add the product details
            pdf.set_font("Arial", style="B", size=12)
            pdf.cell(100, 10, txt="Product", ln=False, align='L', border=1)
            pdf.cell(100, 10, txt="Price", ln=True, align='R', border=1)
            pdf.set_font("Arial", size=8)

            for product in selected_products:
                pdf.cell(100, 10, txt=product["name"], ln=False, align='L', border=1)
                pdf.cell(100, 10, txt="Rs. " + str(product['price']), ln=True, align='R', border=1)

            # Add a line break
            pdf.ln(5)
            
            # Set the background color for the footer
            pdf.set_fill_color(200, 200, 200)

            # Set the font for the footer
            pdf.set_font("Arial", size=8)

            # Set the text color for the footer
            pdf.set_text_color(255, 0, 0)

            # Add the footer
            pdf.cell(0, 10, txt="Thank you for shopping with us!", ln=True, align='C', fill=True)

            # Output the PDF
            pdf.output("bill.pdf")
            messagebox.showinfo("Bill Generated", "Your bill has been generated successfully.")
        
        printfinalbill_button = ctk.CTkButton(billwindow, text="Print Final Bill", command=generate_pdf, fg_color="#660066", height=50)
        printfinalbill_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
     
        
        bill_number_label = ctk.CTkLabel(billwindow, text="Bill Number", text_color="#660066", font=("Arial", 14, "bold"))
        bill_number_label.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        bill_number_value = ctk.CTkLabel(billwindow, text=bill_number)
        bill_number_value.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        customer_name_label = ctk.CTkLabel(billwindow, text="Customer Name", text_color="#660066", font=("Arial", 14, "bold"))
        customer_name_label.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        customer_name_value = ctk.CTkLabel(billwindow, text=customer_name)
        customer_name_value.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        customer_address_label = ctk.CTkLabel(billwindow, text="Customer Address", text_color="#660066", font=("Arial", 14, "bold"))
        customer_address_label.grid(row=2, column=2, pady=5, padx=5, sticky="w")
        customer_address_value = ctk.CTkLabel(billwindow, text=customer_address)
        customer_address_value.grid(row=2, column=3, pady=5, padx=5, sticky="w")

        total_amount_label = ctk.CTkLabel(billwindow, text="Total Amount", text_color="#660066", font=("Arial", 14, "bold"))
        total_amount_label.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        total_amount_value = ctk.CTkLabel(billwindow, text=total_amount)
        total_amount_value.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        tax_amount_label = ctk.CTkLabel(billwindow, text="(+) Tax Amount", text_color="#660066", font=("Arial", 14, "bold"))
        tax_amount_label.grid(row=4, column=0, pady=5, padx=5, sticky="w")
        tax_amount_value = ctk.CTkLabel(billwindow, text=tax_amount)
        tax_amount_value.grid(row=4, column=1, pady=5, padx=5, sticky="w")

        discount_label = ctk.CTkLabel(billwindow, text=f"(-) Discount ({discount}%)", text_color="#660066", font=("Arial", 14, "bold"))
        discount_label.grid(row=5, column=0, pady=5, padx=5, sticky="w")
        discount_value = ctk.CTkLabel(billwindow, text=discount_amount)
        discount_value.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        grand_total_label = ctk.CTkLabel(billwindow, text="Grand Total", text_color="#660066", font=("Arial", 14, "bold"))
        grand_total_label.grid(row=6, column=0, pady=5, padx=5, sticky="w")
        grand_total_value = ctk.CTkLabel(billwindow, text=grand_total)
        grand_total_value.grid(row=6, column=1, pady=5, padx=5, sticky="w")

        products_label = ctk.CTkLabel(billwindow, text="Items", text_color="#660066", font=("Arial", 14, "bold"), bg_color="#ffffcc")
        products_label.grid(row=7, column=0, pady=5, padx=5, sticky="w")

        column = 0
        row = 8
        for i, product in enumerate(selected_products):
            if i % 8 == 0 and i != 0:
                column += 2
                row = 8
            product_name = ctk.CTkLabel(billwindow, text=product["name"])
            product_name.grid(row=row, column=column, pady=5, padx=5, sticky="w")
            product_price = ctk.CTkLabel(billwindow, text=f"Rs. {product['price']:.2f}")
            product_price.grid(row=row, column=column+1, pady=5, padx=5, sticky="w")
            row += 1

        billwindow.mainloop()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()