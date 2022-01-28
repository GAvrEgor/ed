import sqlalchemy
db = 'postgresql://postgres:270194@localhost/music1_1'
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

INSERT INTO category (id_category, category_name)
VALUES (1, 'Рок'),(2, 'Джаз'), (3, 'Соул'), (4, 'Классика'), (5, 'Блюз');

INSERT INTO artist (id_artist, artist_name)
VALUES (1, 'Muse'), (2, 'Papa Roach'), (3, 'Nina Simone'), (4, 'Tony Bennet'), (5, 'Marvin Brooks'), (6, 'Betty Bibbs'), (7,'Mozart'), (8, 'Bach'), (9, 'Jimmy Dawkins'), (10, 'Lafayette Leake');

INSERT INTO categoryartist (id_category, id_artist)
VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(4,7),(4,8),(5,9),(5,10);

INSERT INTO albumn (id_albumn, name_albumn, age)
VALUES (1, 'Первый', 2018), (2, 'Второй', 2002), (3, 'Третий', 2003), (4, 'Четвертый', 2018), (5, 'Пятый', 2005), (6, 'Шестой', 2006), (7, 'Седьмой', 2007), (8, 'Восьмой', 2008);

INSERT INTO ArtistAlbumn (id_artist, id_albumn)
VALUES (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 5), (8, 6), (9, 7), (10, 8);

INSERT INTO track (id_track, id_albumn, track_name, duration, artist_name)
VALUES (1, 1, 'мой трек', 3.20, 'Muse'), (2, 1, 'Песенка 2', 2.12, 'Papa Roach'), (3, 2, 'my track', 3.32, 'Nina Simone'), (4, 2, 'Песенка 4', 3.41, 'Nina Simone'), (5, 3, 'Песенка 5', 4.52, 'Tony Bennet'), (6, 3, 'Песенка 6', 3.38, 'Tony Bennet'), (7, 4, 'Песенка 7', 1.59, 'Marvin Brooks'), (8, 4, 'Песенка 8', 2.34, 'Marvin Brooks'), (9, 5, 'Песенка 9', 2.51, 'Betty Bibbs'), (10, 5, 'Песенка 10', 4.15, 'Mozart'), (11,6,'Песенка 11', 4.16, 'Bach'), (12,6,'Песенка 12', 1.58, 'Bach'), (13,7,'Песенка 13', 2.47, 'Jimmy Dawkins'), (14,7,'Песенка 14', 3.51, 'Jimmy Dawkins'), (15,8,'Песенка 15', 3.48, 'Lafayette Leake'), (16,8,'Песенка 15', 1.57, 'Lafayette Leake'), (17,8,'Песенка 16', 2.47, 'Lafayette Leake');
# ERROR: ОШИБКА:  переполнение поля numeric непонятно что переполняется и как править.
INSERT INTO playlist (Name_playlist, age_playlist, id_albumn, id_playlist)
VALUES ('list1', 2018, 1, 1), ('list2', 2012, 2, 3), ('list3', 2013, 3, 4), ('list4', 2018, 4, 5), ('list5', 2015, 5, 6),('list6', 2016, 6, 7), ('list7', 2019, 7, 8),('list8', 2020, 8, 9);

INSERT INTO TrackPlaylist (id_track, id_playlist)
VALUES (1,1), (2,1), (3,2),(4,3), (5,4), (6,5), (7,6), (8,7), (9,8), (10, 9), (11, 7), (12, 8), (13, 5), (14, 9), (15,1), (16, 9), (17,9);

# название и год выхода альбомов, вышедших в 2018 году;
SELECT name_albumn, age FROM albumn
WHERE age = 2018
# название и продолжительность самого длительного трека;
SELECT track_name, duration FROM track
WHERE duration = (SELECT MAX(duration) FROM track)
# название треков, продолжительность которых не менее 3,5 минуты
SELECT track_name, duration FROM track
WHERE duration <= 3.5
#названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT Name_playlist FROM track
WHERE age_playlist BETWEEN 2018 AND 2020
# исполнители, чье имя состоит из 1 слова
SELECT artist_name FROM artist
WHERE artist_name NOT IN '% %'
#название треков, которые содержат слово "мой"/"my"
SELECT track_name FROM track
WHERE track_name IN '%my%' or track_name IN '%мой%'
