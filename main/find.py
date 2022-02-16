def find():
    datefinder=input("""Enter the date: 

    """)
    namefinder=input("""ENter your name:
    """)
    sql ="SELECT * FROM ebill WHERE date= :datefinder AND name= :namefinder"
    c.execute(sql,{'datefinder':datefinder,'namefinder':namefinder})
    print("""Here is the data from the date in the form (name,date,average power consumption(KWh), bill(in rupees):""")
    print(c.fetchall())
    ch = input("press y to continue to check records and n to end")
    if ch=='y':
      find()
