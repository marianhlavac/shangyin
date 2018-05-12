CREATE TABLE user ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  fullname TEXT,
  department TEXT,
  password TEXT
);
  
CREATE TABLE card ( 
  id TEXT PRIMARY KEY,
  user_id INTEGER NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user(id)
);
  
CREATE TABLE coffee ( 
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  logged DATETIME,
  department TEXT,
  milk BOOL,
  FOREIGN KEY (user_id) REFERENCES user(id)
);