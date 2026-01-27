import os
import shutil

source_dir = r"D:\WORK\Python\USTH\practice_2\data\training_set"   # change this
target_dir = os.path.join(source_dir, "annotations")
keyword = "Annotation"
extension = ".png"

os.makedirs(target_dir, exist_ok=True)

moved_count = 0

for filename in os.listdir(source_dir):
    if keyword in filename and filename.lower().endswith(extension):
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(target_dir, filename)

        # Move file
        shutil.move(src_path, dst_path)
        moved_count += 1

print(f"Moved {moved_count} annotation PNG files to '{target_dir}'")
