
# _Authentication mechanism in REST_

### Basic authentication

- Basic authentication is an HTTP-based authentication approach and is the simplest way to secure REST APIs. It uses a Base64 format to encode usernames and passwords, both of which are stored in the HTTP header.
- This approach doesn't offer out-of-the-box support for multifactor authentication (MFA) or dynamic, user-specific credentials, which would require the use of additional browser-based extensions and authorization tooling.
- key challenges
	- sensitive credentials often travel between systems unencrypted.
	- using Secure Sockets Layer (SSL) and Transport Layer Security (TLS) channels is a must when sharing sensitive data between multiple web applications

### API keys

- variation of the HTTP Basic authentication strategy
- This approach uses machine-generated strings to create unique pairs of identifying credentials and API access tokens
- API keys can be sent as part of the payload, HTTP headers or query string, making them a good fit for consumer-facing web applications.
- key challenges
	- Unfortunately, API keys are susceptible to the same risks as Basic authentication
	- the simplicity of its design inhibits its ability to support layered authentication or MFA.

### HMAC encryption (Hash-Based Message Authentication Code)

- often used when the integrity of the REST API's data payload is a priority.
- HMAC uses symmetric encryption -- sometimes called single-key encryption -- to determine the hashing of a REST API's data payload.
- It then generates a unique code associated with that hashing and attaches that code to the relevant messages. The caller and receiver will share the key and use it to ensure the integrity of the data within the payload.

### OAuth 2.0

- OAuth 2.0 can support dynamic collections of users, permission levels, scope parameters and data types
- It's a preferred approach for organizations looking to secure large numbers of REST APIs that contain sensitive information.
- OAuth 2.0 creates secured access tokens that are refreshed periodically using a series of procedural verification protocols known as grant types. (grant types act as proxy authentication mechanisms)


### OpenID Connect

- open standard authentication protocol built on top of OAuth 2.0
- It provides a simple way for a client application -- referred to as a relying party (RP) -- to validate a user's identity.
- This single standard facilitates information sharing without the need for explicit management of credentials for third-party applications.
- REST APIs covered by OpenID Connect become usable once users have been authenticated by the RP
- Eventually, the API associated with that RP can perform validation using its own variation of the OAuth grant types mentioned above. These grant types are:
		- Authorization Code
		- Implicit
		- Hybrid