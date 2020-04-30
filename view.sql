CREATE OR REPLACE VIEW full_accident_table AS
    SELECT
        placce.twp,
        placce.addr,
        accidento.timestamp,
        accidento.title
    FROM
             accidento
        JOIN placce ON accidento.place_id = placce.place_id;
