from barcode import EAN13

from bbarcode.writer import ImageWriter

number ="9265053201"

my_code=EAN13(number,writer=ImageWriter())

my_code.save("barcode1")