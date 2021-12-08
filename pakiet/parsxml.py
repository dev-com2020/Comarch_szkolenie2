from xml.dom import minidom

Tree = minidom.parse('plik.xml')

#print(Tree.toxml())

nodes = Tree.childNodes
for i in nodes[0].getElementsByTagName("osoba"):
    print(i.getElementsByTagName("imie")[0].childNodes[0].toxml())
    print(i.getElementsByTagName("imie")[0].nodeName)
    print(i.getElementsByTagName("imie")[0].getAttribute("atrybut"))


#print(nodes[0].getElementsByTagName("osoba")[0].toxml())

