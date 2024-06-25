import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

def format_currency(value):
    return f"₹{value:,.2f}"

def amount_in_words(amount):
    # Dummy implementation for the sake of example
    return f"{amount} Rupees only"

def generate_invoice(seller_details, billing_details, shipping_details, order_details, invoice_details, items, logo, signature):
    # Calculate derived parameters
    for item in items:
        item['net_amount'] = item['unit_price'] * item['quantity'] - item['discount']
        if invoice_details['place_of_supply'] == invoice_details['place_of_delivery']:
            item['tax_type'] = 'CGST/SGST'
            item['tax_rate'] = 9
            item['tax_amount_cgst'] = item['net_amount'] * 0.09
            item['tax_amount_sgst'] = item['net_amount'] * 0.09
            item['total_amount'] = item['net_amount'] + item['tax_amount_cgst'] + item['tax_amount_sgst']
        else:
            item['tax_type'] = 'IGST'
            item['tax_rate'] = 18
            item['tax_amount_igst'] = item['net_amount'] * 0.18
            item['total_amount'] = item['net_amount'] + item['tax_amount_igst']
    
    total_amount = sum(item['total_amount'] for item in items)

    # Load the HTML template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('invoice_template.html')

    # Render the template with data
    html_out = template.render(
        seller_details=seller_details,
        billing_details=billing_details,
        shipping_details=shipping_details,
        order_details=order_details,
        invoice_details=invoice_details,
        items=items,
        total_amount=format_currency(total_amount),
        logo=os.path.abspath(logo),
        signature=os.path.abspath(signature),
        amount_in_words=amount_in_words(total_amount)
    )

    # Generate PDF
    pdfkit.from_string(html_out, 'invoice.pdf', options={
        'enable-local-file-access': None
    })

# Sample data
seller_details = {
    "name": "Seller Name",
    "address": "123 Seller St",
    "city": "Seller City",
    "state": "Seller State",
    "pincode": "123456",
    "pan_no": "ABCDE1234F",
    "gst_no": "12ABCDE3456F1Z7"
}

billing_details = {
    "name": "Buyer Name",
    "address": "123 Buyer St",
    "city": "Buyer City",
    "state": "Buyer State",
    "pincode": "654321",
    "state_code": "12"
}

shipping_details = {
    "name": "Buyer Name",
    "address": "123 Buyer St",
    "city": "Buyer City",
    "state": "Buyer State",
    "pincode": "654321",
    "state_code": "12"
}

order_details = {
    "order_no": "12345",
    "order_date": "2024-06-25"
}

invoice_details = {
    "invoice_no": "INV12345",
    "invoice_date": "2024-06-25",
    "place_of_supply": "Seller State",
    "place_of_delivery": "Buyer State"
}

items = [
    {"description": "Item 1", "unit_price": 100, "quantity": 2, "discount": 10, "tax_rate": 18},
    {"description": "Item 2", "unit_price": 200, "quantity": 1, "discount": 20, "tax_rate": 18}
]

logo = 'path/to/logo.png'
signature = 'path/to/signature.png'

generate_invoice(seller_details, billing_details, shipping_details, order_details, invoice_details, items, logo, signature)
