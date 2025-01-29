import sqlite3
from db import queries

# db = sqlite3.connect('db/registered.sqlite3')
db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def create_db():
    if db:
        print('База данных подключена')
    # cursor.execute(queries.CREATE_TABLE_registered)
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_store_detail)
    cursor.execute(queries.CREATE_TABLE_collections)


async def sql_insert_registered(fullname, age, email, city, photo):
    cursor.execute(queries.INSERT_registered_query, (
        fullname, age, email, city, photo
    ))
    db.commit()


async def sql_insert_store(name_product, size, price, photo, product_id):
    cursor.execute(queries.INSERT_store_query, (
        name_product, size, price, photo, product_id
    ))
    db.commit()


async def sql_insert_detail(product_id, category, info_product):
    cursor.execute(queries.INSERT_store_detail_query, (
        product_id, category, info_product
    ))
    db.commit()

async def sql_insert_collection(product_id, collection):
    cursor.execute(queries.INSERT_collections_query, (
        product_id, collection
    ))
    db.commit()


# CRUD - 1
# ==================================================================
def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * from store s
    INNER JOIN store_detail  sd 
    ON s.product_id = sd.product_id
    """).fetchall()
    conn.close()
    return products

def fetch_fetch_all_collections():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * from store s
    INNER JOIN store_detail  sd 
    ON s.product_id = sd.product_id
    INNER JOIN collections c
    ON s.product_id = c.productid
    """).fetchall()
    conn.close()
    return products


def delete_product(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM store WHERE product_id = ?', (product_id,))
    conn.execute('DELETE FROM store_detail WHERE product_id = ?', (product_id,))

    conn.commit()
    conn.close()




# CRUD - update
# ==================================================================

def update_product_field(product_id, field_name, new_value):
    conn = get_db_connection()

    store_table = ['name_product', 'size', 'size', 'price', 'photo']
    store_detail_table = ['category', 'info_product']

    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_detail_table:
            query = f'UPDATE store_detail SET {field_name} = ? WHERE product_id = ?'

        else:
            raise ValueError(F'Неправильное поле {field_name}')

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except ValueError as e:
        print(f'Error - {e}')

    finally:
        conn.close()


def fetch_all_collections():
    return None