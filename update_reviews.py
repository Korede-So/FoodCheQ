import os
import re
import random
from pathlib import Path

# Diverse pool of customer names
FIRST_NAMES = [
    "James", "Mary", "Robert", "Patricia", "Michael", "Jennifer", "William", "Linda",
    "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah",
    "Charles", "Karen", "Christopher", "Nancy", "Daniel", "Betty", "Matthew", "Margaret",
    "Mark", "Sandra", "Donald", "Ashley", "Steven", "Kimberly", "Paul", "Emily",
    "Andrew", "Donna", "Joshua", "Michelle", "Kenneth", "Carol", "Kevin", "Amanda",
    "Brian", "Melissa", "George", "Deborah", "Edward", "Stephanie", "Ronald", "Rebecca",
    "Anthony", "Sharon", "Frank", "Laura", "Ryan", "Cynthia", "Gary", "Kathleen",
    "Nicholas", "Amy", "Eric", "Angela", "Jonathan", "Shirley", "Stephen", "Anna",
    "Larry", "Brenda", "Justin", "Pamela", "Scott", "Emma", "Brandon", "Nicole",
    "Benjamin", "Helen", "Samuel", "Samantha", "Raymond", "Katherine", "Gregory", "Christine",
    "Jerry", "Debra", "Dennis", "Rachel", "Walter", "Catherine", "Patrick", "Carolyn",
    "Peter", "Janet", "Harold", "Ruth", "Clarence", "Maria", "Jose", "Heather",
    "Floyd", "Diane", "Jim", "Virginia", "Vincent", "Julie", "Ralph", "Joyce",
    "Roy", "Victoria", "Russell", "Olivia", "Louis", "Kelly", "Philip", "Christina",
    "Johnny", "Lauren", "Ernest", "Joan", "Martin", "Evelyn", "Randall", "Judith",
    "Vincent", "Megan", "Jared", "Andrea", "Chase", "Cheryl", "Nicholas", "Hannah"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Young",
    "Guzman", "Allen", "King", "Wright", "Scott", "Torres", "Peterson", "Phillips",
    "Campbell", "Parker", "Evans", "Edwards", "Collins", "Reeves", "Grant", "Harper",
    "Knight", "Ferguson", "Stone", "Hawkins", "Dunn", "Perkins", "Hudson", "Spencer"
]

RATINGS = [5, 5, 5, 4, 4, 5, 5, 4]  # Mostly 5-star reviews

def get_random_name():
    """Generate a random customer name"""
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    return f"{first} {last[0]}."

def get_star_rating(rating):
    """Convert numeric rating to star string"""
    filled = "★" * rating
    empty = "☆" * (5 - rating)
    return filled + empty

def update_reviews_in_html(file_path):
    """Update customer names and add HTML comments"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add comment block at the beginning of body if not present
    if "<!-- Product Page -->" not in content:
        content = content.replace("<body>", "<!-- FoodCheq Product Page -->\n<body>")
    
    # Add comment before product section
    if "<!-- Product Details Section -->" not in content:
        content = content.replace('<div class="container product-section">', 
                                  '<!-- Product Details Section -->\n  <div class="container product-section">')
    
    # Add comment before related items
    if "<!-- Related Products Section -->" not in content:
        content = content.replace('<h3 id="related-title">Related Items</h3>', 
                                  '<!-- Related Products Section -->\n    <h3 id="related-title">Related Items</h3>')
    
    # Add comment before customer reviews
    if "<!-- Customer Reviews Section -->" not in content:
        content = content.replace('<section class="container mt-5">',
                                  '<!-- Customer Reviews Section -->\n  <section class="container mt-5">')
    
    # Replace customer names in reviews with random names
    review_pattern = r'<h6 class="mb-0" style="color: var\(--main-green\);">([^<]+)</h6>'
    
    def replace_name(match):
        return f'<h6 class="mb-0" style="color: var(--main-green);">{get_random_name()}</h6>'
    
    content = re.sub(review_pattern, replace_name, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

# Get all HTML files in product category folder
product_dir = Path(r"c:\Users\DELL\Desktop\foodcheq\product category")
html_files = list(product_dir.glob("*.html"))

print(f"Found {len(html_files)} HTML files to update...")

for file_path in html_files:
    try:
        update_reviews_in_html(file_path)
        print(f"✓ Updated: {file_path.name}")
    except Exception as e:
        print(f"✗ Error updating {file_path.name}: {e}")

print("\nDone! All files updated with comments and randomized customer names.")
