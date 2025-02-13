import psycopg2
from config import load_config

def updateItem():

    print("select item_id to update")
    itemToUpdate = int(input())
   

    print("change item description")
    
    newItem = input()


    command = """
    UPDATE list
    SET item='%s'
    WHERE Item_id='%d'
    """ % (newItem,itemToUpdate)


 


    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(command)

        print("""
              item updated
              """)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        

if __name__ == "__main__":
    updateItem()