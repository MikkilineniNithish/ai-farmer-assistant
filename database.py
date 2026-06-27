import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(override=True)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


def save_conversation(city: str, question: str, answer: str, user_id: str = None):
    try:
        data = {
            "city": city,
            "question": question,
            "answer": answer
        }
        if user_id:
            data["user_id"] = user_id
        supabase.table("conversations").insert(data).execute()
        print("✅ Conversation saved!")
    except Exception as e:
        print(f"❌ Error saving: {e}")


def get_conversations(limit: int = 20, user_id: str = None):
    try:
        query = supabase.table("conversations").select("*").order("created_at", desc=True).limit(limit)
        if user_id:
            query = query.eq("user_id", user_id)
        result = query.execute()
        return result.data
    except Exception as e:
        print(f"❌ Error fetching: {e}")
        return []