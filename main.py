# Import the necessary tools from the Flask framework
from flask import Flask, render_template, request

# Initialize the Flask web application
app = Flask(__name__)

# Define the karinderya menu dictionary with food items as keys and prices as values
menu_prices = {
    "Adobo": 80,
    "Sinigang na Baboy": 90,
    "Menudo": 75,
    "Afritada": 80,
    "Chopseuy": 70,
    "Fried Chicken": 85,
    "Fried Fish (Tilapia)": 75,
    "Tokwa't Baboy": 60,
    "Lumpiang Shanghai (3 pcs)": 50,
    "Ginisang Monggo": 55,
    "Rice": 15,
    "Soup": 20,
    "Softdrinks": 25
}


# Define the main route to handle both GET (viewing) and POST (submitting) requests
@app.route('/', methods=['GET', 'POST'])
def receipt_generator():
    # subtotal: Tracks the sum of the prices of selected items
    subtotal = 0
    
    # vat: Stores the calculated 12% Value Added Tax
    vat = 0
    
    # total: Holds the final amount to be paid (subtotal + vat)
    total = 0
    
    # selected_items: A list to store the names of the food items the user checked
    selected_items = []
    
    # customer_name: Stores the name entered by the customer
    customer_name = ""
    
    # table_number: Stores the table number entered by the customer
    table_number = ""

    # Check if the request is a POST (meaning the user submitted the form)
    if request.method == 'POST':
        # Get the customer's name and table number from the form inputs
        customer_name = request.form.get('customer_name')
        table_number = request.form.get('table_number')
        
        # Get the list of all checked menu items from the form
        selected_items = request.form.getlist('menu_item')
        
        # Loop through each selected item to calculate the subtotal
        for item in selected_items:
            # Check if the item exists in our menu dictionary to avoid errors
            if item in menu_prices:
                # Add the price of the item to the running subtotal
                subtotal += menu_prices[item]
                
        # Calculate the 12% VAT based on the subtotal
        vat = subtotal * 0.12
        
        # Calculate the final total by adding the subtotal and the VAT
        total = subtotal + vat

    # Render the HTML template and pass all calculated variables to it
    return render_template(
        'index.html',
        subtotal=subtotal,
        vat=vat,
        total=total,
        items=selected_items,
        customer_name=customer_name,
        table_number=table_number
    )


# Run the Flask application in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
