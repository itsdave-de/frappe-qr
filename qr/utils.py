from base64 import b64encode
import segno
import io

def get_qr_code(data: str, dark: str = 'black', light: str = 'white', return_html: bool = True, width: int = 200, height: int = 200, format: str = 'svg', scale: int = 10) -> str:
    """
    Generates a QR code for a given string, with customizable colors, formats, and sizes.

    This versatile function supports both SVG and PNG formats, ensuring high-quality and scalable output. 
    The generated QR code can be returned either as a base64-encoded string or directly embedded as an HTML 
    <img> tag for seamless integration into web pages.

    Parameters:
    - data (str): The data to encode in the QR code.
    - dark (str, optional): Color of the QR code's dark modules (default is 'black').
    - light (str, optional): Color of the QR code's light modules (default is 'white').
    - return_html (bool, optional): If True, returns an HTML <img> tag; if False, returns a base64-encoded string (default is True).
    - width (int, optional): The width of the QR code image in pixels (default is 200).
    - height (int, optional): The height of the QR code image in pixels (default is 200).
    - format (str, optional): The format of the QR code ('svg' or 'png', default is 'svg').
    - scale (int, optional): The scaling factor for PNG output (default is 10).

    Returns:
    - str: An HTML <img> tag with the embedded QR code, or a base64-encoded string, depending on the return_html parameter.

    Example Usage:
    ```python
    # Generate an HTML <img> tag with a blue QR code on a yellow background
    qr_code_html = get_qr_code("Sample Data", dark='blue', light='yellow', width=200, height=200, format='png', scale=10)

    # Generate a base64-encoded string of the QR code
    qr_code_base64 = get_qr_code("Sample Data", dark='blue', light='yellow', return_html=False, format='png', scale=10)
    ```
    
    This function is ideal for generating QR codes on the fly, with options to customize colors and formats to fit any design or application requirement.
    """
    qr = segno.make(data)  # Generate QR code
    buffer = io.BytesIO()  # Create an in-memory bytes buffer
    
    if format == 'svg':
        qr.save(buffer, kind='svg', dark=dark, light=light)  # Save QR code as SVG to the buffer with specified colors
        mime_type = 'image/svg+xml'
    elif format == 'png':
        qr.save(buffer, kind='png', dark=dark, light=light, scale=scale)  # Save QR code as PNG to the buffer with specified colors and scale
        mime_type = 'image/png'
    else:
        raise ValueError("Unsupported format. Use 'svg' or 'png'.")
    
    buffer.seek(0)  # Rewind the buffer to the beginning
    base_64_string = bytes_to_base64_string(buffer.getvalue())  # Encode the image bytes to base64 string
    base64_data = add_file_info(base_64_string, mime_type)
    
    if return_html:
        html_tag = f'<img src="{base64_data}" alt="QR Code for {data}" width="{width}" height="{height}">'
        return html_tag
    
    return base64_data

def add_file_info(data: str, mime_type: str) -> str:
    """Add info about the file type and encoding.
    This is required so the browser can make sense of the data."""
    return f"data:{mime_type};base64,{data}"

def bytes_to_base64_string(data: bytes) -> str:
    """Convert bytes to a base64 encoded string."""
    return b64encode(data).decode("utf-8")
