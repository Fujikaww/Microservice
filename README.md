Instructions:

    1. Install dependencies by typing "pip install fastapi uvicorn pydantic"
    2. Make sure you have REST client installed

Making a Request:

    1. Create an http file with a method (in this case POST) followed by a URL to the path you'd like the request sent to
    2. Specify the content type of the data being sent (application/json)
    3. Add a "numbers" list containing the numbers that you would like averaged, counted, and compared

    Example:
    POST http://127.0.0.1:8000/api/average
    Content-Type: application/json

    {
        "numbers": [10, 20, 30]
    }

    4. Click on the send request just above POST

Recieving a Request:

    1. Once a request is sent, a separate tab will open containing the desired output
    
    Example:
    HTTP/1.1 200 OK
    date: Sun, 17 Nov 2024 02:08:32 GMT
    server: uvicorn
    content-length: 16
    content-type: application/json
    Connection: close

    {
    "average": 20.0
    }
    
