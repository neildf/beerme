import os
import urllib.request as request
import boto3

def lambda_handler(event, context):
    url = os.environ['BJCP_URL'] #'https://raw.githubusercontent.com/meanphil/bjcp-guidelines-2015/master/styleguide.xml'
    response = request.urlopen(url)
    data = response.read()

    s3= boto3.resource('s3')
    s3.Bucket('bjcp-resources').put_object(Key='bjcp.xml', Body=data)

    return 'success'
