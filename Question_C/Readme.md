# Geo Distributed LRU

The program uses the microservices architecture, each service has its own cache and the clients (CANADA, USA, BRAZIL) are connected on a central (Server). This program stores the data received by HTTP into some caches.
The great advantage of this structure is the scalability, flexibility and resilient to network problems.



# Installation

- Create virtual environment: python3 -m venv name
- Install Required packages: pip3 install -r Requirements.txt
- Install Docker ([LINK](https://docs.docker.com/install/))
- Pull and Run RabbitMQ Service >> ($ docker run -p 5672:5672 --hostname nameko-rabbitmq rabbitmq:3)
- Start all services >> (nameko run clients)
- Interact on Port 8000 using CURL or POSTMAN.



# How it works

## -> COMPONENTS

SERVER: (HTTP GET/POST)
CLIENTS: (CANADA,USA,BRAZIL)
SERVICES: (canada_client,usa_client,brazil_client)


## -> ENDPOINTS

POST: {ip_server}:8000/post/<string:client_aim>
GET: {ip_server}:8000/cache/<string:client_aim>/<string:code>


## -> GET/POST

The Server receive requests by GET/POST

- GET
The server checks if has the requested data (Program Language) and deliver back its cache.
If server hasn't the needed data then it calls a Client (service) by RPC Protocol (Nameko)
Through the RPC the client is able to send its cache to the endpoint.
(Clients Services get_cache())

- POST
The server add the data into its own cache or send to specific client.
(Clients Services add_cache())

## -> SERVER

The SERVER has 2 decorators http from Nameko library exposing 2 entry points.
(do_post() & get_cache())
Whatsmore, it has add_cache() to add new data into cache, and also expire_cache() to delete unnecessary caches.


## -> CLIENTS

Clients services manage its own caches and deliver some data to server.
They have add_cache(), get_cache() and expire_cache() functions


## -> MISSING FUNCTIONALITIES

Locality of reference, data should almost always be available from the closest region
