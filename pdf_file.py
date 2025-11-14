# work with pdf files
import pypdf

with open("dummy.pdf", "rb") as file:
    # rb ==> read in binary mode
    reader = pypdf.PdfReader(file)
    print(reader.get_num_pages())
    print(reader.get_page(0))
    page = reader.get_page(0)
    page.rotate(90)
    writer = pypdf.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)
