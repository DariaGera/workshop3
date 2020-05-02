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
        
