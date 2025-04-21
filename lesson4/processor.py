import json, datetime

def validate_record(record):
    try:
        timestamp = record.get("timestamp")


        truck_id = record.get("truck_id")
        if not truck_id or not isinstance(truck_id,str):
            return False, "Invalid or missing truck_id",timestamp

        latitude = record.get("latitude")
        if not isinstance(latitude,float):
            return False, "Invalid latitude",timestamp


        longitude = record.get("longitude")
        if not isinstance(longitude,float):
            return False, "Invalid longitude"

        return True, "Valid",timestamp



    except Exception as e:
        return False, f"Exception: {str(e)}", timestamp


def procces_log_file(filepath):
    records = []
    with open(filepath,"r") as file:
        records  = json.load(file)
        print(records)
    
    with open("success.log", "w") as success_log, open("error.log", "w") as error_log:
        for record in records:
            valid, message, timestamp = validate_record(record)
            print(valid, message,timestamp)
            
            truck_id = record.get("truck_id","UNKNOWN")
            timestamp = record.get("timestamp","NO_TIME")
            line = f"{truck_id}| {timestamp}"

            if valid:
                success_log.write(line + "|" + "SUCCESS \n" )
            else:
                error_log.write(line + f"ERROR:{message} \n")

procces_log_file("log_input.json")