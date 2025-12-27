import psycopg2


def get_connection():
    return psycopg2.connect(

        dbname='shop',
        user='postgres',
        password="A0B1D9E2",
        host='localhost',
        port=5432
    )


def type_cars():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE car_type(
    id serial PRIMARY KEY,
    name varchar(50) unique)
    ''')
    connect.commit()
    print(f'type_cars table has created')


def cars():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE car(
    id serial PRIMARY KEY,
    name varchar(50) unique,
    type_id int REFERENCES car_type(id),
    year int,
    price int check(price>0),
    is_sold bool default false)''')
    connect.commit()
    print(f'cars table has created')


def customers():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE customers(
    id serial PRIMARY KEY,
    full_name varchar(100) unique,
    phone varchar(20))''')
    connect.commit()
    print(f'customers table has created')


def sales():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    car_id INT,
    customer_id INT,
    sale_date DATE,

    FOREIGN KEY (car_id) REFERENCES car(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
''')
    connect.commit()
    print(f'sales table has created')


type_cars()
cars()
customers()
sales()
