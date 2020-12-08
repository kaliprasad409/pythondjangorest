from rest_framework.test import APIClient


# Using the standard ReqquestFactory to create a form POST
client = APIClient()
response = client.post('/snippets/', {"title": "Third Snippets", "code": "print(\"hello world\")",
                                      "linenos": False, "language": "python", "style": "pep8"})



