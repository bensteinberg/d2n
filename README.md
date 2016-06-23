domain2orgs
===========

This is a Flask application for translating domain names to the organization(s) responsible for the relevant IP range.  You can run it locally like this:

    git clone https://github.com/bensteinberg/domain2orgs.git
    cd domain2orgs
    
then 

    virtualenv venv
    source venv/bin/activate
    
or

    mkvirtualenv venv
    
and

    pip install -r requirements.txt
    python app.py
