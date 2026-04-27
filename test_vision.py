"""Test vision support for providers"""
import sys, os, time
if sys.platform == "win32":
    os.system("")
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

from g4f.client import Client
import g4f
from PIL import Image
import io, base64

# Create dummy image
img = Image.new('RGB', (100, 100), color='red')
buf = io.BytesIO()
img.save(buf, format='JPEG')
img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

client = Client()

providers = [g4f.Provider.PollinationsAI, g4f.Provider.BlackboxPro, g4f.Provider.DeepInfra]

for p in providers:
    print(f"\n--- Testing {p.__name__} ---")
    try:
        model = getattr(p, 'default_model', '') or 'gpt-4o-mini'
        print(f"Using model: {model}")
        
        response = client.chat.completions.create(
            model=model,
            provider=p,
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": "What color is this image?"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
                ]}
            ]
        )
        print(f"SUCCESS: {response.choices[0].message.content[:100]}")
    except Exception as e:
        print(f"ERROR: {e}")
