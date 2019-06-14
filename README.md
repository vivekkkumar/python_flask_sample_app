# python_flask_sample_app
A python web app deployed in AWS.

This uses the Dynamo DB for Creating and reading records. 

This application was deployed with elastic beanstalk without load balancers. (Single instance) in AWS.

aws_cli needs to be installed.

1. Initializie the application by #eb init
2. There will be series of prompts, like region
3. Access ID, key.
4. Name for application, instance number, python version etc

Then,

Create an environment inside the application, using eb console to login to elastic beanstalk page
#eb create “environment”

EB will create all the instances necessary for the application.

Hostname will be the name given during the init and followed by region and elasticbeanstalk.com

After making changes to the code, we can deploy the application using 

#eb deploy -l “version_name”

This will deploy the code changes and newest version to the elastic beanstalk.
 
