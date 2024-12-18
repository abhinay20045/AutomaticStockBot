import pdfplumber

# Open the PDF file
with pdfplumber.open("foo.pdf") as pdf:
    # Select the first page
    first_page = pdf.pages[0]
    
    # Extract text from the page
    text = first_page.extract_text()
    print(text)