#!/usr/bin/python3

import os
import argparse  
import re
import time
import pyfiglet  

def display_ascii_art():
    ascii_art = pyfiglet.figlet_format("DDHunter")
    print(ascii_art)
    print("By Alayna Ferdarko")

def search_dd_file(dd_file_path, output_dir):
    file_signatures = {
        "jpg": b"\xFF\xD8\xFF",
        "gif": b"GIF",  
        "png": b"\x89PNG\x0D\x0A\x1A\x0A",
        "mp4": b"ftyp",  
        "mp3": b"\x49\x44\x33",  
        "pdf": b"%PDF",  
        "docx": b"\x50\x4B\x03\x04",  
        "xlsx": b"\x50\x4B\x03\x04",
        "pptx": b"\x50\x4B\x03\x04"
    }

    os.makedirs(output_dir, exist_ok=True)
    file_count_dict = {key: 0 for key in file_signatures.keys()}

    start_time = time.time()
    file_size = os.path.getsize(dd_file_path)
    total_bytes_processed = 0

    try:
        with open(dd_file_path, "rb") as dd_file:
            chunk_size = 10 * 1024 * 1024  
            offset = 0
            
            while chunk := dd_file.read(chunk_size):
                total_bytes_processed += len(chunk)
                progress = (total_bytes_processed / file_size) * 100
                elapsed_time = time.time() - start_time
                estimated_time_remaining = (elapsed_time / total_bytes_processed) * (file_size - total_bytes_processed)
                print(f"Progress: {progress:.2f}% | Estimated time remaining: {estimated_time_remaining / 60:.2f} minutes", end="\r")

                for file_type, signature in file_signatures.items():
                    offset_in_chunk = 0

                    while True:
                        index = chunk.find(signature, offset_in_chunk)
                        if index == -1:
                            break

                        file_count_dict[file_type] += 1
                        file_count = file_count_dict[file_type]
                        output_file_path = os.path.join(output_dir, f"recovered_{file_type}_{file_count}.{file_type}")

                        with open(output_file_path, "wb") as output_file:
                            output_file.write(chunk[index:index + 10 * 1024 * 1024])  

                        print(f"Recovered {file_type} file at offset {offset + index}: {output_file_path}")
                        offset_in_chunk = index + len(signature)
                
                offset += len(chunk)

        print("\nRecovery summary:")
        for file_type, count in file_count_dict.items():
            if count > 0:
                print(f"  {count} {file_type} files recovered")
    except FileNotFoundError:
        print(f"File not found: {dd_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    display_ascii_art()
    print("DDHunter is running. Please wait while your image is parsed, and your files are recovered.")
    parser = argparse.ArgumentParser(description="File carving tool to recover files from a .dd image")
    parser.add_argument("dd_image_path", help="Path to the .dd or .001 image file")
    parser.add_argument("recovery_folder", help="Directory where recovered files will be saved")
    args = parser.parse_args()
    search_dd_file(args.dd_image_path, args.recovery_folder)

if __name__ == "__main__":
    main()
