create table roadmarkers.marker (
	id int(11) not null AUTO_INCREMENT,
	lat double(20,18),
	lng double(20,18),
	description varchar(200),
	primary key ( id )
);