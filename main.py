import sqlalchemy
db = 'postgresql://egor:270194@localhost/music1'
engine = sqlalchemy.create_engine(db)
print(engine) #Результат - Engine(postgresql://postgres:***@localhost:5432/music1_1)

# название и год выхода альбомов, вышедших в 2018 году;
engine.connect()
c = engine.connect().execute("""SELECT name_albumn, age FROM albumn WHERE age = 2018""").fetchall()
# print(c)

# # название и продолжительность самого длительного трека;
c = engine.connect().execute("""SELECT track_name, duration FROM track WHERE duration = (SELECT MAX(duration) FROM track)""").fetchall()
# print(c)

# # название треков, продолжительность которых не менее 3,5 минуты
c = engine.connect().execute("""SELECT track_name, duration FROM track WHERE duration >= 3.5""").fetchall()
# print(c)

# #названия сборников, вышедших в период с 2018 по 2020 год включительно
c = engine.connect().execute("""SELECT name_playlist FROM playlist WHERE age_playlist BETWEEN 2018 AND 2020""").fetchall()
# print(c)
# # исполнители, чье имя состоит из 1 слова
c = engine.connect().execute("""SELECT artist_name FROM artist WHERE artist_name NOT LIKE '%% %%';""").fetchall()
# print(c)
# #название треков, которые содержат слово "мой"/"my"
c = engine.connect().execute("""SELECT track_name FROM track WHERE track_name LIKE '%%my%%' or track_name LIKE '%%мой%%';""").fetchall()
print(c)

