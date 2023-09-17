import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='1234', host='127.0.0.1', port='5432'
)

cur = conn.cursor()
cur.execute('''SELECT * FROM courses''')
courses_table = cur.fetchall()
#print(courses_table)

cur_2 = conn.cursor()
cur_2.execute('''SELECT * FROM academics''')
academics_table = cur_2.fetchall()
#print(academics_table)

command = (''' CREATE TABLE Delivered_by_Python (
                  id_courses char(7),
                  id_academics varchar(5),
  
                  primary key (id_courses, id_academics)
            );
''')

cur_3 = conn.cursor()
#cur_3.execute(command)
cur_3.execute(''' SELECT * FROM delivered_by_python ''')
conn.commit()

delivered_by_Python = cur_3.fetchall()
#print(delivered_by_Python)

# POPULATING DELIVERED_BY_PYTHON TABLE ------- QUERIES

course_id_list = []
for i in range(len(courses_table)):
   course_id_list.append(courses_table[i][0])

academics_id_list = []
for k in range(len(academics_table)):
   academics_id_list.append(academics_table[k][0])

print(course_id_list)
print(academics_id_list)

while True:

   Add_New_Delivery_y_n = input("Add New Delivery (y/n): ")
   if Add_New_Delivery_y_n == "n":
      break

   elif Add_New_Delivery_y_n == "y":
      New_Course_Delivery = input("New course delivery :")
      Lecturer_id = input("Lecturer ID : ")

      if New_Course_Delivery not in course_id_list:
         print(New_Course_Delivery + " course does not exist ! ")
         print("Failed to add ")

      else:
         if Lecturer_id in academics_id_list:

             insert_query = """ INSERT INTO delivered_by_python  (id_courses,id_academics) VALUES (%s,%s)"""
             record_to_insert = (New_Course_Delivery,Lecturer_id)
             cur_3.execute(insert_query, record_to_insert)
             conn.commit()
             print("Delivery successfully added")

         else:
            print("Lecturer " + Lecturer_id + " does not exist ! ")
            print("Failed to add")

   else:
      print("Invalid response, try it again ! ")
