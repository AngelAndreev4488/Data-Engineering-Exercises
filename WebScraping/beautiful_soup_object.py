from bs4 import BeautifulSoup
import requests

# HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<h3><b id='boldest'>Lebron James</b></h3>
<p> Salary: $ 92,000,000 </p>
<h3> Stephen Curry</h3>
<p> Salary: $85,000, 000 </p>
<h3> Kevin Durant </h3>
<p> Salary: $73,200, 000</p>
</body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all player names and their salaries
players = soup.find_all('h3')
salaries = soup.find_all('p')

# Extract and print the names and salaries
for player, salary in zip(players, salaries):
    player_name = player.get_text().strip()
    player_salary = salary.get_text().strip().replace("Salary:", "").strip()
    print(f"{player_name}: {player_salary}")

tag_object = soup.title
print("tag object:", tag_object)

# Find the h3 tag containing "Stephen Curry" using string (with leading space)
stephen_curry_tag = soup.find('h3', string=' Stephen Curry')

# Check if the tag was found
if stephen_curry_tag is not None:
    # Use next_sibling to get the salary
    salary_tag = stephen_curry_tag.next_sibling.next_sibling
    # Using .next_sibling twice to skip over the newline character
    if salary_tag is not None:
        salary = salary_tag.get_text().strip().replace("Salary:", "").strip()
        print(f"Stephen Curry's salary: {salary}")
    else:
        print("Salary tag not found.")
else:
    print("Stephen Curry tag not found.")
