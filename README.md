# QR Code Generator for Frappe

![itsdave qr](itsdave-www-qr.png "itsdave qr")

QR Code Generator for Frappe Framework, based on Segno

Its mainly intended to be used inside print formats.

It includes a utility function `get_qr_code` that generates QR codes with customizable colors, formats, and sizes. The generated QR codes can be embedded directly as HTML `<img>` tags or returned as base64-encoded strings.

## Function: `get_qr_code`

The `get_qr_code` function generates a QR code for a given string, with customizable colors, formats, and sizes. This versatile function supports both SVG and PNG formats, ensuring high-quality and scalable output. The generated QR code can be returned either as a base64-encoded string or directly embedded as an HTML `<img>` tag for seamless integration into web pages.

### Parameters:
- **data** (`str`): The data to encode in the QR code.
- **dark** (`str`, optional): Color of the QR code's dark modules (default is 'black').
- **light** (`str`, optional): Color of the QR code's light modules (default is 'white').
- **return_html** (`bool`, optional): If `True`, returns an HTML `<img>` tag; if `False`, returns a base64-encoded string (default is `True`).
- **width** (`int`, optional): The width of the QR code image in pixels (default is 200).
- **height** (`int`, optional): The height of the QR code image in pixels (default is 200).
- **format** (`str`, optional): The format of the QR code ('svg' or 'png', default is 'svg').
- **scale** (`int`, optional): The scaling factor for PNG output (default is 10).

### Returns:
- **str**: An HTML `<img>` tag with the embedded QR code, or a base64-encoded string, depending on the `return_html` parameter.

This function is ideal for generating QR codes on the fly, with options to customize colors and formats to fit any design or application requirement.

### Usage

You can use the get_qr_code function in a custom HTML field inside the print format builder. Some examples:

## Example 1: Static Text

```
<div>
  <p>Static Text - {{ get_qr_code("Static QR Code Data") }}</p>
</div>
```

## Example 2: Using a Variable

```
<div>
  <p>Variable Data - {{ get_qr_code(doc.some_field) }}</p>
</div>
```

## Example 3: Using a Child Table

```
<div>
  {% for row in doc.child_table %}
    <p>{{ row.name }} - {{ row.value }} - {{ get_qr_code(row.qrdata) }}</p>
  {% endfor %}
</div>
```

## Example 4: Custom Colors and Formats

```
<div>
  <p>Custom QR Code - {{ get_qr_code("Custom Data", dark='blue', light='yellow', format='png', scale=5) }}</p>
</div>
```