import sqlalchemy
db = 'postgresql://egor:270194@localhost/music1'
engine = sqlalchemy.create_engine(db)
print(engine) #Результат - Engine(postgresql://postgres:***@localhost:5432/music1_1)

engine.connect()
# количество исполнителей в каждом жанре
c = engine.connect().execute("""SELECT COUNT(artist_name) FROM artist 
JOIN categoryartist ON artist.id_artist = categoryartist.id_artist 
JOIN category ON categoryartist.id_category = category.id_category
Group by category""").fetchall()
# print(c)

# количество треков, вошедших в альбомы 2008-2018 годов;
c = engine.connect().execute("""Select count(id_track) from track
join albumn on track.id_albumn = albumn.id_albumn
where albumn.age between 2008 and 2018""").fetchall()
# print(c)

# средняя продолжительность треков по каждому альбому;
c = engine.connect().execute("""Select round(avg(duration),2) from track
 join albumn on track.id_albumn = albumn.id_albumn
 group by name_albumn""").fetchall()
# print(c)

# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
c = engine.connect().execute("""Select name_playlist from playlist
 join albumn on playlist.id_albumn = albumn.id_albumn join
artistalbumn on albumn.id_albumn = artistalbumn.id_albumn join
artist on artistalbumn.id_artist = artist.id_artist
where artist_name like 'Bach'""").fetchall()
# print(c)

# название альбомов, в которых присутствуют исполнители более 1 жанра;
c = engine.connect().execute("""Select name_albumn from albumn join
artistalbumn on albumn.id_albumn = artistalbumn.id_albumn join
artist on artistalbumn.id_artist = artist.id_artist join categoryartist
on artist.id_artist = categoryartist.id_artist join category
on categoryartist.id_category = category.id_category
group by name_albumn
having count(categoryartist.id_artist) > 1
""").fetchall()
# print(c)

# наименование треков, которые не входят в сборники
c = engine.connect().execute("""select track_name from track left join trackplaylist
on track.id_track = trackplaylist.id_track
where trackplaylist.id_track is null""").fetchall()
# print(c)

# все исполнители, которые не выпустили альбомы в 2002 году
c = engine.connect().execute("""select artist_name from artist join
artistalbumn on artist.id_artist = artistalbumn.id_artist join albumn
on artistalbumn.id_albumn = albumn.id_albumn
where artist_name not in (select artist_name from artist join
artistalbumn on artist.id_artist = artistalbumn.id_artist join albumn
on artistalbumn.id_albumn = albumn.id_albumn
 where albumn.age = 2002)""").fetchall()
# print(c)

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
c = engine.connect().execute("""select artist.artist_name, duration from artist join
 artistalbumn on artist.id_artist = artistalbumn.id_artist join
 albumn on artistalbumn.id_albumn = albumn.id_albumn join
 track on albumn.id_albumn = track.id_albumn
 where duration = (select min(duration) from track)""").fetchall()
# print(c)

# название альбомов, содержащих наименьшее количество треков.
c = engine.connect().execute("""select name_albumn, count(track_name) from albumn join
track on albumn.id_albumn = track.id_albumn
group by albumn.id_albumn
having count(track.track_name) = (select min(count) from (select name_albumn, count(track_name) from albumn join
track on albumn.id_albumn = track.id_albumn
group by albumn.id_albumn) as f)""").fetchall()
# print(c)



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
# print(c)

