import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

def get_authors():
    response = supabase.table("author").select("*").execute()
    return response.data

if __name__ == "__main__":
    data = get_authors()
    print(data)