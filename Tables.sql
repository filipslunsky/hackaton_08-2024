CREATE TABLE users (
    ID SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
	age VARCHAR(255),
	weight VARCHAR(255)
);

CREATE TABLE exercise (
    ID SERIAL PRIMARY KEY,
    exercise_type VARCHAR(255),
    exercise_reps VARCHAR(255),
	exercise_sets VARCHAR(255)
);

CREATE TABLE food (
    ID SERIAL PRIMARY KEY,
    food_name VARCHAR(255),
    serving_size VARCHAR(255),
	calories VARCHAR(255)
)