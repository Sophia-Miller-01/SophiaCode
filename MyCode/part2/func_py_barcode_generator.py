# func_py_barcode_generator.py
import barcode
from barcode.writer import ImageWriter

def func_py_barcode_generator(data, filename="barcode.png"):
    code128 = barcode.get("code128", data, writer=ImageWriter())
    code128.save(filename)

func_py_barcode_generator("123456789")
