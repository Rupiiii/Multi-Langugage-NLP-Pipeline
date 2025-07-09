from transformers import MarianMTModel, MarianTokenizer, pipeline

def translate(text, src_lang, tgt_lang):
    """
    Attempts to translate text using MarianMT (Helsinki-NLP).
    Raises ValueError if the specific model is not found.
    """
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
    except Exception as e:
        raise ValueError(f"No MarianMT model for {src_lang} → {tgt_lang}: {e}")

    # Create pipeline for translation
    translation_pipeline = pipeline("translation", model=model, tokenizer=tokenizer)
    translated = translation_pipeline(text, max_length=512, clean_up_tokenization_spaces=True)

    return translated[0]['translation_text']
