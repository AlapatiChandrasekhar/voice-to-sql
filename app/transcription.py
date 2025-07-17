# app/transcription.py

def get_transcript_from_text(text_input: str) -> str:
    """
    Mock function for speech-to-text.
    In the future, this will be replaced with a call to the Whisper API.
    For now, it simply returns the text it was given.
    """
    print("🎤 Mock Transcription: Using provided text directly.")
    return text_input