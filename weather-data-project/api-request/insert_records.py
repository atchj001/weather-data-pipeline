import os
import psycopg2
from api_request import mock_fetch_data, fetch_data


def connect_to_db():
    print("Connecting to PostgreSQL database...")

    host = os.getenv("PGHOST", "db")
    port = int(os.getenv("PGPORT", "5432"))
    dbname = os.getenv("PGDATABASE", "db")
    user = os.getenv("PGUSER", "db_user")
    password = os.getenv("PGPASSWORD", "db_password")

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password,
        )
        return conn
    except psycopg2.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        raise


def create_table(conn):
    print("Creating table if not exists...")
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE SCHEMA IF NOT EXISTS dev;
                CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature FLOAT,
                    weather_descriptions TEXT,
                    wind_speed FLOAT,
                    time TIMESTAMP,
                    inserted_at TIMESTAMP DEFAULT NOW(),
                    utc_offset TEXT
                );
            """)
        conn.commit()
        print("Table created successfully or already exists.")
    except psycopg2.Error as e:
        print(f"An error occurred while creating the table: {e}")
        conn.rollback()
        raise


def insert_records(conn, data):
    print("Inserting weather data into the database...")
    try:
        weather = data["current"]
        location = data["location"]

        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO dev.raw_weather_data (
                    city,
                    temperature,
                    weather_descriptions,
                    wind_speed,
                    time,
                    inserted_at,
                    utc_offset
                ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
            """, (
                location["name"],
                weather["temperature"],
                weather["weather_descriptions"][0],
                weather["wind_speed"],
                location["localtime"],
                location["utc_offset"],
            ))
        conn.commit()
        print("Data inserted successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred while inserting data: {e}")
        conn.rollback()
        raise


def main():
    conn = None
    try:
        #data = mock_fetch_data()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred during execution: {e}")
        raise
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")



