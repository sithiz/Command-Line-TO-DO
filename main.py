import psycopg2
from config import load_config
from remove import remove_item
from change_item import updateItem
from read import check_item
from add_item import add_item

selectionMessage = """
        please make a selecetion
        1.Add a new item    
        2.Change an item
        3.Remove a completed item
        4.Display the list of items again
        5.Exit the To-Do list
        """

def selectionLogic():
    userSelection = int(input())
    if userSelection > 5 or userSelection < 1 :
            print("invaild response please try again")
            print(selectionMessage)
            selectionLogic()
    else :
            if userSelection == 1:
                add_item()
                print(selectionMessage)
                selectionLogic()
            if userSelection == 2:
                updateItem()
                print(selectionMessage)
                selectionLogic()
            if userSelection == 3:
                remove_item()
                print(selectionMessage)
                selectionLogic()
            if userSelection == 4:
                check_item()
                print(selectionMessage)
                selectionLogic()
            if userSelection == 5:
                return print("exited")
                




def main() :
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM list")
                row = cur.fetchone()
                while row is not None:
                    print(row)
                    row = cur.fetchone()
                print("here is your current todo list")
                print(selectionMessage)
        selectionLogic()
       
                
            
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)









if __name__ == "__main__":
    main()