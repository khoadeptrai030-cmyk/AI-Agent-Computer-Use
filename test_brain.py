"""Quick test to verify the AI brain can respond."""
import sys, os
if sys.platform == "win32":
    os.system("")
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from g4f.client import Client
import g4f

client = Client()

# Test with PollinationsAI using its default model
print("Test 1: PollinationsAI with default model 'openai-fast'...")
try:
    response = client.chat.completions.create(
        model="openai-fast",
        provider=g4f.Provider.PollinationsAI,
        messages=[
            {"role": "system", "content": "You are an AI. Reply ONLY with valid JSON, no other text."},
            {"role": "user", "content": 'Reply with exactly: {"action_type": "done", "thought": "test ok", "summary": "test ok"}'}
        ]
    )
    result = response.choices[0].message.content
    print(f"SUCCESS! Response: {result[:300]}")
except Exception as e:
    print(f"ERROR: {e}")

# Test with Chatai
print("\nTest 2: Chatai with default model...")
try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        provider=g4f.Provider.Chatai,
        messages=[
            {"role": "system", "content": "You are an AI. Reply ONLY with valid JSON."},
            {"role": "user", "content": 'Reply with: {"action_type": "click", "x": 100, "y": 200, "thought": "clicking button"}'}
        ]
    )
    result = response.choices[0].message.content
    print(f"SUCCESS! Response: {result[:300]}")
except Exception as e:
    print(f"ERROR: {e}")

print("\nAll tests complete.")
