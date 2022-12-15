import os


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_ACCESS_SECRET = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = "https://testing2-for-demo.fra1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
# AWS_LOCATION = f"https://{AWS_STORAGE_BUCKET_NAME}.nyc3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "foodiez.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "foodiez.cdn.backends.StaticRootS3Boto3Storage"
