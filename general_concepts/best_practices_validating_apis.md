Important Links

https://restfulapi.net/http-status-codes/
https://www.softwaretestinghelp.com/rest-api-response-codes/


# Best Practices While Validating A REST API


### 1) CRUD Operations
- Consist of minimum 4 methods provided and should be working in the Web API. GET, POST, PUT and DELETE.

### 2) Error Handling 
- Possible hints for the API consumers about the error and why it has occurred. It also should provide granular level error messages.

### 3) API Versioning 
- Use the letter ‘v’ in the URL to denote the API version. For example- 
- http://restapi.com/api/v3/passed/319 
- Additional parameter at the end of the URL 
- http://restapi.com/api/user/invaiiduser?v=6.0

### 4) Filtering
- Enabling the user to specify, select the desired data instead of providing them all at a time. /contact/sam?name, age, designation, office
        /contacts?limit=25&offset=20

### 5) Security
- Timestamp in each and every API Request and Response. Use of access_token to make sure that API is invoked by the trust parties.

### 6) Analytics
- Having Analytics in your REST API will give you a good insight of API under test especially when the number of records fetched is very high.

### 7) Documentation
- Proper documentation is to be provided so that API consumers can use it and consume the services effectively.

### 8) URL Structure
- URL structure should remain simple and a user should be able to read the domain name easily over it. 
- For Example, https://api.testdomain.com. 
- Operations to be performed over the Rest API should also be very easy to understand and perform.


### For Example, for an Email client:

- GET: read/inbox/messages – Retrieves the list of all message under inbox
- GET: read/inbox/messages/10 – Reads 10th message in inbox
- POST: create/inbox/folders – Create a new folder under inbox
- DELETE: Delete/spam/messages – Delete  all the messages under spam folder
- PUT: folders/inbox/subfolder – Update the information relating to the subfolder under inbox.

