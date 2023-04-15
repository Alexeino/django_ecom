from django.core.management.base import BaseCommand
import boto3
import dotenv
import os


class Command(BaseCommand):
    help = "Cleanup files from S3..."
    
    def bucket_clean(self,bucket_name):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
        print("Deleted files from bucket ",bucket_name)
        # print("This is the bucket ---------- ",bucket_name)

    def handle(self,*args, **kwargs):
        self.stdout.write("Deleting All files in the bucket !")
        valid_options = ("y","n",)
        while True:
            confirm = input("Are you sure you want to cleanup the S3 bucket.. y/n : ")
            if confirm not in valid_options:
                print("Invalid choice ! Please type y or n")
            elif confirm == "y":
                self.bucket_clean(os.environ.get('AWS_STORAGE_BUCKET_NAME'))
                exit()
            else:
                print("Aborting command s3_cleanup !")
                exit()