import boto3

# AWS Configuration
BUCKET_NAME = "first-image-rekognition-bucket"
S3_IMAGE_KEY = "uploads/cat.jpg"
AWS_REGION = "ap-south-1"
# Initialize Rekognition Client
rekognition_client = boto3.client("rekognition", region_name=AWS_REGION)

# Call Rekognition API
response = rekognition_client.detect_labels(
    Image={"S3Object": {"Bucket": BUCKET_NAME, "Name": S3_IMAGE_KEY}},
    MaxLabels=10
)

# Print detected labels
print("\n🔍 Detected Labels:")
for label in response["Labels"]:
    print(f"{label['Name']} ({label['Confidence']:.2f}%)")
