<h1> Project350 </h1>
  This repo hosts files and codes for our 3rd year project for the course CSE350.

  This is a Django web application to help students search and look at their results; optionally using various filters. 
  The aims of this project were 

  - easy searching
  - good visual representation and
  - an API

  For this project we've used `python-3.8.1` .So To run this project You must use the same version or above.
  To install the dependencies go to project directory and run:

  `pip install -r requirements.txt`

  or
 
  `pip3 install -r requirements.txt`

  > `Django==3.1`
  > `django-filter==2.4.0`
  > `djangorestframework==3.12.2`
  > `requests==2.25.1`
  > `xhtml2pdf==0.2.5`

  To run the project on your local machine,Go to the `src` directory.There you'll find `manage.py` file,
  Then run `python manage.py runserver` and go to your browser and hit `localhost:8000` (by default `port:8000`,you can change it)
  
  How you can use our API:
  Here are two APIs: `resultapi/` and `studentapi/` (for local machine the url is like `localhost:8000/resultapi` and `localhost:8000/studentapi`)
  To filter:
  resultapi/:
  - stuId ( `localhost:8000/resultapi/?stuId=2017331001` )
  - semester ( `localhost:8000/resultapi/?semester= 2` - to Filter only result of 2nd semester)
  - isMajor ( `localhost:8000/resultapi/?isMajor= true` - to Filter only Major courses,for minor put `false` )
  - isLab ( `localhost:8000/resultapi/?isLab= true` - to Filter only results of Lab courses,for theory put `false` )
  - credit ( `localhost:8000/resultapi/?credit= 3` - to Filter only result of `3.00` credit courses)
  - to apply Multiple filters, use `&` between the filter ( `localhost:8000/resultapi/?stuId=2017331001&semester= 2&isMajor= true` - to filter the result of `stuId=2017331001`)
