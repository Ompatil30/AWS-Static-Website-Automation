import boto3

# ===========================
# CONFIGURATION
# ===========================

BUCKET_NAME = "ompatil-static-site-2026"   # Replace with your bucket name

# ===========================
# CREATE S3 CLIENT
# ===========================

s3 = boto3.client("s3")

# ===========================
# ENABLE STATIC WEBSITE HOSTING
# ===========================

try:
    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            "IndexDocument": {
                "Suffix": "index.html"
            },
            "ErrorDocument": {
                "Key": "index.html"
            }
        }
    )

    print("✅ Static Website Hosting Enabled Successfully!")

except Exception as e:
    print("❌ Error:", e)