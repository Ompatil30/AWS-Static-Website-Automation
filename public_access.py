import boto3
import json

# ===========================
# CONFIGURATION
# ===========================

BUCKET_NAME = "ompatil-static-site-2026"   # Replace with your bucket name

# ===========================
# CREATE S3 CLIENT
# ===========================

s3 = boto3.client("s3")

# ===========================
# DISABLE BLOCK PUBLIC ACCESS
# ===========================

try:
    s3.put_public_access_block(
        Bucket=BUCKET_NAME,
        PublicAccessBlockConfiguration={
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False
        }
    )

    print("✅ Block Public Access Disabled")

except Exception as e:
    print("❌ Error disabling Block Public Access:", e)

# ===========================
# APPLY PUBLIC BUCKET POLICY
# ===========================

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
        }
    ]
}

try:
    s3.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=json.dumps(policy)
    )

    print("✅ Public Bucket Policy Applied")

except Exception as e:
    print("❌ Error applying Bucket Policy:", e)

print("\n🎉 Bucket is now public!")