Flask-Mailgun
===========


Introduction
------------

Flask-Mailgun is a simple-to-use [Flask] (http://flask.pocoo.org/) extension that lets you
send mail from your application through [Mailgun](https://mailgun.com). It is built on top of [requests](http://docs.python-requests.org/en/master/user/quickstart/), an HTTP library for Python.

Mailgun allows you to send mail throught SMTP or thorugh REST calls.  This extension uses the REST API, and sends mail from your application through POSTS to the Mailgun API.  Sending mail through POST calls is benifical because it means you have a guarnatted interface for sending mail, there is no chance that your application will become stalled while it tries to negotiate with an SMTP server.

Since this extension uses a 3rd party (Mailgun) to send your emails, you must have a valid account with Mailgun to use it.

Once you have registered your account, you will be able to start sending emails.

Flask-Mailgun is an active project and ready to use today.

Documentation
-------------

### Installation
To install, if you are using a virtual environment you should first switch to that.  You can use pip to install:

    pip install flask-mailgun
    
Or alternatively, you can download the repository and install manually by doing::

    git clone git@github.com:sleekslush/flask-mailgun.git
    cd flask-mailgun
    python setup.py install

### Setting up the project
First you will need to find your Mailgun _domain_ and _apikey_.  They can be located in your mailgun

You can find your API key on your [Mailgun Dashboard at https://mailgun.com/app/dashboard](https://mailgun.com/app/dashboard). Open your dashboard and find "API Key".  Your domain, is either the custom domain you registered with mailgun ('www.example.com') or the subdomain that you setup ('example.

    MAILGUN_DOMAIN='<YOUR DOMAIN>'
    MAILGUN_API_KEY='<YOUR API KEY>'
    
You may also want to set the default from email, so that if you do not provide a _from_ account when you send an email, this email will be used in it's place.
    
    MAILGUN_DEFAULT_FROM='someone@yourdomain.com'

                
**Development Settings**
                
A good practice is to use the mailgun sandbox for local development. If your application has a development and production settings that differ, it would make sense to use the sandbox for development. There is no charge for sending emails through sandbox, and you can view them on the mailgun website.

    MAILGUN_DOMAIN='sandboxXX.mailgun.org'
    
### Sending mail
#### Create the Mailgun Object
To send an email, first import flask-mailgun, and then create an instance of the _Mailgun_ object.  You will need to pass this the app object so that it can find the settings that it needs, and you can either do this on object creation:

    mailgun = Mailgun(app)

or later in your application with:

	mailgun = Mailgun()
	mailgun.init_app(app)

#### Send an email

    data = {"from" : "Awesome User <auser@example.com>", 
            "to" : ["someone@otherdomain.com"], 
            "subject" : "First test", 
            "text": "Sending my email!"}
    mailgun.send_email(**data)
    
The [Mailgun API Documentation](https://documentation.mailgun.com/user_manual.html#sending-via-api) has more information on the parameters that you can use, and what you can send with it.    

#### Sending a file attachment

    from yourapplication import mailgun

    response = mailgun.send_email(
    data={
        "from": "Excited User <mailgun@YOUR_DOMAIN_NAME>",
        "to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
        "subject": "Hello",
        "text": "Testing some Mailgun awesomness!"
    },
    files=[
        ("attachment", open("files/test.jpg")),
        ("inline", open("files/inline_test.jpg"))
    ]
    )

    print(response)
    # {
    #    "message": "Queued. Thank you.",
    #    "id":    "<20111114174239.25659.5817@samples.mailgun.org>"
    # }

### Contributors
- Craig Slusher
[sleekslush](https://github.com/sleekslush)
- Jacob Magnusson
[jmagnusson](https://github.com/jmagnusson)
- Michael Lynch
[nycynik](https://github.com/nycynik)
- Hammy Goonan
[hammygoonan](https://github.com/hammygoonan)
