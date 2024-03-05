from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg

def draw_staves(c, num_staves, start_y, stave_height, stave_spacing, treble_clef_svg, line_width=1):
    """Draws a series of music staves on a PDF canvas and adds a treble clef to each stave."""
    treble_clef_drawing = svg2rlg(treble_clef_svg)
    treble_clef_scale = 0.05  # Adjusted scale for the treble clef
    for i in range(num_staves):
        y = start_y - i * (stave_height + stave_spacing)
        for j in range(5):  # Each stave has 5 lines
            c.line(50, y - j * line_width * 4, 550, y - j * line_width * 4)
        # Draw the treble clef at the beginning of each stave
        c.saveState()
        c.translate(40, y - stave_height * 2)  # Adjusted translation for the treble clef
        c.scale(treble_clef_scale, treble_clef_scale)
        treble_clef_drawing.drawOn(c, 0, 0)
        c.restoreState()

def generate_pdf(pdf_filename, treble_clef_svg):
    """Generates a PDF with music staves and treble clefs."""
    c = canvas.Canvas(pdf_filename, pagesize=LETTER)
    title = "Music Sheet Title"
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 780, title)  # Draw the title
    draw_staves(c, num_staves=12, start_y=730, stave_height=40, stave_spacing=12, treble_clef_svg=treble_clef_svg)
    c.save()

def main():
    pdf_filename = "staves_with_treble_clef.pdf"
    treble_clef_svg = "treble_clef.svg"
    generate_pdf(pdf_filename, treble_clef_svg)

if __name__ == "__main__":
    main()
