#!/usr/bin/env python3
"""
Birthday Flyer Generator
Creates a poster-style PDF birthday flyer with custom colors and details.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os


def create_birthday_flyer(output_path="birthday_flyer.pdf"):
    """
    Generate a poster-style birthday flyer PDF.
    
    Details:
    - Theme colors: Red, Black, and White
    - Birthday: October 8, 1968
    - Location: Greenville, NC
    - Contact: bee@ok.com | 555-555-5555
    - Message: "A Cool Giggling Celebration!"
    """
    # Create canvas with letter size (8.5 x 11 inches)
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Define colors
    red = colors.HexColor('#DC143C')  # Crimson red
    black = colors.black
    white = colors.white
    
    # Background - white with red border
    c.setFillColor(white)
    c.rect(0, 0, width, height, fill=True, stroke=False)
    
    # Red border frame
    c.setStrokeColor(red)
    c.setLineWidth(8)
    c.rect(0.25*inch, 0.25*inch, width - 0.5*inch, height - 0.5*inch, fill=False, stroke=True)
    
    # Inner black border
    c.setStrokeColor(black)
    c.setLineWidth(2)
    c.rect(0.5*inch, 0.5*inch, width - 1*inch, height - 1*inch, fill=False, stroke=True)
    
    # Title banner - red background
    c.setFillColor(red)
    c.rect(0.75*inch, height - 2.5*inch, width - 1.5*inch, 1.5*inch, fill=True, stroke=False)
    
    # Main title text
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(width / 2, height - 1.5*inch, "BEE'S")
    c.drawCentredString(width / 2, height - 2.1*inch, "BIRTHDAY BASH!")
    
    # Date section
    y_position = height - 3.2*inch
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 32)
    c.drawCentredString(width / 2, y_position, "DATE: October 8")
    
    # Birth year
    y_position -= 0.6*inch
    c.setFont("Helvetica", 20)
    c.drawCentredString(width / 2, y_position, "Born October 8, 1968")
    
    # Location
    y_position -= 0.8*inch
    c.setFont("Helvetica-Bold", 28)
    c.setFillColor(red)
    c.drawCentredString(width / 2, y_position, "LOCATION:")
    
    y_position -= 0.5*inch
    c.setFillColor(black)
    c.setFont("Helvetica", 24)
    c.drawCentredString(width / 2, y_position, "Greenville, NC")
    
    # Special message - decorative box
    y_position -= 1*inch
    c.setFillColor(black)
    c.rect(1*inch, y_position - 0.4*inch, width - 2*inch, 0.7*inch, fill=True, stroke=False)
    
    c.setFillColor(white)
    c.setFont("Helvetica-BoldOblique", 22)
    c.drawCentredString(width / 2, y_position, "A COOL GIGGLING CELEBRATION!")
    
    # Dress code
    y_position -= 1*inch
    c.setFillColor(red)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, y_position, "COLORS: Wear Red, Black, or White!")
    
    # Contact information section
    y_position -= 1.2*inch
    c.setFillColor(black)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y_position, "Contact for details or RSVP:")
    
    y_position -= 0.4*inch
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, y_position, "bee@ok.com | 555-555-5555")
    
    # Bottom tagline
    y_position -= 0.8*inch
    c.setFillColor(red)
    c.setFont("Helvetica-BoldOblique", 14)
    c.drawCentredString(width / 2, y_position, "Let's party, laugh, and celebrate another trip around the sun!")
    
    # Decorative elements - corner stars
    star_size = 20
    c.setFillColor(red)
    c.setFont("Helvetica", star_size)
    # Top corners
    c.drawString(0.6*inch, height - 0.7*inch, "★")
    c.drawString(width - 0.9*inch, height - 0.7*inch, "★")
    # Bottom corners
    c.drawString(0.6*inch, 0.6*inch, "★")
    c.drawString(width - 0.9*inch, 0.6*inch, "★")
    
    # Save the PDF
    c.save()
    print(f"Birthday flyer successfully created: {output_path}")
    return output_path


if __name__ == "__main__":
    # Generate the flyer
    output_file = os.path.join(os.path.dirname(__file__), "..", "birthday_flyer.pdf")
    create_birthday_flyer(output_file)
