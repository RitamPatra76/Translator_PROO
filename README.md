# Translator_PROO

This project is a web-based multilingual translation application developed using **Streamlit** and **Hugging Face's Transformers** library. It allows users to input text in any language and translate it into one of five supported languages: **Bengali**, **Gujarati**, **Kannada**, **Telugu**, and **English**. check out this on hugging face space : https://huggingface.co/spaces/ritampatra/Translator_PROO
### Key Features

- **Simple Interface**: An intuitive UI that lets users easily input text and select the desired target language.
- **Multilingual Capabilities**: Supports translations between English and four major Indian languages, making it versatile for a diverse user base.
- **Optimized Performance**: Utilizes caching to minimize load times, ensuring quick and efficient translations.
- **Extendable**: Easily customizable to add more languages and enhance functionality.

### How It Works

1. **Input**: Users provide the text they want to translate.
2. **Language Selection**: Users choose their target language from the available options.
3. **Translation**: The app processes the input using the `facebook/mbart-large-50-many-to-many-mmt` model and returns the translated text.

### Future Enhancements

- **Additional Languages**: Expand the list of supported languages to cover more regions.
- **UI/UX Improvements**: Enhance the visual design and user experience.
- **Model Efficiency**: Integrate more optimized models to further reduce translation time.
