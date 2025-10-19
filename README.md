# core-python-assignment
**1. E-Commerce Cart System** 

Scenario:

You are designing the logic for an e-commerce website. Write a program to calculate the total price of items in a user's cart. If the cart contains more than 5 items, apply 10% discount.

Requirements:

- Use a function to calculate the total price.

- Handle cases where the cart is empty.

Input Example:

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

Expected Output:

Total Price: 54000



**2. Restaurant Menu Management**

Scenario:

You are managing a restaurant's menu. Write a program to update the menu by adding or removing items and allow users to check if a particular item is available.

Requirements:

- Use functions for adding, removing, and checking menu items.

- Handle cases where the item to be removed does not exist.

Input Example:

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item = "Tacos"

remove_item = "Salad"

check_item = "Pizza"

Expected Output:

Updated menu: ["Pizza", "Burger", "Pasta", "Tacos"]

Availability: "Pizza is available"



**3. Classroom Performance Tracker**

Scenario:A teacher wants to track student performance. Write a program to calculate the **average marks** of students and identify the **top performer**.

Requirements:

- Use a function to calculate the average marks.

- Identify the student with the highest average.

- Optional: Implement a `Student` class to handle this logic.

Input Example:

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

Expected Output:

Average Marks: {"John": 85, "Alice": 87.33, "Bob": 75}

Top Performer: "Alice"

 

**4. Movie Ticket Booking System**

Scenario:

A cinema hall wants to manage ticket bookings. Write a program to keep track of **available** and **booked seats**. Allow users to **book** or **cancel** a seat.

Requirements:

- Use functions to handle seat booking and cancellation.

- Prevent booking an already booked seat.

Input Example:

total_seats = 10

booked_seats = [2, 5, 7]

book_seat = 3

cancel_seat = 5

Expected Output:

Available seats: [1, 4, 6, 8, 9, 10]

 

**5. Hospital Patient Management**

Scenario:

A hospital needs a system to manage patient records. Write a program to store patient data, including **name, age, and disease**, and allow the admin to search for patients by disease.

Requirements:

- Store patient records in a list of dictionaries.

- Allow searching for patients based on disease.

- Optional: Use a `Patient` class to manage records.

Input Example:

patients = [

    {"Name": "Alice", "Age": 30, "Disease": "Flu"},

    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},

    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}

]

search_disease = "Flu"

Expected Output:

Patients with Flu: ["Alice", "Charlie"]

 

**6. Customer Feedback Analysis**

Scenario:

A company collects customer feedback in the form of ratings (1-5). Write a program to calculate the **percentage of positive feedback** (4 or 5).

Requirements:

- Use a function to calculate the positive feedback percentage.

- Handle cases where no ratings are available.

Input Example:

```python

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

```

Expected Output:

```

Positive Feedback: 62.5%

```

---

 

**7. Taxi Fare Calculation**

Scenario:

A taxi service calculates fares based on the following rates: 

- **Base fare**: $50 

- **Distance fare**: $10/km 

Write a program to calculate the total fare for multiple trips.

Requirements:

- Use a function to calculate fare for each trip.

Input Example:

```python

trips = [5, 10, 3]  # Distances in km

```

Expected Output:

```

Trip 1: $100

Trip 2: $150

Trip 3: $80

Total Fare: $330

```
