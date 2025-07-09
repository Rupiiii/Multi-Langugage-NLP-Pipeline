import fasttext

MODEL_PATH = "models/lid.176.bin"

# Load the model once at the top
model = fasttext.load_model(MODEL_PATH)

def detect_language(text):
    labels, probs = model.predict(text)
    return labels[0].replace("__label__", "")


