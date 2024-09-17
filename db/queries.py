CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product VARCHAR(255),
    size VARCHAR(255),
    price VARCHAR(255),
    product_id VARCHAR(255),
    photo TEXT
    )
"""


INSERT_PRODUCTS_QUERY = """
    INSERT INTO products (name_product, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_TABLE_PRODUCT_DETAIL = """
    CREATE TABLE IF NOT EXISTS product_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    product_id INTEGER,
    category VARCHAR(255),
    info_product VARCHAR(255)
    )
"""

INSERT_INTO_PRODUCT_DETAIL = """
    INSERT INTO product_detail (product_id, category, info_product)
    VALUES (?, ?, ?)
"""
