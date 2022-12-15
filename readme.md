----------------------------
        Description
----------------------------

A Django based web store. Where users can register buy products and review their purcahse. I integrated Paypal for payments. 
[https://github.com/kubeshauseli17/Project-4]
----------------------------
        Stretch Goals
----------------------------

I'd love to add functionality so that people could register and create their own store fronts and start selling products seamlessly. 
I was only able to get a simple e-com site together at this point so I chose to flush out a page I'd like to have someday. 
I want to add Stripe and Apple Pay sometime soon to round out the payments accepted. 
I also want to dial in the styling more to really make this shine and to make it mobile friendly.

----------------------------
        Reflections
----------------------------

I really wish I hadn't killed my old laptop with an inadvertant coffee spill on night 1. That was a expensive and painful mistake with this project.
For as much as I got done on this project I still feel I am behind where I was hoping to be at this point. I'm going to polish this project up and add 
to it once this cohort is over. I think all things considered at least it's currently functional. Albeit not exactly like I was hoping and not as stylized 
as I would've liked. Longer term I would like to migrate over to Postgres as well.

----------------------------
         Technology
----------------------------

HTML, CSS, Django, Bootstrap, SQLITE3

----------------------------
        User Stories 
----------------------------

As a visitor I’d like to browse listed items. I’d also like to register for an account once I find one I’d like to buy.

As a user I’d like to review an item I bought.

As a user I’d like to buy a listed item. I’d like to pay with my card and have shipping calculated based off my address.

As a merchant I’d like the users to be able to review if I’ve given them good quality service.

As a merchant I’d like users to be able to pay me as seamlessly as possible.


------------------------------
        Installation
------------------------------

- Clone the repository - git clone https://github.com/kubeshauseli17/Project-4.git

- Navigrate to the working directory

- Create virtual environment - python3 -m venv venv

- Activate the virtual environment - source .venv/bin/activate

- Install required packages - pip install -r requirements.txt

- Create environment variables in a .env file

SECRET_KEY=(Paypal Developer Secret key)
DEBUG=True
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=emailaddress@gmail.com
EMAIL_HOST_PASSWORD=yourPassword
EMAIL_USE_TLS=True

- Create Database - python3 manage.py migrate

- Create Super User - python3 manage.py createsuperuser

- Run Server - python manage.py runserver

- Login as Admin - (http://127.0.0.1:8000/securelogin/)

-------------------
        ERD
-------------------

![](https://github.com/kubeshauseli17/Project-4/blob/master/ERD.png)

------------------------------
          Wireframes
------------------------------

![](https://github.com/kubeshauseli17/Project-4/blob/master/p4%20homepage.png)
![](https://github.com/kubeshauseli17/Project-4/blob/master/p4%20item%20page.png)

------------------------------
        Daily Breakdown
------------------------------
Tuesday 10-25 – Planning, Researching Django and React together
Wednesday 10-26 – Django Day (Get my backend working)
Thursday 10-27 --  Django Day (Get React linked up and happy with my backend)
Friday 10-28 – Stripe and API day
Saturday 10-29 – Bug solving day
Sunday 10-30 – Bug solving day / Styling / Adding depth
Monday 10-31 Anxiety Day   