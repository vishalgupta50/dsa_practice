# Different Type Of REST Requests

Here we will discuss each and every method of REST API along with the collections.

### Method	Description
- GET       Fetch status line, Response body, Header etc.
- HEAD      Same as GET, but only fetch status line and header section
- POST	    Perform request using request payload mostly in creating a record at the server
- PUT	    Useful in manipulating/updating the resource using Request payload
- DELETE    Deletes information relating to the target resource.
- OPTIONS   Describe the communication options for the target resource
- PATCH	    Very much similar to put but it is more like a minor manipulation of resource content

Note: There are so many methods that exist, which we can do using POSTMAN but we will be discussing only the following methods using POSTMAN.

We shall use a dummy URL to demonstrate  http://jsonplaceholder.typicode.com. This URL shall give us the desired responses but there will not be any creation, modification in the server.

# 1) GET
Request Parameters:
Method: GET
Request URI: http://jsonplaceholder.typicode.com/posts
Query Parameter: id=3;

Response Received:
Response Status Code: 200 OK

Response body:

Response body


# 2) HEAD
Request Parameters:
Method: HEAD
Request URI: http://jsonplaceholder.typicode.com/posts


HEAD



#3) POST
POST



#4) PUT
PUT

DELETE

#5) OPTIONS
Request Parameters:
Method: OPTIONS
Request URI: http://jsonplaceholder.typicode.com/
Headers: Content-type = Application/JSON

OPTIONS

#6) PATCH
PATCH

