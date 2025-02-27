from bs4 import BeautifulSoup
import html5lib

# HTML content
html_object = """
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
<table>
  <tr>
    <td id='flight'>Flight No</td>
    <td>Launch site</td> 
    <td>Payload mass</td>
  </tr>
  <tr> 
    <td>1</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>300 kg</td>
  </tr>
  <tr>
    <td>2</td>
    <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
    <td>94 kg</td>
  </tr>
  <tr>
    <td>3</td>
    <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
    <td>80 kg</td>
  </tr>
</table>
"""

# Create a BeautifulSoup object with html5lib parser
table_ds = BeautifulSoup(html_object, 'html.parser')

# Find all table rows
table_rows = table_ds.find_all('tr')
print(table_rows)

first_row = table_rows[0]
print(f"This is first row: {first_row}")

print(f"This is the type of first row {type(first_row)}")

print(f"This is the child of first row: {first_row.td}")


# Find all elements without the href attribute
# elements_without_href = table_ds.find_all(href=False)
#
# print(elements_without_href)

# find element by id

print(table_ds.find_all(id='flight'))
