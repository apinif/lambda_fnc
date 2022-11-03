from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import requests
import boto3

s3 = boto3.client('s3')

app = APIGatewayRestResolver()

w, h = letter
@app.get("/file/<event_id>")
def generate_file(event_id):
    response = requests.get(f"https://xbx4z0fx58.execute-api.us-east-1.amazonaws.com/prod/broker/{event_id}")
    event = response.json()
    my_canvas = canvas.Canvas(f"evento_{event_id}.pdf", pagesize=letter)
    text = my_canvas.beginText(50, h - 50)
    text.setFont("Times-Roman", 14)
    text.textLine(f"Evento {event_id}")
    text.textLine(f"Tipo de evento: {event["type"]}")
    text.textLine(f"Latitud: {event["geolocation"]["coordinates"][0]}")
    text.textLine(f"Longitud: {event["geolocation"]["coordinates"][1]}")
    text.textLine(f"Ubicación: {event["location"]}")
    text.textLine(f"Mensaje: {event["message"]}")
    text.textLine(f"Nivel: {event["level"]}")
    text.textLine(f"Fecha: {event["created_at"]}")
    my_canvas.drawText(text)
    my_canvas.showPage()
    my_canvas.save()
    s3.upload_file(
        Filename=f"evento_{event_id}.pdf",
        Bucket="e2-g21-pdfs-iic2173",
        Key="new_user_credentials.csv",
    )
    

def lambda_handler(event, context):
    return app.resolve(event, context)