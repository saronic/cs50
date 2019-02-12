create table flights (
	id serial primary key,
	origin varchar not null,
	destination varchar not null,
	duration integer not null
)

	insert into flights (origin,destination,duration) values ('Shanghai','Paris',760);
	insert into flights (origin,destination,duration) values ('New York','Tokyo',760);
	insert into flights (origin,destination,duration) values ('Moscow','Paris',760);
	insert into flights (origin,destination,duration) values ('Lima','New York',760);

	create table locations (
		id serial primary key,
		code varchar not null,
		name varchar not null
	);

	insert into locations (code,name) values ('JFK', 'New York');
	insert into locations (code,name) values ('PVG', 'Shanghai');
	insert into locations (code,name) values ('LHR', 'London');
	insert into locations (code,name) values ('SVO', 'Moscow');
	insert into locations (code,name) values ('CDG', 'Paris');
	insert into locations (code,name) values ('NRT', 'Tokyo');

	create table passengers (
		id serial primary key,
		name varchar not null,
		flight_id integer references flights
	);

	insert into passengers (name, flight_id) values ('Alice', 1);
	insert into passengers (name, flight_id) values ('Bob', 1);
	insert into passengers (name, flight_id) values ('Charlie', 2);
	insert into passengers (name, flight_id) values ('Dave', 2);
	insert into passengers (name, flight_id) values ('Erin', 4);
	insert into passengers (name, flight_id) values ('Frank', 5);
	insert into passengers (name, flight_id) values ('Grace', 5);

