# checkpoints
A Django application with an API endpoint that accepts a string of comma separated points for example “(2,3), (1,1), (5, 4), ...” and calculates the closest points. It then stores them in a table with the following details: 
-The string of points submitted 
-The result of the computation: the closest points pair.

API:

The following main URLs are now available:

    GET /checkpoints/ — lists all the points that have been checked
    POST /checkpoints/ — checks for nearest points and saves to DB
    GET /checkpoints/:id — gets one query using its id
    GET /admin/ - app admin
    
Examples

1: GET /checkpoints/

	GET query: Empty Body
	
	Response:
	
	{
	    	"data": [
			{
			    "type": "CheckedPoints",
			    "id": "1",
			    "attributes": {
				"query": "(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)",
				"response": "(1, 1), (-1, -1)",
				"check_date": "2021-07-27T21:00:00Z"
			    }
			},
			{
			    "type": "CheckedPoints",
			    "id": "2",
			    "attributes": {
				"query": "(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)",
				"response": "(1, 1), (-1, -1)",
				"check_date": "2021-07-27T21:14:00Z"
			    }
			},
			{
			    "type": "CheckedPoints",
			    "id": "3",
			    "attributes": {
				"query": "(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)",
				"response": "(1, 1), (-1, -1)",
				"check_date": "2021-07-27T21:14:15Z"
			    }
			}
		]
	}
	
2: GET /checkpoints/:id

	GET query: Empty Body

	Response:
	
	{
	    "data": {
		"type": "CheckedPoints",
		"id": "1",
		"attributes": {
		    "query": "(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)",
		    "response": "(1, 1), (-1, -1)",
		    "check_date": "2021-07-28T00:00:00+03:00"
		}
	    }
	}

3: POST /checkpoints/

	POST query:
		{
		  "data": {
		    "type": "CheckedPoints",
		    "attributes": {
			"query": "[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]"
		    }
		  }
		}

	Response:
	
		{
		    "data": {
			"type": "CheckedPoints",
			"id": "34",
			"attributes": {
			    "query": "[(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]",
			    "response": "((1, 1), (-1, -1))",
			    "check_date": "2021-07-28T20:39:56.536415Z"
			}
		    }
		}
	
NB: A postman collections file is included for testing	

How to Run:
===========



	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
