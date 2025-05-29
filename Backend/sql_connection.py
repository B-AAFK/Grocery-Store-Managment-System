import mysql

__cnx = None

def get_sql_connection():
    global  __cnx
    if __cnx is None:
    # Connection to local database
     __cnx  = mysql.connector.connect(user='root', password='admin1234',
                                  host='127.0.0.1', database='grocery_store')

    return __cnx

#------------------END OF FILE-----------------------------------------------------#