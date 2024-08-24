CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
	email VARCHAR(255),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
	gender VARCHAR(255) NOT NULL,
	height SMALLINT,
	weight SMALLINT,
    birth_date DATE
);

CREATE TABLE exercise (
    exercise_id SERIAL PRIMARY KEY,
    exercise_type VARCHAR(255),
    exercise_reps VARCHAR(255),
    exercise_sets VARCHAR(255),
    exercise_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (fk_email) REFERENCES email(email) ON DELETE RESTRICT
);

CREATE TABLE food (
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR(255),
    serving_size VARCHAR(255),
    calories VARCHAR(255),
    food_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user_food FOREIGN KEY (fk_email) REFERENCES email(email) ON DELETE RESTRICT
);

-- INSERT INTO users (first_name, last_name, gender, height, weight, birth_date, email) VALUES ('John', 'Doe', 'Male', 180, 75.0, '1990-1-1', 'example@gmail.com');