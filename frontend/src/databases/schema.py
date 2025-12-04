# Create the database schema for the frontend application
import sqlite3

connection_meals = sqlite3.connect('meals.db')
connection_foods = sqlite3.connect('foods.db')

cursor_meals = connection_meals.cursor()
cursor_foods = connection_foods.cursor()

# Drop existing tables if they exist
cursor_meals.execute('DROP TABLE IF EXISTS meals')
cursor_foods.execute('DROP TABLE IF EXISTS foods')

# Create new tables
meal_creation_query = '''
CREATE TABLE meals (
    id Integer PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    energy_kcal REAL NOT NULL,
    Fat_g REAL NOT NULL,
    Carbohydrates_g REAL NOT NULL,
    Protein_g REAL NOT NULL,
    Sugar_g REAL NOT NULL,
    Fiber_g REAL NOT NULL,
    Sodium_mg REAL NOT NULL,
    ingredients TEXT NOT NULL
    );
    '''

food_creation_query = '''
CREATE TABLE foods (
    id Integer PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    energy_kcal REAL NOT NULL,
    Fat_g REAL NOT NULL,
    Carbohydrates_g REAL NOT NULL,
    Protein_g REAL NOT NULL,
    Sugar_g REAL NOT NULL,
    Fiber_g REAL NOT NULL,
    Sodium_mg REAL NOT NULL
    );
    '''

try:
    cursor_meals.execute(meal_creation_query)
    cursor_foods.execute(food_creation_query)
    print("Database schema created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    connection_meals.commit()
    connection_foods.commit()
    connection_meals.close()
    connection_foods.close()