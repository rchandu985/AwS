import boto3
from botocore.exceptions import ClientError
from dotenv import dotenv_values



class AwS:



    
    def AuthManagement(resource:str):

        credentials     =   dotenv_values()

        AWS_ACCESS_KEY_ID       =   credentials.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY   =   credentials.get('AWS_SECRET_ACCESS_KEY')

        client                  =   boto3.client(resource,aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        return client
    
class S3:
    class Object:
    
        def Upload(bucket_name:str,file:str,file_name:str):
            s3:boto3.s3  =   AwS.AuthManagement("s3")

            with open(file, "rb") as f:
                s3.upload_fileobj(f, bucket_name, file_name, ExtraArgs={'Metadata': {'mykey': 'myvalue'}})

        
        def Delete(bucket_name:str,file_name:str):
            s3:boto3.s3  =   AwS.AuthManagement("s3")

            s3.delete_object(Bucket=bucket_name, Key=file_name)

    class Bucket:
        pass


bucket_name     =   'saankhyadevelopment'   
#s3_del          =   S3.Object.Delete(bucket_name,"Truth_On_The_Wall_FreeMp4Downloader.mp4")
x=dotenv_values()
print(x.get('AWS_ACCESS_KEY_ID'))