events = ["Extraction Started", "Transformation Complete", "Loading to Snowflake", "Success"]

# Use 'w' mode to create or overwrite the file
with open("pipeline.log", "w") as log_file:
    for event in events:
        # We add \n (newline) to ensure each event is on its own row
        log_file.write(event + "\n")

print("Logs successfully written to pipeline.log")