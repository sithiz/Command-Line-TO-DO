import psycopg2
from config import load_config

def create_tables():
    command = """
    CREATE TABLE List (
    Item_id INT NOT NULL,
    Item VARCHAR(255) NOT NULL
    )
    """

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(command)
                print("table created")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
if __name__ == '__main__':
    create_tables()
