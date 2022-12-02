import sqlite3

conn = sqlite3.connect("stuff.db")

c = conn.cursor()

info = F""" Available Commands:

'add'  --> Add a new item to your database                   # ACTIVE
'view' --> View all items in database                        # ACTIVE
'quit' --> Quits the Loop and commits changes to             # ACTIVE
'view specific' --> View one item in database (if it exists) # ACTIVE
              """


def create_Table():
    c.execute(
        """CREATE TABLE foods (
        name text,
        kg real,
        cups real,
        grams real,
        liter real,
        oz real,
        tbsp real,
        tsp real
    )"""
    )
    conn.commit()


def add_to_db():
    c.execute("INSERT INTO foods VALUES ('{}', {},{},{},{},{},{},{})".format(

        input("Enter Name"),

        float(input("Enter KG: ")),
        float(input("Enter Cups: ")),
        float(input("Enter grams: ")),
        float(input("Enter liters: ")),
        float(input("Enter oz: ")),
        float(input("Enter tbsp: ")),
        float(input("Enter tsp: "))

        ))
    print("", end='\n')
    


    conn.commit()


def print_all():
    c.execute(f" SELECT * FROM foods")
    for data in c.fetchall():
        print(f"Name: {data[0]} \n KG: {data[1]} \n CUPS: {data[2]} \n Grams: {data[3]} \n Liters: {data[4]} \n Oz: {data[5]} \n Tbsp: {data[6]} \n Tsp: {data[7]} \n")


def convert(item, fromwhat, towhat):
    c.execute("SELECT * FROM foods WHERE name='{}'".format(item))

    my_item = c.fetchone()

    if fromwhat == "kg":
        val_1 = my_item[1]

    if fromwhat == "grams":
        val_1 = my_item[3]

    if fromwhat == "liters":
        val_1 = my_item[4]

    if fromwhat == "oz":
        val_1 = my_item[5]

    if fromwhat == "tbsp":
        val_1 = my_item[6]

    if fromwhat == "tsp":
        val_1 = my_item[7]

    amount = float(input(f"Enter amount in {fromwhat} --> "))

    if towhat == "kg":
        val_2 = my_item[1]
        
    if towhat == "cups":
        val_2 = my_item[2]

    if towhat == "grams":
        val_2 = my_item[3]

    if towhat == "liters":
        val_2 = my_item[4]

    if towhat == "oz":
        val_2 = my_item[5]

    if towhat == "tbsp":
        val_2 = my_item[6]

    if towhat == "tsp":
        val_2 = my_item[7]

    diffrence = val_2/val_1

    # try:
    #     decs = int(
    #         input("How many decimals do you want your result in (text for all)? --> "))
    # except ValueError:
    #     decs = True
    
    decs = 3

    if not decs == True:
        value = round(amount * diffrence, decs)
    else:
        value = amount * diffrence

    print(f"{amount}{fromwhat} --> {value}{towhat}")


def print_specific(which):
    try:
        print(which)
        c.execute(" SELECT * FROM foods WHERE name='{}'".format(which))

        for data in c.fetchall():
            print(
                f" Name: {data[0]} \n KG: {data[1]} \n CUPS: {data[2]} \n Grams: {data[3]} \n Liters: {data[4]} \n Oz: {data[5]} \n Tbsp: {data[6]} \n Tsp: {data[7]} \n")
    except Exception:
        print(f"{which} doesnt exist")
        e = input("Do you want to add it? --> ")
        if e == "yes":
            add_to_db()


#create_Table()

while True:
    e = input("What do you want to do? --> ")
    if e == "view":
        print()
        print_all()

    if e == "add":
        print()
        add_to_db()

    if e == "convert":
        print()
        convert(input("Enter item --> "), input("What are you converting from? --> "),
                input("What are you converting to --> "))

    if e == "view specific":
        print()
        print_specific(input("Which Item do you want to see? --> "))

    if e == "quit":
        break

    if e == "help":
        print(info)

conn.commit()

conn.close()
