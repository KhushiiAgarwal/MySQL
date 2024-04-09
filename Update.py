import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                             user='root',
                                             password='root',
                                             database='bnqhall',
                                             autocommit = True)
def update_city_name(city_up, c_name):
    try:
        cursor = connection.cursor()
        cur = connection.cursor()
        
        sql_update_query = """Update cust set city = %s where c_name = %s """
        #input_data = (city_up, c_name)
        cursor.execute(sql_update_query, (city_up, c_name))
        #print(c_name,city_up,return1,sql_update_query)
        connection.commit()
        print("Record Updated successfully ")
        
        #print("Happy to serve you, do you wish to continue ahead?")
    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
c_name=input('Enter your name for updating record:')
city_up=input('Enter updated city:')
update_city_name(c_name,city_up)
#update_city_name("New Delhi","Rama")
