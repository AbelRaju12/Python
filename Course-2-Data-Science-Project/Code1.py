from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests # for downloading webpages
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())  # in html format ordered
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))
# tag_child =tag_object.b to access b child of tag object
# parent_tag=tag_child.parent to get access of parent of tag child
# sibling_1=tag_object.next_sibling for siblings

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")
table_rows=table_bs.find_all('title')
print(table_rows)
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('column',j,"cell",cell)
        
        
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print (list_input)        