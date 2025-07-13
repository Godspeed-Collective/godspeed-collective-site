import os
import json
import re

# Folder mapping: folder name → JSON key
gallery_paths = {
    "assets/images/car_photos": "car_photos",
    "assets/images/people_portraits": "people_portraits",
    "assets/images/cinematic_landscape": "cinematic_landscape",
    "assets/videos/portrait": "portrait_videos",
    "assets/videos/landscape": "landscape_videos"
}

output = {}

def extract_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

for folder, key in gallery_paths.items():
    if os.path.exists(folder):
        files = sorted([
            os.path.join(folder, f).replace("\\", "/")
            for f in os.listdir(folder)
            if not f.startswith(".") and f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4'))
        ], key=lambda f: extract_number(os.path.basename(f)))
        output[key] = files
    else:
        output[key] = []

with open("gallery.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ gallery.json created with natural numeric sorting.")