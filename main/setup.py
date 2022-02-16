def setup(q):
   question=input("""do you want to setup the application? Respond with 'y' to setup, 'n' to skip (only for first time): 
   """)
   
   if question=='y':
     print("""Finished setting up the application
        """)
     cur.execute("""CREATE TABLE electricbill (
            name varchar(30) PRIMARY KEY
            date integer,
            pu integer,
            tamount integer
            );""")
   else:
        pass 
