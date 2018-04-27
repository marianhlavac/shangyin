CREATE TABLE coffees (
	logged_at datetime,
	user_id integer,
	type integer,
	division integer
);

CREATE TABLE users (
	id integer PRIMARY KEY AUTOINCREMENT,
    name text,
    division text
);
