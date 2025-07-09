### Multilingual NLP Translation Pipeline

This is a simple and practical multilingual NLP pipeline that can **detect the language** of any input text and **translate** it into a user-selected target language.
It supports over 100 languages using pre-trained models and offers a fallback to **Google's Gemini** API when direct translation is unavailable.

### What It Can Do

- Detect the language of any input text (using `fastText`)  
- Translate between many language pairs (using `MarianMT`)  
- Automatically fallback to Gemini if MarianMT can't handle the language pair  
 
### Project Structure

| File / Folder         | Description |
|-----------------------|-------------|
| `main.py`             | Entry point. Takes user input, detects source language, and performs translation. |
| `lang_detect.py`      | Handles language detection using the `fastText` model `lid.176.ftz`. |
| `translator.py`       | Contains MarianMT and Gemini translation logic. Falls back automatically when needed. |

### Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/multilang-nlp-pipeline.git
cd multilang-nlp-pipeline
```

### 2. Install Python dependencies

``` bash
pip install -r requirements.txt  
```

### 3. Download the fastText Language Detection Model
This project uses fastText to detect the language of the input text.
The model file is not included in the repo due to its size.

Download the model here:

https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz

Then, place it in the project root (i.e., same folder as main.py).

### 4. How to Run

``` bash
python main.py
```

### 5. Using Gemini (Optional)
If you want to enable translation fallback using Google's Gemini API, you’ll need an API key:

- Visit Google AI Studio
- Generate your API key

Paste it in main.py here:

```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
```
Gemini will only be used for fallback translation when MarianMT doesn’t support the pair.

### 6. Supported Languages
Component	Languages  
`fastText`: 176+ (for detection)  
`MarianMT`: ~100 language pairs  
`Gemini API`: Major world languages (contextual translation)  

### 7. License
This project is released under the MIT License.
Feel free to use, fork, and build upon it.

