from django.shortcuts import render
from django.http import JsonResponse
import boto3, os

def test_r2_upload(request):
    try:
        session = boto3.session.Session()
        s3 = session.client(
            service_name="s3",
            aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
            endpoint_url=os.getenv("R2_ENDPOINT"),
        )

        s3.put_object(
            Bucket=os.getenv("R2_BUCKET_NAME"),
            Key="test_upload/hello_from_django_via_view.txt",
            Body=b"Hello from Django via HTTP view!"
        )
        return JsonResponse({"status": "success", "message": "File uploaded to R2 successfully!"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
