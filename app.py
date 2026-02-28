from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Sample Menu Data (Category Wise)
menu = {
    "Starters": {
        "Veg Spring Rolls": 120,
        "Chicken 65": 180,
        "Paneer Tikka": 200
    },
    "Main Course": {
        "Veg Biryani": 220,
        "Chicken Biryani": 280,
        "Butter Naan": 40,
        "Paneer Butter Masala": 240
    },
    "Beverages": {
        "Coke": 40,
        "Lemon Juice": 30,
        "Coffee": 50
    },
    "Desserts": {
        "Ice Cream": 60,
        "Brownie": 90
    }
}

@app.route('/')
def home():
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return render_template('menu.html', menu=menu, current_time=current_time)

@app.route('/order', methods=['POST'])
def order():
    table_number = request.form.get("table_number")
    order_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    total = 0
    ordered_items = []

    for category in menu:
        for item, price in menu[category].items():
            quantity = request.form.get(item)
            if quantity and int(quantity) > 0:
                item_total = int(quantity) * price
                total += item_total
                ordered_items.append({
                    "name": item,
                    "quantity": quantity,
                    "price": price,
                    "item_total": item_total
                })

    return render_template('summary.html',
                           table_number=table_number,
                           ordered_items=ordered_items,
                           total=total,
                           order_time=order_time)

if __name__ == '__main__':
    app.run(debug=True)