import boto3

# AWS Configuration
BUCKET_NAME = "first-image-rekognition-bucket"  # Change this to your S3 bucket name
IMAGE_FILE = "road.jpg"  # Replace with your image file name
S3_IMAGE_KEY = "uploads/road.jpg"  # Path inside S3

# Initialize S3 Client
s3_client = boto3.client("s3")

# Upload image to S3
s3_client.upload_file(IMAGE_FILE, BUCKET_NAME, S3_IMAGE_KEY)
print(f"✅ Image uploaded successfully to s3://{BUCKET_NAME}/{S3_IMAGE_KEY}")
