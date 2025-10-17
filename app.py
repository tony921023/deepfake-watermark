# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from pathlib import Path
from werkzeug.utils import secure_filename
from datetime import datetime

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True, parents=True)
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

ALLOWED_EXTS = {"png", "jpg", "jpeg", "bmp"}

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTS

def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok", ts=datetime.utcnow().isoformat() + "Z"), 200

    @app.post("/api/embed")
    def embed():
        file = request.files.get("file")
        if not file or file.filename == "":
            return jsonify(error="missing file"), 400
        if not allowed_file(file.filename):
            return jsonify(error="unsupported file type"), 415
        fname = secure_filename(file.filename)
        save_path = UPLOAD_DIR / f"embed_{fname}"
        file.save(save_path)
        return jsonify(ok=True, action="embed", filename=fname, saved=str(save_path),
                       note="stub: replace with real embed pipeline"), 200

    @app.post("/api/detect")
    def detect():
        file = request.files.get("file")
        if not file or file.filename == "":
            return jsonify(error="missing file"), 400
        fname = secure_filename(file.filename)
        save_path = UPLOAD_DIR / f"detect_{fname}"
        file.save(save_path)
        return jsonify(ok=True, action="detect", filename=fname, tamper_score=0.12,
                       risk="low", note="stub: replace with real detector"), 200

    @app.post("/api/reveal")
    def reveal():
        file = request.files.get("file")
        if not file or file.filename == "":
            return jsonify(error="missing file"), 400
        fname = secure_filename(file.filename)
        save_path = UPLOAD_DIR / f"reveal_{fname}"
        file.save(save_path)
        out_name = f"reveal_{Path(fname).stem}.png"
        out_path = OUTPUT_DIR / out_name
        out_url = f"/download/{out_name}"  # placeholder
        return jsonify(ok=True, action="reveal", filename=fname, output=str(out_path),
                       download_hint=out_url, note="stub: generate actual reveal image here"), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=5000, debug=True)
