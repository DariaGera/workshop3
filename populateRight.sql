---------------------------------------------------------------------------------
DELETE FROM mont911
WHERE
    addr IS NULL
    OR timestamp IS NULL
    OR title IS NULL
    OR twp IS NULL;
---------------------------------------------------------------------------------    

INSERT INTO town ( town )
    SELECT UNIQUE
        ( twp )
    FROM
        mont911
    WHERE
        ROWNUM < 5; -- there are 4 towns
--delete from town where exists(select * from town);

CREATE OR REPLACE VIEW plac_e AS
    SELECT DISTINCT
        ROWNUM AS place_id,
        mont911.addr,
        mont911.twp
    FROM
             mont911
        JOIN town ON mont911.twp = town.town
    WHERE
        ROWNUM < 20
    ORDER BY
        ROWNUM ASC;
--i--dont--know--how--to--insert--it--to--the--tables--(((--------------------------
CREATE TABLE placce
    AS
        ( SELECT
            place_id,
            addr,
            twp
        FROM
            plac_e
        )

CREATE TABLE accidento
    AS
        ( SELECT
            plac_e.place_id,
            mont911.timestamp,
            mont911.title
        FROM
                 mont911
            JOIN plac_e ON plac_e.addr = mont911.addr
                           AND plac_e.twp = mont911.twp
        );
        
select count(*) from accidento; --2588

