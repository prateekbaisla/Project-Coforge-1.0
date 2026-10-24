from azure.eventhub import EventHubProducerClient, EventData
import json
 
# Connection string and Event Hub name
connection_str = "Endpoint=sb://prateek.servicebus.windows.net/;SharedAccessKeyName=prateekstream_prateekevent_policy;SharedAccessKey=ANBwWxwt0eyAv7wcci+g/500bLtHzS6tj+AEhEbGZ/8=;EntityPath=prateekevent"
eventhub_name = "prateekevent "
 
json_file_path = "real_time_transactions.json"
 
def send_json_file_to_eventhub():
    producer = EventHubProducerClient.from_connection_string(
        conn_str=connection_str,
        eventhub_name=eventhub_name
    )
 
    try:
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
 
        event_batch = producer.create_batch()
 
        for record in json_data:
            event_batch.add(EventData(json.dumps(record)))
 
        producer.send_batch(event_batch)
 
        print(f"Successfully sent {len(json_data)} records to Event Hub")
 
    except Exception as e:
        print(f"Error: {e}")
 
    finally:
        producer.close()
 
send_json_file_to_eventhub()
