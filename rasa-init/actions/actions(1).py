from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pyodbc

class QueryDatabaseAction(Action):
    def name(self):
        return "action_query_database"

    def run(self, dispatcher, tracker, domain):
        try:
            # Define your SQL Server connection details
            server = "localhost"
            database = "aspnet-Store"
            port = "1433"
            username = "sa"
            password = "123123"
            
            # Establish a connection to the SQL Server database
            connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
            connection = pyodbc.connect(connection_string)

            # Example: Fetch data from the database
            cursor = connection.cursor()
            cursor.execute("SELECT Id, Name, Image FROM Products")
            results  = cursor.fetchall()

            if results:
                for result in results:
                    # Extract data from each result
                    product_id, product_name, image = result

                    slot_values = {
                        "product_id": product_id,
                        "product_name": product_name,
                        "product_image": image
                    }

                    # Send the response for each product
                    dispatcher.utter_message(template="utter_product_info", **slot_values)
            else:
                dispatcher.utter_message("No data found")
            
            connection.close()
            return []
        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")
            return []

