CREATE TABLE user ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  fullname TEXT,
  department TEXT,
  password TEXT
);
  
CREATE TABLE card ( 
  id TEXT PRIMARY KEY,
  user_id INTEGER NULL,
  FOREIGN KEY (user_id) REFERENCES user(id)
);
  
CREATE TABLE coffee ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  card_id INTEGER NOT NULL,
  logged DATETIME,
  milk BOOL NOT NULL,
  FOREIGN KEY (card_id) REFERENCES card(id)
);