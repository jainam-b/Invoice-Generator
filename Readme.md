

```markdown
# Invoice Generator

This project automates the creation of PDF invoices from provided data using Python, Jinja2 templating, and pdfkit.

## Features

- **Professional Invoices:** Generates professional-looking PDF invoices.
- **Tax Calculation:** Supports both CGST/SGST and IGST tax calculations based on the place of supply and delivery.
- **Dynamic Totals:** Dynamically calculates totals, tax amounts, and net amounts for each item.
- **Detailed Information:** Includes detailed seller, billing, and shipping information.
- **Customizable:** Easily customizable with your company logo and authorized signature.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- pdfkit
- Jinja2
- wkhtmltopdf (required by pdfkit for PDF rendering)

### Installing Dependencies

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/invoice-generator.git
   cd invoice-generator
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install wkhtmltopdf:
   - **Ubuntu/Debian:**
     ```bash
     sudo apt-get install wkhtmltopdf
     ```
   - **macOS:**
     ```bash
     brew install wkhtmltopdf
     ```
   - **Windows:** Download and install from [wkhtmltopdf website](https://wkhtmltopdf.org/downloads.html).

## Usage

1. **Prepare Your Data:**
   - Update `seller_details`, `billing_details`, `shipping_details`, `order_details`, `invoice_details`, and `items` dictionaries in `invoice_generator.py`.

2. **Customize Invoice Layout (Optional):**
   - Modify the HTML structure in `invoice_template.html` to adjust the invoice layout.

3. **Generate Invoice:**
   ```bash
   python invoice_generator.py
   ```

4. **View Invoice:**
   - The generated PDF invoice will be saved as `invoice.pdf` in the current directory.

## Customization

- **Invoice Template:** Adjust `invoice_template.html` to change the layout, styling, or content of the invoice.
- **Data Formatting:** Modify `format_currency` and `amount_in_words` functions in `invoice_generator.py` as per your requirements.
- **Images:** Replace `logo.png` and `signature.png` placeholders with your actual logo and signature images.

## Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

### Changes Made:

- **Features Section Enhancement:** Emphasized key features with bullet points for clarity.
- **Prerequisites Section:** Provided a subsection on installing dependencies for better organization.
- **Detailed Installation Instructions:** Included steps for cloning the repository, installing Python dependencies from `requirements.txt`, and installing `wkhtmltopdf` based on different operating systems.
- **Customization Section:** Expanded details on how to customize the invoice template and adjust data formatting functions.
- **Contributing Section:** Encouraged contributions with a brief guide on how to contribute via Pull Requests.
- **License Section:** Clarified licensing information with a direct reference to the LICENSE file.

These refinements should help users understand and utilize your invoice generator project more effectively. Adjust any paths or instructions as necessary based on your specific project structure and requirements.