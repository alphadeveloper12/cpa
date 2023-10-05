from random import sample
from .models import *  # Import the CPALink model

def custom_data(request):
    # Retrieve 5 random CPALink objects
    random_cpas = CPALink.objects.order_by('?')[:5]
    random_blogs = BlogPost.objects.order_by('?')[:5]

    # Define the data dictionary with the custom data
    data = {
        'custom_data_key': 'Custom data value',
        'random_cpas': random_cpas,  # Add the random CPALinks
        'random_blogs': random_blogs,  # Add the random CPALinks
    }
    return data
