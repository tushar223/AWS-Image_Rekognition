import boto3
import json
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# AWS S3 and Rekognition Configuration
BUCKET_NAME = "first-image-rekognition-bucket"
S3_IMAGE_KEY = "uploads/road.jpg"  # Change to your image file

# Initialize Rekognition Client
rekognition_client = boto3.client("rekognition", region_name="ap-south-1")
# Call Rekognition API
response = rekognition_client.detect_labels(
    Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": S3_IMAGE_KEY}},
    MaxLabels=15,
    Features=["GENERAL_LABELS"]
)

# Load Image
s3_client = boto3.client("s3")
s3_client.download_file(BUCKET_NAME, S3_IMAGE_KEY, "local_image.jpg")
image = Image.open("local_image.jpg")
# Draw Bounding Boxes
draw = ImageDraw.Draw(image)

for label in response["Labels"]:
    for instance in label.get("Instances", []):
        box = instance["BoundingBox"]
        width, height = image.size

        # Convert bounding box to pixel values
        left = int(box["Left"] * width)
        top = int(box["Top"] * height)
        right = int((box["Left"] + box["Width"]) * width)
        bottom = int((box["Top"] + box["Height"]) * height)

        # Draw rectangle
        draw.rectangle([left, top, right, bottom], outline="red", width=3)

        # Draw label text
        draw.text((left, top), f"{label['Name']} ({label['Confidence']:.2f}%)", fill="red")

# Save and Display Image
image.save("output.jpg")
plt.imshow(image)
plt.axis("off")
plt.show()
