import json
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from reportlab.pdfgen import canvas
import requests

app = APIGatewayRestResolver()


@app.get("/file/<event_id>")
def generate_file(event_id):
    my_canvas = canvas.Canvas(f"evento_{event_id}.pdf")
    my_canvas.drawString(100, 750, f"{}")
    return 