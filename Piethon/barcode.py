import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    # Create a Code128 barcode object
    code = barcode.get('code128', data, writer=ImageWriter())

    # Set barcode options
    code.set_options(height=50, quiet_zone=10)

    # Save the barcode image to a file
    code.save(filename)

    print(f"Barcode generated and saved as {filename}")

data = "1234-5678-9012"
filename = "barcode.png"

generate_barcode(data, filename)
