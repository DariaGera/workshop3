CREATE TABLE plc (
    p_id     INTEGER NOT NULL,
    town     VARCHAR2(128) NOT NULL,
    address  VARCHAR2(128) NOT NULL
);

--------------------------------------------------------------------------------------------
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


--не--завдання,--але--рекурсія-----
with numbers(velue, n_mber) as
(
--select 1 as value from dual

select  1 as velue, (select 1 as velue from dual)*2 as n_mber from dual
union all

--select value+1 as value from numbers
select velue+1 as velue, (select (velue+1) from dual)*2 as n_mber from numbers
--where value<5
where velue <7 
)
--select value from numbers;
select * from numbers;



    
    
 
