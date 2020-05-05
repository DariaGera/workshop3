create table placce(
    place_id INTEGER NOT NULL,
    twp VARCHAR2(128) NOT NULL,
    addr VARCHAR2(128) NOT NULL
);

insert into placce(place_id, twp, addr) values (1, 'first', 'first');
insert into placce(place_id, twp, addr) values (2, 'first', 'second');
insert into placce(place_id, twp, addr) values (3, 'first', 'third');
insert into placce(place_id, twp, addr) values (4, 'second', 'first');
insert into placce(place_id, twp, addr) values (5, 'third', 'first');
insert into placce(place_id, twp, addr) values (6, 'third', 'second');
insert into placce(place_id, twp, addr) values (7, 'third', 'third');
insert into placce(place_id, twp, addr) values (8, 'third', 'forth');

create table accidento(
    timestamp TIMESTAMP NOT NULL,
    title VARCHAR2(128) NOT NULL,
    place_id INTEGER NOT NULL
);
insert into accidento(timestamp, title, place_id) values (to_timestamp('12-AUG-18 10.07.39.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'EMS: RESPIRATORY EMERGENCY', 1);
insert into accidento(timestamp, title, place_id) values (to_timestamp('17-OCT-18 06.26.46.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'Fire: FIRE ALARM', 2);
insert into accidento(timestamp, title, place_id) values (to_timestamp('30-JUL-19 04.04.18.000000000 PM','DD-MON-RR HH.MI.SSXFF AM'),'Traffic: VEHICLE ACCIDENT -', 2);
insert into accidento(timestamp, title, place_id) values (to_timestamp('24-NOV-19 09.11.32.000000000 AM','DD-MON-RR HH.MI.SSXFF AM'),'Traffic: VEHICLE ACCIDENT -', 6);

-----------creating test view---------------------------
CREATE OR REPLACE VIEW full_accident_table AS
    SELECT
        placce.twp,
        placce.addr,
        accidento.timestamp,
        accidento.title
    FROM
             accidento
        JOIN placce ON accidento.place_id = placce.place_id;
 
 
 
 
 
--creating--new--right--view---------------------------------------------
CREATE OR REPLACE VIEW full_table AS
    SELECT
        place.town_town,
        place.address,
        accident.timestamp,
        accident.title
    FROM
             accident
        JOIN place ON accident.place_place_id = place.place_id;    
        
