# AWS-Image_Rekognition
A project using AWS Rekognition to detect and label objects in images
✅ Upload images to **Amazon S3**  
✅ Use **AWS Rekognition** for object detection  
✅ Display **bounding boxes & confidence scores**  
✅ Deploy on **AWS EC2**  
✅ Transfer processed images back to local system  
## 🛠️ Tech Stack
- **AWS Services**: S3, Rekognition, IAM, EC2  
- **Programming**: Python, Boto3, OpenCV, Matplotlib  
- **Tools**: Git, SCP, AWS CLI


Install Dependencies
--pip install boto3 matplotlib pillow opencv-python

Run the detection script
--python3 detect_objects.py

Transfer output image from EC2 to local:
-- scp -i "your pem file" "your ec2 ubuntu ip"~:/output.jpg


![image](https://github.com/user-attachments/assets/ba72a6e6-0f51-4e79-9bf8-c1e5b096db37)
