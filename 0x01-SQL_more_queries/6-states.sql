-- CREATE DATABASE hbtn_0d_usa AND TABLE states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(256));
