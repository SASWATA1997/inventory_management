from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Item  # Ensure to import the Item model

User = get_user_model()  # Get the User model

class ItemTests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='Saswata', password='1234')
        
        # Obtain a JWT token for the created user
        self.token = self.get_token()

    def get_token(self):
        # Create a token for the user
        url = reverse('api:token_obtain_pair')  # Endpoint for obtaining token
        response = self.client.post(url, data={
            'username': 'Saswata',  # Use the same username
            'password': '1234'      # Use the same password
        }, format='json')

        # Check for response status and print for debugging
        if response.status_code != status.HTTP_200_OK:
            print("Failed to obtain token:", response.data)  # Debug print statement
            raise Exception("Token generation failed: {}".format(response.data))

        return response.data['access']  # Extract the access token

    def test_create_item(self):
        url = reverse('api:create-item')  
        data = {
            "name": "Bronze",
            "description": "It is a metal."
        }

        # Set the Authorization header with the token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Send a POST request to create the item
        response = self.client.post(url, data, format='json')

        # Assert successful creation
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  
        self.assertEqual(Item.objects.count(), 1)  # Check if the item was created
        self.assertEqual(Item.objects.get().name, "Bronze")  # Verify the item's name
