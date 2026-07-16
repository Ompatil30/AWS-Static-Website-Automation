import boto3
from botocore.exceptions import ClientError

# ===========================
# CONFIGURATION
# ===========================

BUCKET_NAME = "ompatil-static-site-2026"   # Change this to something unique
REGION = "ap-south-1"

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
    print("❌ Error:", e)