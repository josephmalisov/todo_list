import psycopg2
try:
    connection = psycopg2.connect(user = "azbqralazbwyxa",
                                  password = "0206a0e69bbd6645722f471b1997afdefb56e3d4bac73044a69e7859d54efaca",
                                  host = "ec2-54-211-210-149.compute-1.amazonaws.com",
                                  port = "5432",
                                  database = "d8trkkj3bm36c9")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")