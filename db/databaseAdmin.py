import sqlite3
import os
from tabulate import tabulate
class dbAdmin:
    def list_tables():
        currentPath=os.getcwd()
        database= f"{currentPath}/../instance/leoPhisher.db"
        

        try:
            conn = sqlite3.connect(database)
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

            table_names = cursor.fetchall()

            print("Tables in the database:")
            for i, table in enumerate(table_names, start=1):
                print(f"{i}. {table[0]}")

            table_selection = input("Enter the number of the table you want to select: ")

            if not table_selection.isdigit() or int(table_selection) < 1 or int(table_selection) > len(table_names):
                print("Invalid table selection.")
                return

            selected_table = table_names[int(table_selection) - 1][0]

            cursor.execute(f"SELECT * FROM {selected_table}")
            rows = cursor.fetchall()

            headers = [description[0] for description in cursor.description]
            print(f"\nRows in table '{selected_table}':")
            print(tabulate(rows, headers=headers))

            action = input("Enter 'd' to delete a row, 'drop' to drop the table, or 'q' to quit: ")

            if action.lower() == 'd':
                row_id = input("Enter the ID of the row you want to delete: ")
                if row_id.isdigit():
                    
                    cursor.execute(f"DELETE FROM {selected_table} WHERE ID = ?", (row_id,))
                    conn.commit()
                    print("Row deleted successfully.")
                else:
                    print("Invalid row ID.")
            elif action.lower() == 'drop':
                confirm = input(f"Are you sure you want to drop the table '{selected_table}'? (y/n): ")
                if confirm.lower() == 'y':
                    cursor.execute(f"DROP TABLE IF EXISTS {selected_table}")
                    conn.commit()
                    print("Table dropped successfully.")
                else:
                    print("Table drop operation cancelled.")
            elif action.lower() == 'q':
                print("Quitting...")
            else:
                print("Invalid action.")

            cursor.close()
            conn.close()
        except sqlite3.Error as e:
            print("An error occurred:", e)

    database_path = "./instance/leoPhisher.db"