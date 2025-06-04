import boto3

def lambda_handler(event, context):
    # Entrada
    bucket = event['body']['bucket']
    directorio = event['body']['directory']  #Debe terminar en '/' !!!!!!!!!!

    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=directorio)

    # Salida
    return {
        'statusCode': 200,
        'body': {
            'message': f'Directorio {directorio} creado en el bucket {bucket}'
        }
    }
