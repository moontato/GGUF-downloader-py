import os

# CONSTANTS
DOT_GGUF_LENGTH = 5

print("== GGUF Model Downloader ==")

url = input("Huggingface URL: ")
local_destination = input("Destination (default = './'): ")

# Process destination path
if(len(local_destination) > 0):
    if(local_destination[0] == "/"):
        local_destination = local_destination[1:]
    if(local_destination[len(local_destination)-1] != "/"):
        local_destination = f"{local_destination}/"

destination = f"{os.path.dirname(os.path.realpath(__file__))}/{local_destination}"
print(f"Saving to: {destination}")


# Extract model name
gguf_index = url.find(".gguf")
slash_offset = 0        # "/ <--offset--> .gguf"

while(url[gguf_index - slash_offset] != "/"):
    slash_offset += 1

model_filename = url[(gguf_index - slash_offset + 1):(gguf_index + DOT_GGUF_LENGTH)]


# Download the model
os.system(f"wget -O {destination}{model_filename} {url}")

print("Model downloaded.")