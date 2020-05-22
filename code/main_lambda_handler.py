import os, json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

def main_lambda_handler(event, context):
    message = Mail(
        from_email='from@example.com',
        to_emails=["to@example.com", "to@example.com"],
        subject='Testing Email from SendGrid Lambda',
        html_content='<strong>Testing Email from App</strong>')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email sent Successfully!')
    }
