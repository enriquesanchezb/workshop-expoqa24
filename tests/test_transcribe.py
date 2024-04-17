import os

from src.transcribe import transcribe_audio


def test_transcribe_audio_success():
    audio_file = os.path.join(os.path.dirname(__file__), "samples/test.mp3")
    expected_text = "This is a test"
    assert transcribe_audio(audio_file) == expected_text


def test_transcribe_audio_exception():
    audio_file = ""
    expected_text = ""
    assert transcribe_audio(audio_file) == expected_text
