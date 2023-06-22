CREATE TABLE piloto (
	id serial PRIMARY KEY,
	name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	email VARCHAR (150)
);

CREATE TABLE avion (
	id serial PRIMARY KEY,
	modelo VARCHAR (50) NOT NULL,
	color VARCHAR (50) NOT NULL,
	fk_piloto integer,
	CONSTRAINT avion_frkey FOREIGN KEY (fk_piloto) 
	REFERENCES piloto (id)
);

CREATE TABLE hangar (
	id serial PRIMARY KEY,
	sector VARCHAR (50) NOT NULL,
	aeropuerto VARCHAR (50) NOT NULL,
	fk_avion integer,
	CONSTRAINT hangar_frkey FOREIGN KEY (fk_avion) 
	REFERENCES avion (id)
);
