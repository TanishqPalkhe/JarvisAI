import re
mystr="1233456,+915286317231,87698755,8796098004,919528124081,+9106276900"
patt=re.compile(r'\+91\d{10}')
mat=patt.finditer(mystr)
for mate in mat:
    print(mate)
mystr1 = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata56@gmail.com
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Email:rtutuy@gmail.com
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@gmail.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''
i=1
with open ("Nb.txt",'w')as f:
    ty=re.compile(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]')
    total=ty.finditer(mystr1)
    for items in total:
        print(items)
        str1=str(items)
        strong=str1
        f.write(strong)





















