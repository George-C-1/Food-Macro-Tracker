# This file is to navigate food queries in the database
import sqlite3

def get_connection():
    return sqlite3.connect('food_database.db')

def add_food_query(name, energy_kcal, fat_g, carbohydrates_g, protein_g, sugar_g, fiber_g, sodium_mg):
    with get_connection() as conn: # with statement ensures the connection is closed after use
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO foods (name, energy_kcal, Fat_g, Carbohydrates_g, Protein_g, Sugar_g, Fiber_g, Sodium_mg)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, energy_kcal, fat_g, carbohydrates_g, protein_g, sugar_g, fiber_g, sodium_mg))
        conn.commit()

def get_food_by_name(name):
    with get_connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM foods WHERE name = (name)
            ''', (name)
        )
        return cursor.fetchall()
    cursor.commit()

def delete_ingredient_by_name(name):
    with get_connection as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            DELETE * FROM foods WHERE name = (name)
            ''', (name)
        )