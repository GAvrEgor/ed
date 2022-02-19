create table if not exists category(
	id_category serial primary key,
	category_name varchar(50) unique
);
create table if not exists artist(
	id_artist serial primary key,
	artist_name varchar(50)
);
create table if not exists CategoryArtist(
	id_category integer not null  references category(id_category),
	id_artist integer not null  references artist(id_artist),
	constraint pk primary key (id_artist, id_category)
);
create table if not exists albumn(
	id_albumn serial primary key,
	name_albumn text not null unique,
	age integer not null
);
create table if not exists ArtistAlbumn(
	id_artist integer not null references artist(id_artist),
	id_albumn integer not null references albumn(id_albumn),
	constraint pk1 primary key (id_artist, id_albumn)
);
create table if not exists track(
	id_track serial primary key,
	id_albumn integer references albumn(id_albumn),
	track_name text not null unique,
	duration numeric(3,2),
	artist_name varchar(40)
);
create table if not exists playlist(
	Name_playlist varchar(50) not null unique,
	age_playlist integer not null,
	id_albumn int not null references albumn(id_albumn),
	id_playlist serial primary key
);
create table if not exists TrackPlaylist(
	id_track int references track(id_track),
	id_playlist int references playlist(id_playlist),
	constraint pk2 primary key (id_track, id_playlist)
);

INSERT INTO category (id_category, category_name)
VALUES (1, 'Рок'),(2, 'Джаз'), (3, 'Соул'), (4, 'Классика'), (5, 'Блюз');

INSERT INTO artist (id_artist, artist_name)
VALUES (1, 'Muse'), (2, 'Papa Roach'), (3, 'Nina Simone'), (4, 'Tony Bennet'), (5, 'Marvin Brooks'), (6, 'Betty Bibbs'), (7,'Mozart'), (8, 'Bach'), (9, 'Jimmy Dawkins'), (10, 'Lafayette Leake');

INSERT INTO categoryartist (id_category, id_artist)
VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(4,7),(4,8),(5,9),(5,10),(2,1);

INSERT INTO albumn (id_albumn, name_albumn, age)
VALUES (1, 'Первый', 2018), (2, 'Второй', 2002), (3, 'Третий', 2003), (4, 'Четвертый', 2018), (5, 'Пятый', 2005), (6, 'Шестой', 2006), (7, 'Седьмой', 2007), (8, 'Восьмой', 2008);

INSERT INTO ArtistAlbumn (id_artist, id_albumn)
VALUES (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 5), (8, 6), (9, 7), (10, 8);

INSERT INTO track (id_track, id_albumn, track_name, duration, artist_name)
VALUES (1, 1, 'мой трек', 3.20, 'Muse'), (2, 1, 'Песенка 2', 2.12, 'Papa Roach'), (3, 2, 'my track', 3.32, 'Nina Simone'), (4, 2, 'Песенка 4', 3.41, 'Nina Simone'), (5, 3, 'Песенка 5', 4.52, 'Tony Bennet'), (6, 3, 'Песенка 6', 3.38, 'Tony Bennet'), (7, 4, 'Песенка 7', 1.59, 'Marvin Brooks'), (8, 4, 'Песенка 8', 2.34, 'Marvin Brooks'), (9, 5, 'Песенка 9', 2.51, 'Betty Bibbs'), (10, 5, 'Песенка 10', 4.15, 'Mozart'), (11,6,'Песенка 11', 4.16, 'Bach'), (12,6,'Песенка 12', 1.58, 'Bach'), (13,7,'Песенка 13', 2.47, 'Jimmy Dawkins'), (14,7,'Песенка 14', 3.51, 'Jimmy Dawkins'), (15,8,'Песенка 15', 3.48, 'Lafayette Leake'), (16,8,'Песенка 16', 2.47, 'Lafayette Leake');


INSERT INTO playlist (id_playlist, Name_playlist, age_playlist, id_albumn)
VALUES (1, 'list1', 2018, 1), (2, 'list2', 2012, 2), (3,'list3', 2013, 3), (4, 'list4', 2018, 4), (5, 'list5', 2015, 5), (6, 'list6', 2016, 6), (7, 'list7', 2019, 7), (8, 'list8', 2020, 8);

INSERT INTO TrackPlaylist (id_track, id_playlist)
VALUES (1,1), (3,2), (4,3), (5,4), (6,5), (7,6), (8,7), (9,8), (10, 7), (11, 7), (12, 8), (13, 5), (14, 6), (15,1), (16, 6);

update track set id_albumn = 2 where id_track = 2