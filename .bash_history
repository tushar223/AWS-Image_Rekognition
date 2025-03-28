clear
sudo apt update -y
sudo apt install python3-pip -y
python3 -m myenv venv
python3 -m venv myenv
sudo apt install python3.12-venv
python3 -m venv myenv
source myenv/bin/activate
pip3 install boto3 matplotlib pillow
nano image_upload.py
scp -i aws-key.pem cat.jpg ec2-user@your-ec2-ip:~
scp -i aws-key.pem cat.jpg ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com
scp -i aws-key.pem "C:\Users\Tushar Sinha\.ssh\cat.jpg" ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com
scp -i ~/aws-key.pem "/mnt/c/Users/Tushar Sinha/.ssh/cat.jpg" ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com:~
scp -i ~/.ssh/aws-key.pem "/c/Users/Tushar Sinha/.ssh/cat.jpg" ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com:~
ls -l ~/.ssh/aws-key.pem
scp -i "/c/Users/Tushar Sinha/.ssh/aws-key.pem" "/c/Users/Tushar Sinha/.ssh/cat.jpg" ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com:~
chmod 400 ~/.ssh/aws-key.pem
ssh -i ~/.ssh/aws-key.pem ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com
clear
ls -l /c/Users/Tushar\ Sinha/.ssh/aws-key.pem
scp -i "/c/Users/Tushar Sinha/.ssh/aws-rekognition.pem" "/c/Users/Tushar Sinha/.ssh/cat.jpg" ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com:~
ls
scp -v -i "/c/Users/Tushar Sinha/.ssh/aws-key.pem" "/c/Users/Tushar Sinha/.ssh/cat.jpg" ubuntu@ec2-13-232-228-5.ap-south-1.compute.amazonaws.com:~
ls -l "/c/Users/Tushar Sinha/.ssh/cat.jpg"
ls -l "/c/Users/Tushar Sinha/.ssh/"
exit
ls -l ~
ls -lh cat.jpg
source myenv/bin/activate
python3 image_upload.py
aws s3 ls s3://my-image-rekognition-bucket/uploads/
sudo apt install awscli
aws s3 ls s3://my-image-rekognition-bucket/uploads/
sudo apt install awscli
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
aws configure
source myenv/bin/activate
python3 image_upload.py
nano detect_labels.py
python3 detect_labels.py
nano detect_labels.py
python3 detect_labels.py
nano detect_labels.py
clear
nano detect_labels.py
python3 detect_labels.py
nano detect_labels.py
nano download_image.py
ls
python3 detect_labels.py
vi download_image.py
ls
nano download_image.py 
clear
source myenv/nin/activate
source myenv/bin/activate
ls
python3 detect_labels.py 
nano download_image.py
python3 download_image.py 
exit
ls
aws s3 cp road.jpg s3://first-image-rekognition-bucket/uploads/
source myenv/bin/activate
nanao image_upload.py 
nano image_upload.py 
python3 image_upload.py 
nano download_image.py
nano detect_objects.py
python3 detect_objects.py 
exit
clear
ls
pwd
git init
git remote add origin https://github.com/tushar223/AWS-Image_Rekognition.git
git add .
git commit -m "Initial commit - AWS Rekognition Project"
git branch -M main
git push -u origin main
git init
git remote add origin https://github.com/tushar223/AWS-Image_Rekognition.git
git branch -M main
git push -u origin main
