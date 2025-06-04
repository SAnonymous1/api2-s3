import boto3
import base64

def lambda_handler(event, context):
    # Entrada
    bucket = event['body']['bucket']
    key = event['body']['key']
    data_b64 = event['body']['data_b64']

    # Proceso
    contenido = base64.b64decode(data_b64)
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=contenido, ContentType='image/png')

    # Salida
    return {
        'statusCode': 200,
        'body': {
            'message': f'Archivo {key} subido correctamente al bucket {bucket}'
        }
    }
