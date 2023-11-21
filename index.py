import jinja2
import pdfkit
from datetime import datetime

my_name = "Frank Andrade"
item1 = "Black Strap A012"
item1_sub ="Watch, Black"
item2 = "Stainless Steel S010"
item2_sub="Watch, Gold"

today_date = datetime.today().strftime("%d %b, %Y")

context = {'my_name': my_name, 'item1': item1,'item1_sub': item1_sub, 'item2': item2,'item2_sub': item2_sub,'today_date': today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'invoice_card.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='./')
output_pdf = 'pdf_generated.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css')