# API Design

## V1 Application Endpoints

GET /applications  
POST /applications  
GET /applications/{id}  
PUT /applications/{id}  
DELETE /applications/{id}  

## Query Parameters

GET /applications?company=Google  
GET /applications?status=Applied  
GET /applications?source=LinkedIn  
GET /applications?sort_by=deadline  
GET /applications?page=1&limit=20  

## Future Auth Endpoints

POST /auth/register  
POST /auth/login  
GET /users/me  

## Future Stats Endpoints

GET /stats/applications-by-status  
GET /stats/applications-by-source  
GET /applications/upcoming-deadlines  

## Valid Status Values

- Saved
- Applied
- OA
- Interview
- Rejected
- Offer
- No Response
