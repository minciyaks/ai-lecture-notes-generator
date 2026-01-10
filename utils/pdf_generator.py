from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(file_path, transcript, summary, key_points, keywords, important_sentences):
    styles = getSampleStyleSheet()
    story = []

    def add_section(title, content):
        story.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
        story.append(Spacer(1, 6))
        if isinstance(content, list):
            for item in content:
                story.append(Paragraph(f"- {item}", styles["Normal"]))
        else:
            story.append(Paragraph(content, styles["Normal"]))
        story.append(Spacer(1, 12))

    add_section("Transcript", transcript)
    add_section("Summary", summary)
    add_section("Key Points", key_points)
    add_section("Keywords", [", ".join(keywords)])
    add_section("Important Sentences", important_sentences)

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    doc.build(story)
