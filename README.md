# apis-benchmark
Simple REST API Benchmark:  Django Rest Framework x Flask x API Star
 
### Database
###### PostgreSQL 10.4-1 (run in Docker)

### Django
###### Django==2.0.5
###### djangorestframework==3.8.2

### Flask
###### Flask==1.0.2
###### Flask-SQLAlchemy==2.3.2
###### SQLAlchemy==1.2.7

### ApiStar
###### apistar==0.5.18
###### apistar-sqlalchemy==0.3.1
###### SQLAlchemy==1.2.7


# Benchmark:

### Test 1: GET - return JSON with 1000 records
Test with Postman

#### Django: 78ms
#### Flask: 64ms
#### ApiStar: 82ms


