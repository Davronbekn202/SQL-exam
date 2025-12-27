import psycopg2


def get_connection():
    return psycopg2.connect(
        dbname='shop',
        user='postgres',
        password='A0B1D9E2',
        host='localhost',
        port=5432
    )


def add_car(name, type_id, year, price, is_sold=False):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   INSERT INTO car (name, type_id, year, price, is_sold)
                   VALUES (%s, %s, %s, %s, %s)
                   ''', (name, type_id, year, price, is_sold))
    connection.commit()
    print("Car tiqildi")


def add_type(ty):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   insert into car_type (name)
                   values (%s)
                   ''', (ty,))
    connection.commit()
    print("Type tiqildi")


# add_type('mechanic')
# add_type('automat')
def read_cars():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM car order by id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def update_price(new_price, car_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   UPDATE car
                   SET price = %s
                   WHERE id = %s
                   ''', (new_price, car_id))
    connection.commit()

    print("Price ozgardi")


def delete_car(car_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   DELETE
                   FROM car
                   WHERE id = %s
                   ''', (car_id,))
    connection.commit()
    cursor.close()
    connection.close()
    print(f"{car_id} ochirildi")


def search_car(name, min_price, max_price):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   SELECT *
                   FROM car
                   WHERE name ILIKE %s
                     AND price BETWEEN %s
                     AND %s
                     AND is_sold = false
                   ''', (f"%{name}%", min_price, max_price))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def sell_car(car_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   UPDATE car
                   SET is_sold = true
                   WHERE id = %s
                   ''', (car_id,))
    connection.commit()
    print("Car sotildi")


def add_customer(full_name, phone):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
                   INSERT INTO customers (full_name, phone)
                   VALUES (%s, %s)
                   ''', (full_name, phone))
    connection.commit()
    print("Customer qoshildi")


def search(title):
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("""  
    SELECT * FROM car WHERE name = '%s' """, (title,))


def create_sales_view():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
                CREATE
                OR REPLACE VIEW sales_view AS
                SELECT c.name       AS car,
                       ct.name      AS type,
                       c.price,
                       cu.full_name AS customer,
                       s.sale_date
                FROM sales s
                         JOIN car c ON c.id = s.car_id
                         JOIN car_type ct ON ct.id = c.type_id
                         JOIN customers cu ON cu.id = s.customer_id;
                ''')
    conn.commit()
