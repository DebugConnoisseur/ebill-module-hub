def findall():
    namefinder= input("Enter your name(first character capital)")
    sql = "SELECT * FROM electricbill WHERE name= :namefinder ORDER BY date"
    c.execute(sql,{"namefinder":namefinder})
    print("Here are all the bills listed with the name" + namefinder)
    print(c.fetchall()) 
