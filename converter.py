
from weasyprint import HTML, CSS
import os

def convert_to_pdf(html_path, css_path, output_pdf):
    """
    Convert the HTML and CSS files to a PDF file.

    Args:
        html_path (str): Path to the HTML file.
        css_path (str): Path to the CSS file.
        output_pdf (str): Path to the output PDF file.
    """
    html = HTML(filename=html_path)
    css = CSS(filename=css_path)
    html.write_pdf(output_pdf, stylesheets=[css])

if __name__ == "__main__":
    """
    Command line usage:
    python converter.py
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(base_dir, "cv.html")
    css_file = os.path.join(base_dir, "cv.css")
    output_pdf = os.path.join(base_dir, "cv.pdf")
    convert_to_pdf(html_file, css_file, output_pdf)
