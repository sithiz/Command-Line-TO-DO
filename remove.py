import psycopg2
from config import load_config

def remove_item():
    requestedId = int(input())

    removeItem = """
    DELETE FROM list WHERE Item_id='%d'
""" % (requestedId)


 


    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(removeItem)
                print("item number  deleted:", requestedId)
        
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    remove_item()