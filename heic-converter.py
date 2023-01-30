from PIL import Image
from pillow_heif import register_heif_opener
import os
import shutil
import sys

heic_original_dir_name = "heicOriginals"

def find_heic_files(directory):
    heic_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".heic")]
    print(f'{directory}: found {len(heic_files)} HEIC files')
    return heic_files

def convert_heic_to_jpg(heic_files, directory):
    if not heic_files:
        return

    heic_original_backup_dir_path = os.path.join(directory, heic_original_dir_name)
    heic_original_zip_path = heic_original_backup_dir_path + ".zip"
    if not os.path.exists(heic_original_backup_dir_path) and not os.path.isfile(heic_original_zip_path):
        os.mkdir(heic_original_backup_dir_path)
    else:
        print(f"The '{heic_original_dir_name}' folder/zip already exists in {directory}. Skipping...")
        return

    # Check no files already converted before starting
    for file in heic_files:
        new_file_path = os.path.join(directory, os.path.splitext(os.path.basename(file))[0]) + ".jpg"
        if os.path.isfile(new_file_path):
            print(f'File {new_file_path} already exists. Aborting...')
            sys.exit(1)

    for file in heic_files:
        new_file_path = os.path.join(directory, os.path.splitext(os.path.basename(file))[0]) + ".jpg"
        heic_file_backup_path = os.path.join(heic_original_backup_dir_path, os.path.basename(file))
        with Image.open(file) as im:
            im.save(new_file_path, "JPEG", exif=im.info.get("exif"))

        shutil.move(file, heic_file_backup_path)

    shutil.make_archive(heic_original_backup_dir_path, 'zip', heic_original_backup_dir_path)
    shutil.rmtree(heic_original_backup_dir_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a folder path as an argument")
    else:
        directory = sys.argv[1]

        if not os.path.exists(directory):
            print("Unable to find folder")
            sys.exit(1)

        register_heif_opener()
        for root, dirs, files in os.walk(directory):
            heic_files = find_heic_files(root)
            convert_heic_to_jpg(heic_files, root)