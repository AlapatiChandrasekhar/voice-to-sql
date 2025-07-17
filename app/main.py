# app/main.py

from .transcription import get_transcript_from_text
from .text_to_sql import generate_sql_query

def main():
    """
    Main function to run the Voice-to-SQL application.
    """
    # 1. Get user input (for now, we'll hardcode it)
    user_query = "Show me all customers from the USA"
    print(f"User Input: '{user_query}'")

    # 2. Convert speech to text (using our mock function)
    transcribed_text = get_transcript_from_text(user_query)

    # 3. Generate SQL from the text (using our mock function)
    sql_query = generate_sql_query(transcribed_text)
    
    print("\n--------------------------")
    print("✅ Generated SQL Query:")
    print(sql_query)
    print("--------------------------\n")
    
    # 4. TODO: Connect to the database and execute the query.
    # 5. TODO: Display the results to the user.
    print("Next steps: Implement database connection and query execution.")


if __name__ == "__main__":
    main()