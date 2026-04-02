import time
import os
from pathlib import Path
from process_audio import audio_to_docx  # import your converted notebook

# -------------------------------
# Config
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent
WATCH_FOLDER = str(BASE_DIR)
TEMPLATE_PATH = str(BASE_DIR / "0.docx")
PROCESSED_FOLDER = os.path.join(WATCH_FOLDER, "processed")

Path(PROCESSED_FOLDER).mkdir(exist_ok=True)

# -------------------------------
# Watch folder loop
# -------------------------------
print(f"Watching folder: {WATCH_FOLDER}")

while True:
    for file_name in os.listdir(WATCH_FOLDER):
        if file_name.lower().endswith((".m4a", ".wav", ".mp3")):
            file_path = os.path.join(WATCH_FOLDER, file_name)
            processed_path = os.path.join(PROCESSED_FOLDER, file_name)

            # Skip already processed files
            if os.path.exists(processed_path):
                continue

            print(f"Processing {file_name}...")
            try:
                docx_file = audio_to_docx(file_path, TEMPLATE_PATH, patient_name="John Doe")
                print(f"✅ Generated SOAP note: {docx_file}")

                # Move audio to processed folder
                os.rename(file_path, processed_path)
            except Exception as e:
                print(f"❌ Failed to process {file_name}: {e}")

    time.sleep(30)  # Check every 30 seconds
