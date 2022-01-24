import sqlalchemy
db = 'postgresql://postgres:270194@localhost:5432/music1_1'
engine = sqlalchemy.create_engine(db)
print(engine) #Результат - Engine(postgresql://postgres:***@localhost:5432/music1_1)


# engine.connect()
# # c = engine.connect().execute("""SELECT * FROM track;""").fetchone()
# # print(c)
# sqlalchemy.exc.OperationalError: (psycopg2.OperationalError)
# (Background on this error at: https://sqlalche.me/e/14/e3q8)


# import psycopg2
# from param import host, user, password, db_name
# connection = psycopg2.connect(
#     host=host,
#     user=user,
#     password=password,
#     database=db_name
# )
# with connection.cursor() as cursor:
#     cursor.execute(
#         "SELECT version();"
#     )
#     print(cursor.fetchone())
# psycopg2.OperationalError
