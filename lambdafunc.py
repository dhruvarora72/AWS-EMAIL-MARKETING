import boto3
import csv
# Initialize the boto3 client
s3_client = boto3.client('s3')
ses_client = boto3.client('ses')
def lambda_handler(event, context):
 # Specify the S3 bucket name
 bucket_name = 'aws-project-vit'
 try:
 
 csv_file = s3_client.get_object(Bucket=bucket_name, Key='contacts-contacts.csv')
 lines = csv_file['Body'].read().decode('utf-8').splitlines()
 
 email_template = s3_client.get_object(Bucket=bucket_name, 
Key='email_template.html')
 email_html = email_template['Body'].read().decode('utf-8')
 
 
 contacts = csv.DictReader(lines)
 
 for contact in contacts:
 
 personalized_email = email_html.replace('{{FirstName}}', contact['FirstName'])
 
 # Send the email using SES
 response = ses_client.send_email(
 Source=drashyajkm@gmail.com',
 Destination={'ToAddresses': [contact['Email']]},
 Message={
 'Subject': {'Data': 'Your Weekly Tiny Tales Mail!', 'Charset': 'UTF-8'},
 'Body': {'Html': {'Data': personalized_email, 'Charset': 'UTF-8'}}
 }
 )
 print(f"Email sent to {contact['Email']}: Response {response}")
 except Exception as e:
 print(f"An error occurred: {e}")
