import asyncio
import websockets
import json
from datetime import datetime, timezone
import pandas as pd
from boat import boat

boat_dictionary = {}  # Dictionary to hold boat objects with UserID as key. 

async def connect_ais_stream():

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        subscribe_message = {"APIKey": "864002057a10f30379dae6cab23925bbe0eff74e",  # Required !
                            "BoundingBoxes": [[[-90, -180], [90, 180]]], # Required!
                            #"FiltersShipMMSI": ["368207620", "367719770", "211476060"], # Optional!
                            #"FilterMessageTypes": ["PositionReport"] # Optional!
                            }

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)

        async for message_json in websocket:
            message = json.loads(message_json)
            message_type = message["MessageType"]

            if message_type == "PositionReport":
                # the message parameter contains a key of the message type which contains the message itself
                ais_message = message['Message']['PositionReport']
                currBoat = boat(ais_message['UserID'], ais_message['Latitude'], ais_message['Longitude'])
                if currBoat.get_id() not in boat_dictionary:
                    boat_dictionary[currBoat.get_id()] = currBoat
                    boat_dictionary[currBoat.get_id()].set_latitude(ais_message['Latitude'])
                    boat_dictionary[currBoat.get_id()].set_longitude(ais_message['Longitude'])
                print(f"[{datetime.now(timezone.utc)}] ShipId: {ais_message['UserID']} Latitude: {ais_message['Latitude']} Longitude: {ais_message['Longitude']}")

def getDataFrame():
    data = {
        "ShipId": [],
        "Latitude": [],
        "Longitude": []
    }
    for boat_id, boat_obj in boat_dictionary.items():
        data["ShipId"].append(boat_id)
        data["Latitude"].append(boat_obj.get_latitude())
        data["Longitude"].append(boat_obj.get_longitude())
    
    df = pd.DataFrame(data)
    return df

def main():
    asyncio.run(connect_ais_stream())

if __name__ == "__main__":
    main()