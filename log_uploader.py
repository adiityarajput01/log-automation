import boto3
import os
from datetime import datetime

#bucket_name = "log-uploaded-bucket" (older version)
bucket_name = os.environ.get("S3_BUCKET_NAME", "log-uploaded-bucket")
print(f"--- Starting v2 Logger ---")
print(f"Target Bucket: {bucket_name}")
folder_path = "./host-logs" 
today = datetime.now().strftime("%Y-%m-%d")



s3 = boto3.client('s3')

def start_upload():
	print("Starting the upload process...")
	try:
		with open("./host-logs/outputs.log","a") as f:
			f.write(f"\n--- Run started at {today} ---\n")
		
			for filename in os.listdir(folder_path):
				
				if filename.endswith(".log"):

					new_name = filename.replace(".log", f"_{today}.log")
					full_local_path = os.path.join(folder_path, filename)

					try:
						
						print(f"Uploading {filename} as {new_name}...")
						s3.upload_file(full_local_path, bucket_name, new_name)
						print("Done!")
						f.write(f"Successfully uploaded: {filename} as {new_name}\n")
					except Exception as e:
						print(f"Error uploading {filename}: {e}")
						f.write(f"Failed upload: {filename}. Error: {e}\n")
			f.flush()
			os.fsync(f.fileno())
	except Exception as e:
		print(f"Logging error: {e}")
						

if __name__ == "__main__":
	start_upload()


#END


