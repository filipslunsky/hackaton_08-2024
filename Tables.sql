CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
	height VARCHAR(255),
	weight VARCHAR(255),
    birth_date DATE
);

CREATE TABLE exercise (
    exercise_id SERIAL PRIMARY KEY,
    exercise_type VARCHAR(255),
    exercise_reps VARCHAR(255),
    exercise_sets VARCHAR(255),
    exercise_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE RESTRICT
);

CREATE TABLE food (
    food_id SERIAL PRIMARY KEY,
    food_name VARCHAR(255),
    serving_size VARCHAR(255),
    calories VARCHAR(255),
    food_date DATE,
    fk_user_id INT,
    CONSTRAINT fk_user_food FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE RESTRICT
);

SELECT * FROM users
