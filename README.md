# voice-translator

Training project based in [Mouredev](https://gist.github.com/mouredev/0ea42112751f0187d90d5403d1f333e2) example.

The project use two different APIs to get you audio translated in the language you want.
This example it's configured to save your audio in 🇪🇸 and return it in 🇬🇧, 🇮🇹, 🇫🇷, 🇩🇪.

The project use different APIs / libraries:

- [Whisper](https://github.com/openai/whisper) which we use locally and not calling directly their API in the cloud (free). We use Whisper to transcribe the audio into text.
- [Translate](https://pypi.org/project/translate/) python library to translate text in different languages
- [elevenlabs.io](elevenlabs.io) allow us create audio in different languages based in text

## How to install

1. Install python 3 in your machine

2. Clone the repo

3. Create a virtual environment in the main folder of the repo

   ```
   python3 -m venv .venv

   source .venv/bin/activate
   ```

4. Install dependencies (it will take the onces defined in the requirements.txt file)

   ```
   pip install
   ```

5. Sign up in [elevenlabs.io](elevenlabs.io) and create you own API key for the API we will use in the project

6. Create your own `.env` file based in the `.env.template` and paste your API key
   ```
   ELEVENLABS_API_KEY=
   ```
7. Run the python project

   ```
   python -u main.py
   ```
