import json
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import requests

app = APIGatewayRestResolver()


@app.get("/file/<event_id>")
def generate_file(event_id):
    response = requests.get(f"https://xbx4z0fx58.execute-api.us-east-1.amazonaws.com/prod/broker/{event_id}")
    event = response.json()
    my_canvas = canvas.Canvas(f"evento_{event_id}.pdf", pagesize=letter)
    my_canvas.drawString(100, 740, f"Evento {event_id}")
    my_canvas.drawString(100, 720, f"Tipo de evento: {event["type"]}")
    my_canvas.drawString(100, 700, f"Latitud: {event["geolocation"]["coordinates"][0]}")
    my_canvas.drawString(100, 680, f"Longitud: {event["geolocation"]["coordinates"][1]}")
    my_canvas.drawString(100, 660, f"Ubicación: {event["location"]}")
    my_canvas.drawString(100, 640, f"Mensaje: {event["message"]}")
    my_canvas.drawString(100, 620, f"Nivel: {event["level"]}")
    my_canvas.drawString(100, 600, f"Fecha: {event["created_at"]}")
    

def lambda_handler(event, context):
    return app.resolve(event, context)