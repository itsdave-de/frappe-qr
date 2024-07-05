from base64 import b64encode
import segno
import io

def get_qr_code(data: str, dark: str = 'black', light: str = 'white', return_html: bool = True, size: int = 200, format: str = 'svg', scale: int = 10) -> str:
    """
    Generates a square QR code for a given string, with customizable colors, formats, and sizes.
    This function ensures the QR code is always square to preserve its aspect ratio.

    Parameters:
    - data (str): The data to encode in the QR code.
    - dark (str, optional): Color of the QR code's dark modules (default is 'black').
    - light (str, optional): Color of the QR code's light modules (default is 'white').
    - return_html (bool, optional): If True, returns an HTML <div> tag with an embedded <img>; if False, returns a base64-encoded string (default is True).
    - size (int, optional): The size (width and height) of the QR code image in pixels (default is 200).
    - format (str, optional): The format of the QR code ('svg' or 'png', default is 'svg').
    - scale (int, optional): The scaling factor for PNG output (default is 10).

    Returns:
    - str: An HTML <div> tag with an embedded <img> and CSS to maintain aspect ratio, or a base64-encoded string, depending on the return_html parameter.
    """
    qr = segno.make(data, micro=False)  # Generate QR code, ensuring it is not a micro QR code
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
        html_tag = (
            f'<div style="width:{size}px;height:{size}px;display:inline-block;">'
            f'<img src="{base64_data}" alt="QR Code for {data}" style="width:100%;height:100%;object-fit:contain;">'
            f'</div>'
        )
        return html_tag
    
    return base64_data

def add_file_info(data: str, mime_type: str) -> str:
    """Add info about the file type and encoding.
    This is required so the browser can make sense of the data."""
    return f"data:{mime_type};base64,{data}"

def bytes_to_base64_string(data: bytes) -> str:
    """Convert bytes to a base64 encoded string."""
    return b64encode(data).decode("utf-8")
