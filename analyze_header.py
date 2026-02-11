# /// script
# dependencies = ["pypdf"]
# ///
import pypdf

try:
    reader = pypdf.PdfReader("62451.pdf")
    # Extract just the first page to analyze headers/metadata
    if len(reader.pages) > 0:
        text = reader.pages[0].extract_text()
        with open("header_sample.txt", "w") as f:
            f.write(text)
        print("Successfully extracted first page to header_sample.txt")
    else:
        print("PDF has no pages")
except Exception as e:
    print(f"Error: {e}")
