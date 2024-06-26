import boto3
from credentials.keys import ACCESS_KEY, SECRET_KEY

#este metodo permite la conexion con el servicio de s3
def connection_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY) #se agregan dos elementos para rcrear la conexión
        s3_resource = session_aws.resource ('s3') #aca se pone el servicio a usar RDS, s3 ETC
        print("Connecting to s3")
        return s3_resource
    except Exception as err:
        print("Error",err)
        return None
    
    
def save_file(photo):
    try:
        photo_path_local ="/tmp/photo.JPG"
        photo.save(photo_path_local)
        print("Photo saved")
        return photo_path_local
    except Exception as err:
        print("Error", err)
        return None
        
def upload_file(s3_resource, photo, photo_path_local, id):
    try:
        bucket_name = "myaws-cym-ex" #nombre del bucket creado
        photo_name = photo.filename
        photo_extension = photo_name.split(".")[1]
        photo_path_dest = "images/" + id + "." + photo_extension
        bucket_connection = s3_resource.meta.client.upload_file(photo_path_local, bucket_name, photo_path_dest)
        print("File uploaded")
        return True
    except Exception as err:
        print("Error", err)
        return False
