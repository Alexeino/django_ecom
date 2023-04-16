# django_ecom

- Clone the repository to your computer
- Launch VS Code and Choose > **Select workspace from file**
- When prompted choose **_code.code-workspace** file
- Create your own ENV File at same level as **manage.py**

## Caveats 
### Product Views
-   While uploading product with image, if that image is already in s3 for other model object, It would use the same image reference for new product object. But when deleting one of the objects the image is removed from s3 bucket completely due to **django-cleanup** library and other objects that are using same image reference, lose their image file.
-   
  