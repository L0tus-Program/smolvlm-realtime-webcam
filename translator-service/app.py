from functools import lru_cache

from deep_translator import GoogleTranslator
from flask import Flask, jsonify, request

app = Flask(__name__)


@lru_cache(maxsize=32)
def get_translator(source: str, target: str) -> GoogleTranslator:
    return GoogleTranslator(source=source, target=target)


@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok"})


@app.get("/languages")
def languages():
    return jsonify(
        [
            {"code": "en", "name": "English"},
            {"code": "pt", "name": "Portuguese"},
        ]
    )


@app.post("/translate")
def translate():
    payload = request.get_json(silent=True) or {}

    text = payload.get("q", "")
    source = payload.get("source", "en")
    target = payload.get("target", "pt")

    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Field 'q' must be a non-empty string"}), 400
    if not isinstance(source, str) or not source.strip():
        return jsonify({"error": "Field 'source' must be a string"}), 400
    if not isinstance(target, str) or not target.strip():
        return jsonify({"error": "Field 'target' must be a string"}), 400

    try:
        translated = get_translator(source.strip(), target.strip()).translate(text)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 502

    return jsonify({"translatedText": translated})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
