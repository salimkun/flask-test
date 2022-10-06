import sqlite3, random, datetime
from .models.product_model import Product


def getNewId():
    return random.getrandbits(28)


product_list = [
    {
        'name': "Xenia R CVT 2022",
        'price': 2440000,
        'description': "xenia terbaru 2022 dengan fitur terbaru",
        'quanitity': 2,
        'timestamp':datetime.datetime.now()
    },
    {
        'name': "Rocky R CVT 2022",
        'price': 2740000,
        'description': "rocky terbaru 2022 dengan fitur terbaru",
        'quanitity': 2,
        'timestamp':datetime.datetime.now()
    },
]    

def connect():
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, description TEXT, quantity INTEGER, timestamp TEXT)")
    conn.commit()
    conn.close()
    for i in product_list:
        bk = Product(getNewId(), i['name'], i['price'], i['description'], i['quantity'], i['timestamp'])
        insert(bk)

def insert(product):
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    print('new product: ', product.serialize())
    cur.execute("INSERT INTO products VALUES (?,?,?,?,?,?)", (
        product.id,
        product.name,
        product.price,
        product.description,
        product.quantity,
        product.timestamp
    ))
    conn.commit()
    conn.close()

def view(order_by="", sort_by=""):
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    query = "SELECT * FROM products "
    if order_by:
        if not sort_by:
            sort_by = "desc"
        query = query + "order by " + order_by + " " + sort_by
    cur.execute(query)
    rows = cur.fetchall()
    products = []
    for i in rows:
        product = Product(i[0], i[1], i[2], i[3], i[4], i[5])
        products.append(product)
    conn.close()
    return products