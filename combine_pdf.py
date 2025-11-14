import pypdf
import sys

my_inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger =pypdf.PdfWriter()
    for pdf in pdf_list:
        print("Processing", pdf)
        merger.append(pdf)
    merger.write("combined_files.pdf")

    my_watermark = pypdf.PdfReader(open("wtr.pdf", "rb")).pages[0]
    my_original_file =pypdf.PdfWriter(open("combined_files.pdf", "rb"))
    output_file = pypdf.PdfWriter()
    for page in my_original_file.pages:
        
        page.merge_page(my_watermark, over=False)
        output_file.add_page(page)

    with open("my_modified_file.pdf", "wb") as f:
        output_file.write(f)


if __name__ == "__main__":
    pdf_combiner(my_inputs)