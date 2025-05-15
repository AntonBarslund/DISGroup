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