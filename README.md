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
  > 
  > `django-filter==2.4.0`
  > 
  > `djangorestframework==3.12.2`
  > 
  > `requests==2.25.1`
  > 
  > `xhtml2pdf==0.2.5`

  To run the project on your local machine, Go to the `src` directory. There you'll find `manage.py` file,
  Then run 
  `python manage.py runserver` 
  and go to your browser and type 
  `localhost:8000` (by default `port:8000`,you can change it)
  
  <h3> Using the API:</h3>
  
  There are two APIs: 
  - `resultapi/` and 
  - `studentapi/` 
  
  (for local machine the url is like `localhost:8000/resultapi` and `localhost:8000/studentapi`)
  
  <h4>To filter grades:</h4>
  
    resultapi/:
  - stuId ( `localhost:8000/resultapi/?stuId=2017331001` )
  - semester ( `localhost:8000/resultapi/?semester=2` - to Filter only results of 2nd semester)
  - isMajor ( `localhost:8000/resultapi/?isMajor=true` - to Filter only results of 'Major' courses,in case of 'minor' put `false` )
  - isLab ( `localhost:8000/resultapi/?isLab=true` - to Filter only results of 'Lab' courses,in case of 'theory' put `false` )
  - credit ( `localhost:8000/resultapi/?credit=3` - to Filter only results of `3.00` credit courses)

to apply Multiple filters, use `&` between the filters 
example: `localhost:8000/resultapi/?stuId=2017331001&semester= 2&isMajor= true` 
to filter the result of major courses of 2nd semester of the student with Id-2017331001)

  <h4>To filter students:</h4>

    studentapi/:
  - reg ( `localhost:8000/resultapi/?reg=2017331001` )
  - session ( `localhost:8000/resultapi/?session=2017-2018` - to Filter the details of the students of 2017-2018 session)
  - name ( `localhost:8000/resultapi/?name=Alex Bob` - to Filter the details of student named `Alex Bob` )


  <h2>Admin Panel</h2>

      We have our customized admin panel.To login to admin panel on your local machine,enter the
      URL - `localhost:8000/admin`. In database we've the information of admin user.
      To log in, username- `admin`
                 password- `admin`
      
      You can add students details in `Students` section, results in 'Results` section.