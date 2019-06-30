import csv
import mysql.connector
import my_settings
from django.db import connection

db_settings = my_settings.DATABASES
options = db_settings['default'].get('OPTIONS', None)

if options and 'read_default_file' in options:
    db = mysql.connector.connect(read_default_file=options['read_default_file'])
else:
    db_default = db_settings['default']
    db = mysql.connector.connect(host= db_default.get('HOST'),
                         user= db_default.get('USER'),
                         passwd= db_default.get('PASSWORD'),
                         db= db_default.get('NAME'))

cursor = db.cursor()
# cursor.execute(f"DELETE FROM suppliers")

with open('exercise_list.csv', encoding='utf-8-sig') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
       
        sql = f"""INSERT INTO train_traininfo (
            train_name,
            default_activation,
            default_break,
            default_set,
            default_calorie
        ) VALUES (
            %(train_name)s,
            %(default_activation)s,
            %(default_break)s,
            %(default_set)s,
            %(default_calorie)s
        )"""

        cursor.execute(sql, row)


db.commit()

db.close()
