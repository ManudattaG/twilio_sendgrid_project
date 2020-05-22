# TWILIO SENDGRID EMAIL

Twilio SendGrid’s Email API triggers an email with a simple API call by managing all the contents, deliverables, templates and automatically displays the latest content in your email.

## Overview:
There's a platform built(ChatBot) wherein I am using Twilio SendGrid to send emails related to Major Incident ticket details raised by the support team. It is intended that whenever a Major Incident occurs, it will be the bot's responsibility to retreive all the required details for ex: incident details, business impact, time, incident commanders, incident managers, whom to notify via email, list of users etc.. Bot then triggers an email to the users with all the details by using SendGrid template.

## Pre-requisites

* Python
* AWS Lambda (Optional)
* SendGrid Email API Endpoint
* SENDGRID_API_KEY
  
### Libraries:
* python_http_client or requests
* sendgrid.helpers.mail (optional)
