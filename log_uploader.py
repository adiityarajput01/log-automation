import boto3
import os
from datetime import datetime

bucket_name = "log-uploaded-bucket"
folder_path = "./log" 
today = datetime.now().strftime("%Y-%m-%d")


s3 = boto3.client('s3')

def start_upload():
	print("Starting the upload process...")
	
	for filename in os.listdir(folder_path):
		
		if filename.endswith(".log"):

			new_name = filename.replace(".log", f"_{today}.log")
			full_local_path = os.path.join(folder_path, filename)

			try:
				print(f"Uploading {filename} as {new_name}...")
				s3.upload_file(full_local_path, bucket_name, new_name)
				print("Done!")
			except Exception as e:
				print(f"Error uploading {filename}: {e}")

if __name__ == "__main__":
	start_upload()

