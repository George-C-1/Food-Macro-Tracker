# This file is to navigate meal queries in the database
import sqlite3
from typing import List

def get_connection():
    return sqlite3.connect('meals.db')

def add_meals(name, energy_kcal, Fat_g, Carbohydrates_g, Protein_g, Sugar_g, Fiber_g, Sodium_mg, ingredients:List[str]):
    with get_connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            INSERT INTO meals (name, energy_kcal, Fat_g, Carbohydrates_g, Protein_g, Sugar_g, Fiber_g, Sodium_mg, ingredients),
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (name, energy_kcal, Fat_g, Carbohydrates_g, Protein_g, Sugar_g, Fiber_g, Sodium_mg, ingredients)
        )
        conn.commit()

def get_food_by_name(name):
    with get_connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM meals WHERE name = (?) VALUES (name)
            ''', (name)
        )

def delete_food_by_name(name):
    with get_connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            DELETE * FROM meals WHERE name = (name)
            ''', (name)
        )
        conn.commit()

def edit_foods_in_meal(name, new_ingredients: List):
    with get_connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE meals SET ingredients = (new_ingredients) WHERE name = (name)
            ''', (new_ingredients, name)
        )