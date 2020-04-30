CREATE TABLE accident (
    timestamp        TIMESTAMP NOT NULL,
    title            VARCHAR2(128) NOT NULL,
    place_place_id   INTEGER NOT NULL
);

ALTER TABLE accident ADD CONSTRAINT accident_pk PRIMARY KEY ( timestamp,
                                                              place_place_id );

CREATE TABLE place (
    place_id    INTEGER NOT NULL,
    address     VARCHAR2(128) NOT NULL,
    town_town   VARCHAR2(50) NOT NULL
);

ALTER TABLE place ADD CONSTRAINT place_pk PRIMARY KEY ( place_id );

ALTER TABLE place ADD CONSTRAINT place_address_town_un UNIQUE ( address,
                                                                town_town );

CREATE TABLE town (
    town VARCHAR2(50) NOT NULL
);

ALTER TABLE town ADD CONSTRAINT town_pk PRIMARY KEY ( town );

ALTER TABLE accident
    ADD CONSTRAINT accident_place_fk FOREIGN KEY ( place_place_id )
        REFERENCES place ( place_id );

ALTER TABLE place
    ADD CONSTRAINT place_town_fk FOREIGN KEY ( town_town )
        REFERENCES town ( town );
