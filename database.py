import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(override=True)

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)


def save_conversation(city: str, question: str, answer: str):
    """Save a conversation to the database."""
    try:
        supabase.table("conversations").insert({
            "city": city,
            "question": question,
            "answer": answer
        }).execute()
        print("✅ Conversation saved!")
    except Exception as e:
        print(f"❌ Error saving: {e}")


def get_conversations(limit: int = 10):
    """Get recent conversations from database."""
    try:
        result = supabase.table("conversations").select("*").order("created_at", desc=True).limit(limit).execute()
        return result.data
    except Exception as e:
        print(f"❌ Error fetching: {e}")
        return []


if __name__ == "__main__":
    # Test save
    save_conversation("Tirupati", "Should I water my crops?", "Yes, water them today!")
    
    # Test fetch
    conversations = get_conversations()
    print(f"Found {len(conversations)} conversations:")
    for conv in conversations:
        print(f"- {conv['city']}: {conv['question'][:50]}")