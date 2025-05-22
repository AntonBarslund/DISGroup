CREATE TABLE IF NOT EXISTS kucourses1 (
    course_id VARCHAR(255) PRIMARY KEY NOT NULL,
    title VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),
    level VARCHAR(10) NOT NULL,
    length FLOAT NOT NULL,
    timeslot VARCHAR(255) NOT NULL,
    block_group VARCHAR(10) NOT NULL,
    description TEXT NOT NULL,
    pass_pct FLOAT NOT NULL,
    median FLOAT NOT NULL,
    mean FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS exam_types (
    exam_type_id INT PRIMARY KEY NOT NULL,
    exam_type VARCHAR(255) NOT NULL
);


-- Create 'users' table
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Insert sample users
INSERT INTO users (name) VALUES
('Wally McWiggle'),
('Bubbles O''Snort'),
('Pickle Von Quirk'),
('Noodle McDoodle'),
('Fizzle McSprankle');

-- Create 'scores' table
DROP TABLE IF EXISTS scores;
CREATE TABLE scores (
    score_id SERIAL PRIMARY KEY,  -- SERIAL is PostgreSQL auto-increment
    user_id INT NOT NULL,
    score_value INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert scores
INSERT INTO scores (user_id, score_value) VALUES
(5, 88),
(2, 75),
(3, 90),
(1, 82),
(4, 91),
(2, 77),
(1, 65),
(5, 94),
(3, 73),
(2, 80),
(1, 70),
(2, 85),
(3, 78),
(4, 89),
(5, 95);
