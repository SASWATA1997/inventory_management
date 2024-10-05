from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class ItemTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='saswata', password='1234')
        assert self.user.is_active  # Ensure the user is active

        # Obtain a JWT token for the created user
        self.token = self.get_token()

    def get_token(self):
        url = reverse('api:token_obtain_pair')
        response = self.client.post(url, data={
            'username': 'saswata',  # Correct username
            'password': '1234'      # Correct password
        }, format='json')
        
        print(response.data)  # Debug print to see response
        if response.status_code != status.HTTP_200_OK:
            raise Exception("Token generation failed: {}".format(response.data))
        
        return response.data['access']  # Extract the access token

        def test_create_item(self):
        url = reverse('api:create-item')  # Include the namespace 'api'
        data = {
            "name": "Gold",
            "description": "It is an item"
        }
        
        # Set the Authorization header with the token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Send a POST request to create the item
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Assert successful creation
        self.assertEqual(Item.objects.count(), 1)  # Check if the item was created
        created_item = Item.objects.get()  # Retrieve the created item
        self.assertEqual(created_item.name, "Gold")  # Verify the item's name

    def test_item_creation_count(self):
        # Ensure no items exist before creating one
        self.assertEqual(Item.objects.count(), 0)  # Check initial count
        
        # Create the item
        url = reverse('api:create-item')  # Include the namespace 'api'
        data = {
            "name": "Gold",
            "description": "It is an item"
        }
        
        # Set the Authorization header with the token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        # Send a POST request to create the item
        self.client.post(url, data, format='json')
        
        # Check if the item was created
        self.assertEqual(Item.objects.count(), 1)  # Check if the item was created

        # Ensure the created item has the correct attributes
        created_item = Item.objects.get()  # Get the created item
        self.assertEqual(created_item.name, "Gold")  # Verify the item's name
