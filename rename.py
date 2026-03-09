import os
import random

# Folder containing the images
folder = r"C:\Users\pcshop\Documents\GitHub\lpk2026.github.io\prom_pics"

# Get all png files
files = [f for f in os.listdir(folder) if f.lower().endswith(".jpeg")]

# Shuffle order randomly
random.shuffle(files)

# Rename files
for i, file in enumerate(files, start=1):
    old_path = os.path.join(folder, file)
    new_name = f"prom_{i}.png"
    new_path = os.path.join(folder, new_name)
    
    os.rename(old_path, new_path)

print("Done! Images renamed randomly.")