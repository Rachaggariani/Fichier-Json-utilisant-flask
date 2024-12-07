from flask import Flask, jsonify,Response
import xml.etree.ElementTree as ET
app = Flask(__name__)

products = [
    {"id": 1, "name": "Prod A", "price": 10.99},
    {"id": 2, "name": "Prod B", "price": 24.99},
    {"id": 3, "name": "Prod C", "price": 5.99}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})
contacts=[ 
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
    ]
@app.route('/api/contacts-xml',methods=['GET'])
def get_contacts_xml():
    root=ET.Element('contacts')
    for contact in contacts:
        item=ET.SubElement(root,'contact')
        ET.SubElement(item,'id').text=str(contact['id'])
        ET.SubElement(item,'name').text=str(contact['name'])
        ET.SubElement(item,'age').text=str(contact['age'])
    return Response(ET.tostring(root),content_type='text/xml')  
if __name__ == '__main__':
    app.run(debug=True, port=5002)
