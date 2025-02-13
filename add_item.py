import psycopg2
from config import load_config

def add_item():
    toDoItem = input()


    command = """
    INSERT INTO list (Item)
    VALUES ('%s'); 
    """ % (toDoItem)


    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(command)
                print("item added")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    add_item()