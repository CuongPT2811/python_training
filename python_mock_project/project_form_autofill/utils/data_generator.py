import random
from faker import Faker
from datetime import datetime 
import os
import json 


#Init Faker to create fake data
fake = Faker('en_US')

def generate_user_profile():
    """
    Fake a random user profile to fill in the form
    """
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    #List available choice of the form
    genders = ['Male', 'Female', 'Other']

    hobbies = ['Sports', 'Reading', 'Music'] 

    subjects = [
        'Maths', 'Physics', 'Chemistry', 'Computer Science', 'Economics',
        'Biology', 'Arts', 'History'
    ]
    
    states = {
        "NCR": ["Delhi", "Gurgaon", "Noida"],
        "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
        "Haryana": ["Karnal", "Panipat"],
        "Rajasthan": ["Jaipur", "Jaiselmer"]
    }

    #Random state, then random city based on choosen state
    state_choice = random.choice(list(states.keys())) 
    city_choice = random.choice(states[state_choice])

    #Create a fake png file for image to upload
    #Make sure it's placed in the same folder with the script
    picture_filename = "dummy_image.png"
    #Check if the dummy_image available to advoid create again
    if not os.path.exists(picture_filename):
        with open(picture_filename, "w") as f: #Dummy file for image
            f.write("This is a dummy image file for testing purposes.")
        print(f"Created dummy image file: {picture_filename}") #Announced while create file
    else:
        print(f"Dummy image file already exists: {picture_filename}")

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": f"{first_name.lower()}.{last_name.lower()}@example.com",
        "gender": random.choice(genders),
        "mobile": fake.msisdn()[:10], #Get the first 10 digit
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=60), #Random birthday 
        "subjects": random.sample(subjects, k=random.randint(1, 3)), #Choose random subject
        "hobbies": random.sample(hobbies, k=random.randint(1, 2)), #Choose random hobbies
        "picture_path": os.path.abspath(picture_filename), #Get the absolute path of image
        "address": fake.address().replace('\n', ', '), #Change address to a single line
        "state": state_choice,
        "city": city_choice
    }

if __name__ == '__main__':
    print("Generating user profile data...")
    user_data = generate_user_profile()
    print(json.dumps(user_data, indent=4, default=str, ensure_ascii=False))
    print("\nData generation complete.")

