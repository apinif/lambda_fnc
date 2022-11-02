import json
from aws_lambda_powertools.event_handler import APIGatewayRestResolver

app = APIGatewayRestResolver()

# import requests


@app.get("/file/<event_id>")
def get_file(event_id):
    return 