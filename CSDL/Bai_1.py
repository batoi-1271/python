import mysql.connector
conn = mysql.connector.connect(
    host= "localhost",
    user = "root",
    passwd = "1234",
    database = "kinhbac"
)
sql = conn.cursor()
# sql.execute("CREATE DATABASE kinhbac")
# sql.execute("show databases")
# for i in sql:
#     print(i)
#
# sql.execute("create table `kinhbac`.`sinhvien` (masv int(15) primary key, ten varchar(20),diachi varchar(30))")
# sql.execute("SHOW TABLES")
# for i in sql:
#     print(i)

# insert_data = "INSERT INTO sinhvien(masv, ten, diachi) VALUES (555, 'Thai', 'HN')"
# sql.execute(insert_data)
# conn.commit()

# sql.execute("SELECT * FROM sinhvien")
# result = sql.fetchall()
# for i in result:
#     print(i)

update_data = "UPDATE sinhvien SET ten = 'Thai Duong' WHERE masv = 555"
sql.execute(update_data)
conn.commit()