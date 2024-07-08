import os
import shutil
from datetime import datetime


def create_folder_on_desktop(folder_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    folder_path = os.path.join(desktop_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def copy_and_rename_files(src_folder, dst_folder, prefix):
    if not os.path.exists(src_folder):
        print(f"Source folder does not exist: {src_folder}")
        return

    for file_name in os.listdir(src_folder):
        file_path = os.path.join(src_folder, file_name)
        if os.path.isfile(file_path):
            if not file_name.lower().endswith('.jpg'):
                new_file_name = f"{prefix}_{file_name}.png"
            else:
                new_file_name = file_name
            new_file_path = os.path.join(dst_folder, new_file_name)
            shutil.copyfile(file_path, new_file_path)
            print(f"Copied and renamed: {new_file_path}")


def copy_cached_wallpapers():
    source_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Themes', 'CachedFiles')
    target_folder = create_folder_on_desktop("Wallpapers")
    copy_and_rename_files(source_folder, target_folder, "cached")


def copy_additional_wallpapers():
    src_folder = os.path.join(os.getenv('LOCALAPPDATA'),
                              r'Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')
    dst_folder = create_folder_on_desktop("Wallpapers")
    copy_and_rename_files(src_folder, dst_folder, "additional")


def main():
    # Copy cached wallpapers
    copy_cached_wallpapers()

    # Copy additional wallpapers
    copy_additional_wallpapers()


if __name__ == "__main__":
    main()
