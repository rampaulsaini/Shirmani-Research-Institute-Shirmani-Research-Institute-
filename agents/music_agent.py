"""Audio Agent: creates reusable prompt metadata; it does not fabricate audio files."""

def prompt(index, lyric, language="hi"):
    return {
        "id": index,
        "language": language,
        "lyric": lyric,
        "status": "prompt-only",
        "audio_file": None,
    }
