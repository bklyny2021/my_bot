# Birthday Flyer Generator

This directory contains a Python script to generate a poster-style birthday flyer in PDF format.

## Overview

The flyer celebrates a birthday on **October 8** for someone born in **1968**, with a party theme in **red, black, and white** colors.

## Party Details on the Flyer

- **Date:** October 8
- **Birth Year:** 1968
- **Location:** Greenville, NC
- **Theme:** "A Cool Giggling Celebration!"
- **Dress Code:** Wear Red, Black, or White
- **Contact Info:** bee@ok.com | 555-555-5555

## Requirements

The script requires the `reportlab` Python library:

```bash
pip3 install reportlab
```

## Usage

### Generate the Flyer

Run the script from the repository root:

```bash
python3 scripts/generate_birthday_flyer.py
```

This will create `birthday_flyer.pdf` in the repository root directory.

### Customization

To customize the flyer details (colors, text, layout), edit the `generate_birthday_flyer.py` script. The main function `create_birthday_flyer()` contains all the flyer content and styling.

## Output

The generated PDF is a full-page (8.5" x 11") poster-style flyer with:
- Professional layout with red and black borders
- Large, bold title text
- Clear party information
- Decorative elements (stars in corners)
- Ready to print or share digitally

## Files

- `generate_birthday_flyer.py` - Main script to generate the PDF
- `../birthday_flyer.pdf` - Generated flyer (in repository root)
