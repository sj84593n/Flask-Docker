# Python flask using docker container

This project includes fetching customer data for a online shopping website.The project includes database created in json format which consists of customer details such as customer_id,customer_name and their order details such as order_id,product,date_of_purchase.
We have created a RESTful Web service that runs in a docker container.
Our web service will contain four GET routes:

1.One that displays a collection of records.

2.One that displays a single record that corresponds to an ID

■Example:​ If I created two routes; /getallorders and /cust/3 (notethat 3 is the ID of a given customer in my database).
On that displays a collection of records for a given entity
■Example:​ /cust/3/orders (note that 3 is the ID of a given customer in my database). 
One that displays a single record from a collection of a given entity.
■Example:​ /cust/3/orders/1 (note that 1 is the ID of a given order submitted by customer with ID 3 in my JSON database.

How to run the project:

Requirments:
You must have Docker environment intalled your system.


Step 1: Build Docker Container using the command " docker build -t flask-project:latest . "


Step 2: Run the Docker container using the command " docker run -d -p 5000:5000 flask-project "
        Now you can access all the APIs on browser using IP of your machine.
        
        
        Please use RESTful APIs explained above to fetch desired records. 



