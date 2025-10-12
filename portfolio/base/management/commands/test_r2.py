from django.core.management.base import BaseCommand
import boto3, os

class Command(BaseCommand):
    help = "Test Cloudflare R2 connection"

    def handle(self, *args, **kwargs):
        try:
            session = boto3.session.Session()
            s3 = session.client(
                service_name="s3",
                aws_access_key_id=os.getenv("R2_ACCESS_KEY_ID"),
                aws_secret_access_key=os.getenv("R2_SECRET_ACCESS_KEY"),
                endpoint_url=os.getenv("R2_ENDPOINT")
            )

            # Test fayl yuborish
            s3.put_object(
                Bucket=os.getenv("R2_BUCKET_NAME"),
                Key="test_upload/hello_from_django.txt",
                Body=b"Hello from Django on Render!"
            )

            self.stdout.write(self.style.SUCCESS("✅ Test fayl R2 ga yuborildi! Cloudflare’da test_upload/hello_from_django.txt faylini tekshir."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ R2 upload xatosi: {e}"))
