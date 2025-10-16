# SKYQR
# SkyQr.py - QR Code Generator
# Generates QR codes from links and saves them as PNG files in QR-png folder

import qrcode
import os
from datetime import datetime

# Check for required dependencies
try:
    import qrcode
    from PIL import Image  # This confirms Pillow is available
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Please install required packages by running: pip install qrcode pillow")
    exit(1)

def create_qr_folder():
    """Create QR-png folder if it doesn't exist"""
    folder = "QR-png"
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def generate_qr_code(link, filename):
    """Generate QR code from link and save to QR-png folder"""
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        # Add data to QR code
        qr.add_data(link)
        qr.make(fit=True)
        
        # Create image from QR code
        qr_image = qr.make_image(fill_color="black", back_color="white")
        
        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join("QR-png", f"{filename}_{timestamp}.png")
        
        # Save QR code image
        qr_image.save(output_path)
        print(f"QR code saved successfully as {output_path}")
        
     # Ask for permission to view the QR code automatically
        view_permission = input("Do you want to view the QR code now? (y/n): ").strip().lower()
        if view_permission == 'y':
            try:
                system = platform.system()
                if system == 'Darwin':  # macOS
                    subprocess.call(['open', output_path])
                elif system == 'Windows':
                    os.startfile(output_path)
                else:  # Linux and others
                    subprocess.call(['xdg-open', output_path])
                print("Opening QR code in default viewer...")
            except Exception as e:
                print(f"Error opening image: {str(e)}. You can manually open {output_path}")
        
        return True
        
    except Exception as e:
        print(f"Error generating QR code: {str(e)}")
        if "PIL" in str(e):
            print("Hint: This might be due to missing Pillow. Run: pip install pillow")
        return False

def main():
    """Main function to handle QR code generation"""
    print("\n=== SKYQR - QR Code Generator ===")
    
    # Create QR-png folder
    create_qr_folder()
    
    while True:
        # Get user input
        link = input("\nEnter the link to convert to QR code (or 'quit' to exit): ")
        
        if link.lower() == 'quit':
            print("Thank you for using SKYQR!")
            break
            
        if not link:
            print("Error: Please enter a valid link")
            continue
            
        # Generate filename from link or user input
        filename = input("Enter filename for QR code (without extension): ").strip()
        if not filename:
            filename = "qr_code"
            
        # Generate and save QR code
        generate_qr_code(link, filename)

if __name__ == "__main__":
    main()
