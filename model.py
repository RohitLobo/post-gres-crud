from config import config
import psycopg2
from psycopg2 import DatabaseError
# db_config = config(filename="database.ini",section="postgresql")


# db_connection = psycopg2.connect(dbname=db_config['database'],host = db_config['host'], user=db_config['db_username'], password=db_config['db_password'])
# print(**db_config)
# db_connection = psycopg2.connect(**db_config)
# db_cursor = db_connection.cursor()

# db_cursor.execute("SELECT * FROM demo_table;")
# rows= db_cursor.fetchall()
# print('Before commit : ',rows)

# db_cursor.execute("""INSERT INTO demo_table (employee_id, first_name, last_name, email, phone_number) VALUES
# (11, 'John', 'Doe', 'john.doe2@example.com', '555-1234'),
# (4, 'Michael', 'Brown', 'michael.brown@example.com', '555-4321'),
# (5, 'Sarah', 'Davis', 'sarah.davis@example.com', '555-6789'),
# (6, 'David', 'Wilson', 'david.wilson@example.com', '555-2345'),
# (7, 'Laura', 'Taylor', 'laura.taylor@example.com', '555-3456'),
# (8, 'James', 'Anderson', 'james.anderson@example.com', '555-7890'),
# (9, 'Olivia', 'Thomas', 'olivia.thomas@example.com', '555-8901'),
# (10, 'William', 'Martinez', 'william.martinez@example.com', '555-9012');""")
# db_connection.commit()
# rows= db_cursor.fetchall()
# print(rows)
# db_cursor.execute("SELECT * FROM demo_table;")
# rows= db_cursor.fetchall()
# print('After commit : ',rows)


class Db_connector:
    def __init__(self,config_filename,config_section):
        self.db_config = config(filename=config_filename,section=config_section)
        
        
    def db_conn(self):
        db_connection = None
        try :
            db_connection = psycopg2.connect(dbname=self.db_config ['database'],host = self.db_config ['host'], user=self.db_config ['db_username'], password=self.db_config ['db_password'])
            print('>>>Connecting to PostgreSQL...')
            crsr= db_connection.cursor()
            crsr.execute('SELECT version();')
            print(f'>>>DB version : {crsr.fetchONE()}')
            crsr.close()
            
            
        except (Exception, psycopg2.DatabaseError )as err:
            print(f'Error {err}')    
            
        finally:
            if db_connection is not None:
                db_connection.close()
                print('>>> Terminating PostgreSQL connection')    
        
    # def display_info(self):
    #     print(f"Name: {self.name}")
    #     print(f"Age: {self.age}")
    #     print(f"Email: {self.email}")
    
    
    

db_instance = Db_connector("database.ini","postgresql")
db_instance.db_conn()