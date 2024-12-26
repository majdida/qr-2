import os
from bs4 import BeautifulSoup

# Directory containing your HTML files
html_dir = r"C:/Users/cm/Desktop/New folder/2/www.qrlim.com/huqqabazgarden/catalog"

# List of specific HTML files to process (add filenames here)
files_to_process = [
    "categoryf71e.html"
    # Add any other specific filenames
]

# Initialize a counter for data keys
global_counter = 0

# Function to process specific HTML files in the directory
def process_html_files(directory, files_to_process):
    global global_counter
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file is in the list of files to process
            if file in files_to_process and file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    soup = BeautifulSoup(f, "html.parser")

                # Find all elements to update (e.g., spans with text content)
                for element in soup.find_all(["span", "div", "a", "p"]):
                    if element.string and element.string.strip():
                        element["data-key"] = f"key_{global_counter}"
                        global_counter += 1

                # Save changes back to the file
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(str(soup))

                print(f"Processed: {file_path}")

# Run the function with the specified list of files
process_html_files(html_dir, files_to_process)
print("Selected files processed!")
