import os
import shutil
import zipfile
import xml.etree.ElementTree as ET
import re
import argparse


def increment_filename(increment):
    """Create a filename with a leading zero format"""
    return "{:03}.jpg".format(increment)


def sanitize_filename(filename):
    """
    Removes invalid characters from the filename.
    """
    return re.sub(r'[\\/:"*?<>|]', "", filename)


def create_metadata():
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    summary = input("Enter the summary: ")

    root = ET.Element("ComicInfo")
    ET.SubElement(root, "Title").text = title
    ET.SubElement(root, "Author").text = author
    ET.SubElement(root, "Summary").text = summary

    tree = ET.ElementTree(root)
    tree.write("ComicInfo.xml")
    return sanitize_filename(title)


def main(parent_directory, new_directory, verbose=False):
    increment = 1  # Start the numbering from 1
    # Create the metadata file first to know the title
    title = create_metadata()

    # Create directories
    title_directory = os.path.join(new_directory, title)  # output/title/
    image_directory = os.path.join(title_directory, "images")  # output/title/images
    cbz_directory = os.path.join(title_directory, "cbz")  # output/title/cbz

    # Create the directories if they don't exist
    for directory in [title_directory, image_directory, cbz_directory]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Walk through all directories and files in the parent directory
    for root, dirs, files in os.walk(parent_directory):
        if verbose:
            print(f"\U0001F4C1 Working in directory: {root}")  # 📁

        accepted_extensions = (".jpg", ".jpeg", ".png")
        sorted_files = sorted(file for file in files if file.lower().endswith(accepted_extensions))

        for filename in sorted_files:
            # Construct the full file paths
            old_filepath = os.path.join(root, filename)
            new_filepath = os.path.join(image_directory, increment_filename(increment))

            # Copy the file to the new directory with the incremented filename
            shutil.copy2(old_filepath, new_filepath)

            # Output progress message
            if verbose:
                print(
                    f"\U0001F4CE Renaming: {filename} to {increment_filename(increment)}"
                )  # 📎

            # Increment the counter
            increment += 1

    # Create a CBZ file
    print("\U0001F4C6 Creating CBZ file...")  # 📆
    cbz_filename = os.path.join(cbz_directory, f"{title}.cbz")
    with zipfile.ZipFile(cbz_filename, "w") as comic_zip:
        # Add all files in the output directory to the CBZ file
        for foldername, subfolders, filenames in os.walk(image_directory):
            for filename in filenames:
                comic_zip.write(os.path.join(foldername, filename), filename)
        # Add the metadata file to the CBZ file
        comic_zip.write("ComicInfo.xml")

    print("\U0001F4C6 CBZ file created!")  # 📆
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "--debug", "--verbose", action="store_true", help="Display debug information"
    )
    args = parser.parse_args()

    main("./source", "./output", verbose=args.debug)
