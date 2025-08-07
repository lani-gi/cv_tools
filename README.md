# Project Structure

This workspace contains the following main files:

- `cv.html`: The main HTML file for the CV. It includes:
  - Sidebar with contact info, technical and professional skills, languages, and hobbies.
  - Main content with profile summary, professional experience, education, and an additional section for legend and social links.
- `cv.css`: The stylesheet for both screen and print. It features:
  - Modern sidebar and main content design.
  - Print-optimized layout for single-page PDF export.
  - Styles for legend and social links, including flexbox alignment and responsive adjustments.
  - Consolidated `@media print` block for all print rules.
- `converter.py`: (if present) Python script for converting HTML+CSS to PDF, likely using WeasyPrint or similar ( You need to install weasyprint and GTK3 on windows).

## Key Features
- Responsive and print-friendly CV layout.
- Sidebar and main content are visually distinct and well-organized.
- Legend and social links are styled for clarity and modern appearance.

## How to Use
- Edit `cv.html` and `cv.css` to update your CV content and design.
- Use the print styles or `python converter.py` to export a single-page PDF with optimal layout.
- Add or update social links in the `links` section of `cv.html`.
---
