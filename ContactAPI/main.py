from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json 

with open("contacts.json", "r") as file:
    contacts = json.load(file)


app = FastAPI()

class Contact(BaseModel):
    name: str
    number: str



def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# contacts = [{"name": "dan",
#                 "number": "62727"}, {"name": "deb",
#                 "number": "292968"}]

@app.get("/")
def Home():
    return{"message": "Hello World"}


@app.get("/contacts")
def get_all_contacts():
    
    return contacts

@app.post("/contacts")
def add_contact(contact: Contact):
    contact_ids =[]
    for existing_contact in contacts:
        contact_ids.append(existing_contact["id"])
    highest_id = (max(contact_ids, default = 0))
    new_id = highest_id + 1
    new_contact = {"id" : new_id,
        "name": contact.name, 
                    "number": contact.number}
    contacts.append(new_contact)
    save_contacts()
    return new_contact

@app.get("/contacts/{contact_id}")
def get_contact_id(contact_id: int):
    for contact in contacts:
        if contact_id == contact["id"]:
            return contact
    
    raise HTTPException(status_code=404, detail="Contact does not exist")

@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    for existing_contact in contacts:
        if existing_contact["id"] == contact_id:
            existing_contact["name"] = contact.name
            existing_contact["number"] = contact.number
            save_contacts()
            return existing_contact
    else:
        raise HTTPException(status_code= 404, detail= "Contact does not exist")

@app.delete("/contacts/{contact_id}", status_code=204)
def delete_contact(contact_id: int):
    if  1 <= contact_id <= len(contacts):
        del contacts[contact_id - 1]
        save_contacts()
    else:
        raise HTTPException (status_code = 404, detail = "Contact does not exist")

