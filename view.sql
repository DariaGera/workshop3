create table placce(
    place_id INTEGER NOT NULL,
    twp VARCHAR2(128) NOT NULL,
    addr VARCHAR2(128) NOT NULL
);

insert into placce(place_id, twp, addr) values (1, "first", "first");
insert into placce(place_id, twp, addr) values (2, "first", "second");
insert into placce(place_id, twp, addr) values (3, "first", "third");
insert into placce(place_id, twp, addr) values (4, "second", "first");
insert into placce(place_id, twp, addr) values (5, "third", "first");
insert into placce(place_id, twp, addr) values (6, "third", "second");
insert into placce(place_id, twp, addr) values (7, "third", "third");
insert into placce(place_id, twp, addr) values (8, "third", "forth");



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
        
