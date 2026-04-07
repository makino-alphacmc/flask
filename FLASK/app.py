from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to the Product Page</h1>"

@app.route('/product')
def product():
    product_list =[
        "computer", "smartphone", "tablet"
    ]
    product_dict = {"id": "1", "name": "ノートパソコン", "processor": "core i5", "price": "550000"},
  
    return render_template('product.html', product_list=product_list, product_dict=product_dict)

if __name__ == '__main__':
    app.run(debug=True)