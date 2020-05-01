CREATE TABLE plc (
    p_id     INTEGER NOT NULL,
    town     VARCHAR2(128) NOT NULL,
    address  VARCHAR2(128) NOT NULL
);

DECLARE
    amount  plc.p_id%TYPE := 6;
    rown   plc.p_id%TYPE := 0;
    namet  plc.town%TYPE;
    namea  plc.address%TYPE;
    
BEGIN
    FOR i IN 1..amount LOOP
        SELECT MIN(place_id) INTO rown FROM placce WHERE place_id > rown;
        SELECT twp, addr INTO namet, namea FROM placce WHERE place_id = rown;

        INSERT INTO plc (p_id, town, address) VALUES (i, namet, namea);
    END LOOP;
END;
/






    
    
 