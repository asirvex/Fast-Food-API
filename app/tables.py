import os, psycopg2

class db():
    def __init__(self):
        self.db_url=os.getenv('DATABASE_URL')
        self.conn= psycopg2.connect(self.db_url)
        self.cur=self.conn.cursor()

    def create_tables(self):
        #create foods table
        self.foods="""CREATE TABLE IF NOT EXISTS foods(
                    id INT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    price REAL NOT NULL
                    );"""
        self.cur.execute(self.foods)

        #create orders table
        self.orders="""CREATE TABLE orders(
                    id integer PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    address TEXT,
                    units INT
                    );"""
        self.cur.execute(self.orders)
        print("tables created successfully")

    
    def insert_food(self, id, name, price):
        self.id=id
        self.name=name
        self.price=price
        if self.id and self.name and self.price:
            self.cur.execute(
                            """INSERT INTO foods(id, name, price)
                            VALUES(%s, %s, %s)""", (self.id, self.name, self.price)
                            )
        self.conn.commit()

    def insert_order(self, id, name, price):
        self.id=id
        self.name=name
        self.price=price
        if self.id and self.name and self.price:
            self.cur.execute(
                            """INSERT INTO orders(id, name, price)
                            VALUES(%s, %s, %s)""", (self.id, self.name, self.price)
                            )
        self.conn.commit()

    def fetch_foods(self):
        self.cur.execute("SELECT * from foods")
        return self.cur.fetchall()

    def fetch_orders(self):
        self.cur.execute("SELECT * orders")
        return self.cur.fetchall()
        