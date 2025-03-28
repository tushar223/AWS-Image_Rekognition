import boto3
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# AWS Configuration
BUCKET_NAME = "first-image-rekognition-bucket"
S3_IMAGE_KEY = "uploads/cat.jpg"
LOCAL_IMAGE = "cat.jpg"
OUTPUT_IMAGE = "output.jpg"
AWS_REGION = "ap-south-1"

s3_client = boto3.client("s3")
s3_client.download_file(BUCKET_NAME, S3_IMAGE_KEY, LOCAL_IMAGE)

# Initialize Rekognition Client
rekognition_client = boto3.client("rekognition", region_name=AWS_REGION)

# Call Rekognition API
response = rekognition_client.detect_labels(
    Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": S3_IMAGE_KEY}},
    MaxLabels=10
)
image = Image.open(LOCAL_IMAGE)
draw = ImageDraw.Draw(image)

# Draw Bounding Boxes (if available)
for label in response["Labels"]:
    if "Instances" in label:
        for instance in label["Instances"]:
            if "BoundingBox" in instance:
                box = instance["BoundingBox"]
                x1 = box["Left"] * image.width
                y1 = box["Top"] * image.height
                x2 = (box["Left"] + box["Width"]) * image.width
                y2 = (box["Top"] + box["Height"]) * image.height
                draw.rectangle([x1, y1, x2, y2], outline="red", width=2)

# Save Processed Image
image.save(OUTPUT_IMAGE)
print(f"✅ Processed image saved as {OUTPUT_IMAGE}")



