This Repository contains mini project LOG UPLODER.
Basiclly , it upload log files to S3.
It have date in the name to specify on which date log get uploaded.
Where is this used in the real world?
Web Servers: Websites generate "Access Logs" (who visited) and "Error Logs" (what broke). Since servers have limited space, scripts move these logs to AWS S3 (which has infinite space) every night.
Compliance: Many industries (like Banking or Healthcare) are legally required to keep logs for 5–7 years. Automated uploaders ensure no data is lost.
Debugging: If an app crashes at 3:00 AM, a developer can go to the S3 bucket and find error_log_2025-12-27.log to see exactly what happened.


The Setup (Libraries)
boto3: This is the official Python library for AWS. It is the "bridge" that lets Python talk to Amazon's servers.
os: This is a built-in Python tool used to talk to your computer's operating system (to find files and folders).
logging: Instead of just print(), we use logging. It’s better because it categorizes messages as INFO (normal) or ERROR (something is wrong).
The Logic (The "How-To")
Scanning the Folder:
os.listdir(LOG_DIRECTORY) looks at every file in your folder. The script then uses an if statement to say: "Only pay attention to files that end in .log."
Creating the New Name:
If you have a file named system.log, the script splits it into system and .log. It then grabs today's date (e.g., 2025-12-27) and stitches them back together: system + _ + 2025-12-27 + .log.
This prevents files from overwriting each other in S3.
The Upload:
The line s3_client.upload_file(...) does the heavy lifting. It sends the bits of data over the internet to your specific Amazon S3 Bucket.
Exception Handling (The Safety Net):
The try...except block is like a safety net.
Without it: If your internet cuts out, the script crashes and stops.
With it: If the internet cuts out, the script "catches" the error, logs a message saying "Hey, I couldn't upload this!", and then moves on to the next file or exits gracefully.


Visualizing the Process
Step	Local Computer	Action	AWS S3 Bucket
1	app.log	Script finds file	(Empty)
2	app.log	Script renames it	(Empty)
3	app.log	UPLOADING...	app_2025-12-27.log
4	app.log	Success!	File is safely stored.
