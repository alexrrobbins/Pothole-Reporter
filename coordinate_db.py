def add_to_db(latitude,longitude):
    print("Writing to database")
    print(str(latitude))
    print(str(longitude))
    import mysql.connector
    from mysql.connector import errorcode
    try:
        cnx = mysql.connector.connect(user='', password='',
                                    host='',
                                    database='roadmarkers')
        cursor = cnx.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()

    add_coordinates = ("INSERT INTO marker (lat, lng, description) VALUES (%(lat)s, %(lng)s, %(description)s);")
    desc = 'This was posted from IUP'
    data_coordinates = {
                        'lat': latitude,
                        'lng':longitude,
                        'description': desc
                        }

    cursor.execute(add_coordinates, data_coordinates)
    cnx.commit()

    cursor.close()
    cnx.close()
