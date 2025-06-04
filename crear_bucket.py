import boto3

def lambda_handler(event, context):
    # Entrada
    nombre = event['body']['bucket_name']

    # Proceso
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre)

    # Salida
    return {
        'statusCode': 200,
        'body': {
            'message': f'Bucket {nombre} creado correctamente'
        }
    }

