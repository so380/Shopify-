from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {"name": "T-Shirt", "price": 499},
    {"name": "Shoes", "price": 1499},
    {"name": "Watch", "price": 999}
]

@app.route("/")
def home():
    html = """
    <h1>My Online Store</h1>
    {% for product in products %}
        <div>
            <h3>{{ product.name }}</h3>
            <p>₹{{ product.price }}</p>
            <button>Buy Now</button>
        </div>
        <hr>
    {% endfor %}
    """
    return render_template_string(html, products=products)

if __name__ == "__main__":
    app.run(debug=True)
