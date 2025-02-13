import psycopg2
from config import load_config

def check_item():
    checkItems = """
    SELECT * FROM List
    """


 


    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(checkItems)
                row = cur.fetchone()
                counter = 0
                while row is not None:
                    counter += 1
                    print(row[0],row[1])
                    row = cur.fetchone()
        print(f"""
              items fetched: {counter}
              """)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    check_item()