"""
Module 4: Data Warehouse Creation Script
File: scripts/dw_create.py

This script handles the creation of the SQLite data warehouse. It creates tables
for customer, product, and sale in the 'data/smart_sale.db' database.
Each table creation is handled in a separate function for easier testing and error handling.
"""

import sqlite3
import sys
import pathlib

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger  # noqa: E402

# Constants
DW_DIR: pathlib.Path = pathlib.Path("data").joinpath("dw")
DB_PATH: pathlib.Path = DW_DIR.joinpath("smart_sales.db")

# Ensure the 'data/dw' directory exists
DW_DIR.mkdir(parents=True, exist_ok=True)

# Delete data warehouse file if it exists
if DB_PATH.exists():
    try:
        DB_PATH.unlink()  # Deletes the file
        logger.info(f"Existing database {DB_PATH} deleted.")
    except Exception as e:
        logger.error(f"Error deleting existing database {DB_PATH}: {e}")

def create_customer_table(cursor: sqlite3.Cursor) -> None:
    """Create customer table in the data warehouse."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                customerid INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                region TEXT,
                joindate TEXT  -- ISO 8601 format recommended for SQLite,
                totaltransactions INTEGER,
                loyaltystatus TEXT
            )
        """)
        logger.info("customer table created.")

        # Ensure 'totaltransactions' column exists as it is not being added
        cursor.execute("PRAGMA table_info(customer);")
        columns = [column[1] for column in cursor.fetchall()]
        if 'totaltransactions' not in columns:
            cursor.execute("ALTER TABLE customer ADD COLUMN totaltransactions INTEGER;")
            logger.info("Added 'totaltransactions' column to customer table.")

    except sqlite3.Error as e:
        logger.error(f"Error creating customer table: {e}")

def create_product_table(cursor: sqlite3.Cursor) -> None:
    """Create product table in the data warehouse."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS product (
                productid INTEGER PRIMARY KEY,
                productname TEXT NOT NULL,
                category TEXT,
                unitprice_usd REAL NOT NULL,
                daytoreceive INTEGER,
                customizable TEXT
            )
        """)
        logger.info("product table created.")
    except sqlite3.Error as e:
        logger.error(f"Error creating product table: {e}")

def create_sale_table(cursor: sqlite3.Cursor) -> None:
    """Create sale table in the data warehouse."""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale (
                transactionid INTEGER PRIMARY KEY,
                saledate TEXT -- ISO 8601 format recommended for SQLite,
                customerid INTEGER,
                productid INTEGER,
                storeid INTEGER,
                campaignid INTEGER,
                saleamount REAL NOT NULL,
                loyaltypercentage INTEGER,
                billtype TEXT
            )
        """)
        logger.info("sale table created.")

         # Ensure 'customerid' column exists as it is not being added
        cursor.execute("PRAGMA table_info(sale);")
        columns = [column[1] for column in cursor.fetchall()]
        if 'customerid' not in columns:
            cursor.execute("ALTER TABLE sale ADD COLUMN customerid INTEGER;")
            logger.info("Added 'customerid' column to sale table.")
            
    except sqlite3.Error as e:
        logger.error(f"Error creating sale table: {e}")

def create_dw() -> None:
    """Create the data warehouse by creating customer, product, and sale tables."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create tables
        create_customer_table(cursor)
        create_product_table(cursor)
        create_sale_table(cursor)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        logger.info("Data warehouse created successfully.")

    except sqlite3.Error as e:
        logger.error(f"Error connecting to the database: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

def main() -> None:
    """Main function to create the data warehouse."""
    logger.info("Starting data warehouse creation...")
    create_dw()
    logger.info("Data warehouse creation complete.")

if __name__ == "__main__":
    main()