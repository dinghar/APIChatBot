# TODO: Pass example for how to format request

testChat = [{"role": "user", "content": "Please format a request to query the API described for the user's request"}, {"role": "user", "content": """
openapi: 3.0.0
    info:
    title: Simple API
    version: 1.0.0
    description: A simple API with a single GET route
    servers:
    - url: http://example.com/api/v1
        description: Local server
    paths:
    /example:
        get:
        summary: Get example data
        operationId: getExample
        responses:
            '200':
            description: Successful response
            content:
                application/json:
                schema:
                    type: object
                    properties:
                    message:
                        type: string
                        example: "This is a simple example response."
            '400':
            description: Bad request
            '404':
            description: Not found
            '500':
            description: Internal server error
"""}, {"role": "system", "content": "I want to get example data"}]