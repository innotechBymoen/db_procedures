import dbcreds
import mariadb

def get_number():
    num = input("Please enter a minimum price: ")
    num = float(num)
    return num

def get_priced_items(num):
    conn = mariadb.connect(**dbcreds.conn_params)
    cursor = conn.cursor()

    cursor.execute('call get_priced_items(?)', [num])
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    for item in results:
        print('Name:', str(item[1], 'utf-8'), 'Price:', item[2])

conn = mariadb.connect(**dbcreds.conn_params)
cursor = conn.cursor()

cursor.execute('call get_all_items()')
results = cursor.fetchall()

cursor.close()
conn.close()

for item in results:
    print('Name:', str(item[1], 'utf-8'), 'Price:', item[2])

user_num = get_number()
get_priced_items(user_num)