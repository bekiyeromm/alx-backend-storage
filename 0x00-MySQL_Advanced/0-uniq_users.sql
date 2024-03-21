-- creates a table users with id, email, name
CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL AUTO-INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL PRIMARY KEY UNIQUE,
    name VARCHAR(255)
    );