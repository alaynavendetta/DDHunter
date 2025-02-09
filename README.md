# DD Hunter - Python  
**By Alayna Ferdarko**  
**Written on 11 December, 2024.**  
**Updated and re-released on 9 February, 2025.**  

## Overview  

**DD Hunter** is a command-line Python tool designed for file carving from `.dd` image files. It helps digital forensic investigators recover files from file slack or deleted data, where there are file headers present. This tool was created using what I had learned during my time in the **Digital Forensics** program at Bloomsburg University of Pennsylvania (2017-2020) in File Systems 1 and 2.  

So I would like to give a special thanks to **Dr. Scott Inch, Dr. John Riley, and Dr. Phil Polstra** for teaching me everything I needed to know about Digital Forensics, File Systems, and Python to make this project happen - even if it has been a few years since I was a student under their guidance. I'm proud to have been one of your students!  

The name "DD Hunter" reflects the program's purpose: it hunts down file headers in `.dd` files and recovers various types of files.  

## Supported File Types  

The program currently supports the recovery of the following file types by identifying their respective headers in the `.dd` file:  

- **JPG** (JPEG images)  
- **GIF** (Graphics Interchange Format)  
- **PNG** (Portable Network Graphics)  
- **MP4** (MPEG-4 video files)  
- **MP3** (MPEG audio files)  
- **PDF** (Portable Document Format)  
- **DOCX** (Microsoft Word files)  
- **XLSX** (Microsoft Excel files)  
- **PPTX** (Microsoft PowerPoint files)  

## Features  

- **Automatic Carving**: Scans a `.dd` file and recovers files with recognizable headers.  
- **Efficient Header Matching**: Uses signature-based matching for accurate file recovery.  
- **Supports Multiple File Types**: Recovers various document, media, and image formats.  
- **Output Directory Creation**: Automatically creates and organizes a directory for recovered files.  
- **Time Estimation**: Provides real-time progress tracking and estimates remaining recovery time.  
- **ASCII Art Banner**: Displays a startup banner to enhance the user experience.  
- **Chunk-Based Processing**: Reads large `.dd` images in 10MB chunks for better performance.  
- **Error Handling**: Gracefully handles missing or corrupted `.dd` files.  

## Requirements  

- **Python 3.x** (tested on Python 3.8+)  
- **Operating System**: Should work on most systems that support Python (Linux, Windows, macOS).  

## Installation  

### Prerequisites  

Make sure you have Python 3 installed on your system. If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).  

### Getting Started  

1. **Clone or Download the Repository**:  
   - You can download the script as a ZIP file or clone the repository using `git`:  
   
     ```bash
     git clone https://github.com/your-username/DDHunter.git
     ```
   
2. **Install Required Libraries**:  
   The tool requires `pyfiglet` for ASCII art. You can install it using:  
   
     ```bash
     pip install pyfiglet
     ```

3. **Ensure Python is in your PATH**:  
   Make sure Python 3 is installed and that the `python` command works in your terminal. You can verify this by running:  
   
   ```bash
   python --version
   ```

## Usage  

### Running the Tool  

1. Open a terminal or command prompt.  
2. Navigate to the directory where `ddhunter.py` is located.  

   Example:  
   ```bash
   cd path/to/DDHunter
   ```

3. Run the script with the following syntax:  

   ```bash
   python ddhunter.py <path_to_dd_image> <output_directory>
   ```

   Example:  
   ```bash
   python ddhunter.py "C:\path\to\your\image.dd" "C:\path\to\recovery\folder"
   ```

   - `<path_to_dd_image>`: The path to the `.dd` or `.001` image file from which files are to be recovered.  
   - `<output_directory>`: The directory where the recovered files will be saved.  

### Output  

- The program will attempt to carve and recover supported file types from the provided `.dd` file.  
- All recovered files will be saved in the specified output directory.  
- The filenames of recovered files will be based on the file type and an incrementing number.  

### Example Output:  

```bash
Recovered jpg file at offset 1234567: C:\recovered_files\recovered_jpg_1.jpg
Recovered mp4 file at offset 2345678: C:\recovered_files\recovered_mp4_1.mp4
...
Recovery summary:
  3 jpg files recovered
  2 mp4 files recovered
```

## Limitations  

- **File Integrity**: The recovered files may not always be complete or fully functional, especially for fragmented files.  
- **Partial Recovery**: Only the first 10MB of each file is currently recovered due to chunk-based extraction.  
- **No TXT Support**: Recovery of plain text files has been temporarily disabled due to performance concerns.  
- **Fixed File Size**: Some document formats (`.docx`, `.xlsx`, `.pptx`) may have incomplete data if the full file structure isn’t present.  

## Acknowledgments  

- Thank you to the Digital Forensics program and instructors at Bloomsburg University for providing the foundation for learning about file carving.  
- Thank you to my dad, Bob Ferdarko Jr., for teaching me everything I knew about computers before I went to Bloomsburg University, and for also helping me do file recovery in the past. I know you won't be able to see this thank you, but I hope that even from beyond the veil, you know what a big help and inspiration you've been with everything. **RIP: 24 Dec., 1965 – 24 June, 2024.**  
- Inspired by the techniques taught in forensic courses on manual file carving, and my father's many years of experience doing data recovery, networking, programming, and PC building.  
