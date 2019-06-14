from flask import render_template, redirect, url_for, flash
from app import application
from app.forms import SignUpForm
import boto3

# access a dynamodb resource through boto.

'''
It is possible to create a resource and manage it using boto
but in this tutorial it is already created in aws web console
'''
db = boto3.resource('dynamodb', region_name='us-west-2')

# table already created in aws console

table = db.Table('signuptable')

# create a sns resource
notification = boto3.client('sns', region_name='us-west-2')

# this is the way to identify a resource through arn
topic_arn = 'arn:aws:sns:us-west-2:502010945762:flask-aws-sns'


@application.route('/')
@application.route('/home')
def home_page():
    return render_template('home.html')


@application.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        table.put_item(
            Item={
                'name': form.name.data, 'email': form.email.data,
                'mobile': form.mobile.data, 'country': form.country.data,
                'newsletter': form.newsletter.data
            }
        )
        msg = 'Congratulations !!! {} for signing in !'.format(form.name.data)

        # a flash message thorugh flask framework
        flash(msg)

        # mail to app owner, its me now created a sns service to vivekster account
        email_message = '\nname: {} ' \
                        '\nmobile: {} ' \
                        '\nemail: {} ' \
                        '\ncountry: {}'.format(form.name.data, form.mobile.data, form.email.data, form.country.data)
        notification.publish(Message=email_message, TopicArn=topic_arn, Subject="You've Got A Mail")
        return redirect(url_for('home_page'))
    return render_template('signup.html', form=form)
