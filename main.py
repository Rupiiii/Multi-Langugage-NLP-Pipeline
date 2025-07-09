import re
from google.colab import userdata
import google.generativeai as genai
from lang_detect import detect_language
from translator import translate

# 👇 Securely load your Gemini API key
genai.configure(api_key="YOUR-GEMINI-KEY")

# Map language codes to full names
LANGUAGE_NAMES = {
    "en": "English", "fr": "French", "de": "German", "hi": "Hindi",
    "bn": "Bengali", "es": "Spanish", "it": "Italian", "ru": "Russian",
    "zh": "Chinese", "ja": "Japanese", "ko": "Korean", "ar": "Arabic",
    # Add more if needed
}


def translate_with_gemini(text, src_lang_name, tgt_lang_name):
    prompt = f"Translate the following from {src_lang_name} to {tgt_lang_name}:\n\n{text}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    raw = response.text.strip()

    # Find bold text
    bold_match = re.search(r"\*\*(.*?)\*\*", raw)
    
    if bold_match:
        bold_text = bold_match.group(1)

        # Remove the word "Comment" anywhere in the bold text
        cleaned_bold = re.sub(r'\b[Cc]omment\b', '', bold_text).strip()

        # Replace the original bold section with cleaned one
        raw = raw.replace(bold_match.group(0), cleaned_bold)

    return raw.strip()


text = input("Enter your text: ")
target_lang = input("Translate to which language? (e.g., en, fr, de, hi): ").strip()

src_lang = detect_language(text)
src_lang_name = LANGUAGE_NAMES.get(src_lang, src_lang)
tgt_lang_name = LANGUAGE_NAMES.get(target_lang, target_lang)

print(f"\n🌐 Detected input language: {src_lang_name}")

try:
    translated_text = translate(text, src_lang, target_lang)
    print(f"\n✅ Translated using MarianMT [{src_lang_name} → {tgt_lang_name}]:\n{translated_text}")
except ValueError:
    print(f"\n⚠️ MarianMT model not available for {src_lang_name} → {tgt_lang_name}. Using Gemini API...")
    translated_text = translate_with_gemini(text, src_lang_name, tgt_lang_name)
    print(f"\n✅ Translated using Gemini [{src_lang_name} → {tgt_lang_name}]:\n{translated_text}")

