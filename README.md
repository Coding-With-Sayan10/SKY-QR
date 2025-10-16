# SKY-QR
User Friendly Interface Link To QR Generator . 
# Sky-Qr: Link to QR Code Generator

A lightweight Python script to convert URLs into QR codes. Saves output as `Qr-Png`

## Features
- Interactive URL input
- URL validation
- Customizable QR size/error correction
- Termux-friendly , Linux , Windows, MacOs (with preview option)

## Installation
1. Clone : `https://github.com/Coding-With-Sayan10/SKY-QR.git`
2. Install deps: `pip install -r requirements.txt`
3. Run: `cd SKY-QR` : `python SkyQr.py`

## Usage
- Enter a valid URL when prompted.
- QR code saves as `Qr-Png`.
- Optional: Preview with Termux API.

## Dependencies
- qrcode[pil]
- pillow
- validators

## Customization
Edit `SkyQr.py`:
- Change `box_size` for larger QR.
- Modify `filename` for different output names.

Build By Sayan Das .
