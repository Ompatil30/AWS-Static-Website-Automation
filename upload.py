import boto3
import os
import mimetypes
from botocore.exceptions import ClientError

# ===========================
# CONFIGURATION
# ===========================

BUCKET_NAME = "ompatil-static-site-2026"      # Replace with your bucket name
REGION = "ap-south-1"

WEBSITE_FOLDER = "website"

# ===========================
# CREATE S3 CLIENT
# ===========================

s3 = boto3.client("s3", region_name=REGION)

# ===========================
# CREATE BUCKET
# ===========================

try:
    s3.create_bucket(
        Bucket=BUCKET_NAME,
        CreateBucketConfiguration={
            'LocationConstraint': REGION
        }
    )
    print("✅ Bucket Created Successfully!")

except ClientError as e:
    print("ℹ️ Bucket may already exist:", e)

# ===========================
# UPLOAD WEBSITE FILES
# ===========================

print("\nUploading website files...\n")

for file_name in os.listdir(WEBSITE_FOLDER):

    file_path = os.path.join(WEBSITE_FOLDER, file_name)

    content_type = mimetypes.guess_type(file_path)[0]

    if content_type is None:
        content_type = "binary/octet-stream"

    s3.upload_file(
        file_path,
        BUCKET_NAME,
        file_name,
        ExtraArgs={
            "ContentType": content_type
        }
    )

    print(f"✅ Uploaded: {file_name}")

print("\n🎉 All files uploaded successfully!")