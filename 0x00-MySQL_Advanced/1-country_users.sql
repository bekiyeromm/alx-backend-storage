-- creates a table users following attribute id,email.name,country
CREATE TABLE IF NOT EXISTS users(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE NOT NULL,
	name VARCHAR(255),
	country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
	);
