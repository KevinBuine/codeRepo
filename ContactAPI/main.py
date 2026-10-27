from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import json 

BASE_DIR = Path(__file__).resolve().parent
CONTACTS_FILE = BASE_DIR / "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
            if not isinstance(contacts, list):
                raise ValueError("Contacts.json must contain a list of contacts")
            required_keys = {"id", "name", "number"}
            seen_ids = set()
            for contact in contacts: 
                
                if not isinstance (contact, dict):
                    raise ValueError("Every contact must be a dictionary")
                
                if not required_keys.issubset(contact):
                    raise ValueError("Contact is missing one or more required keys")
                
                if type(contact["id"]) != int:
                    raise ValueError("contact id must be an integer")
                if contact["id"] <=0:
                    raise ValueError("Contact ID must be greater than zero")
                
                if contact["id"] in seen_ids:
                    raise ValueError("contact IDs must be unique")
                
                seen_ids.add(contact["id"])

                if not isinstance(contact["name"], str):
                    raise ValueError("contact name must be a string")
                if not isinstance(contact["number"], str):
                    raise ValueError("Contact number must be a string")
                if not contact["name"].strip() or not contact["number"].strip():
                    raise ValueError("contact name or contact number cannot be empty")
            return contacts
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("your file contacts.json contains invalid JSON")
        raise

contacts = load_contacts()


app = FastAPI()

class Contact(BaseModel):
    
    name: str
    number: str
    @field_validator("name", "number")
    @classmethod
    def strip_whitespace(cls, value: str) -> str:
        cleaned_value = value.strip()
        if cleaned_value == "":
            raise ValueError ("name or number cannot be empty")
        return cleaned_value




def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def find_contact(contact_id: int):
    for contact in contacts:
        if contact_id == contact["id"]:
            return contact
    raise HTTPException(status_code=404, detail="Contact does not exist")


@app.get("/")
def home():
    return{"message": "Hello World"}


@app.get("/contacts")
def get_all_contacts():
    
    return contacts

@app.post("/contacts")
def add_contact(contact: Contact):
    highest_id = max((contact["id"] for contact in contacts), default = 0)
    new_id = highest_id + 1
    new_contact = {"id" : new_id,
        "name": contact.name, 
                    "number": contact.number}
    contacts.append(new_contact)
    save_contacts()
    return new_contact

@app.get("/contacts/{contact_id}")
def get_contact_id(contact_id: int):
    return find_contact(contact_id)



@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    existing_contact = find_contact(contact_id)
    existing_contact["name"] = contact.name
    existing_contact["number"] = contact.number
    save_contacts()
    return existing_contact
    

@app.delete("/contacts/{contact_id}", status_code=204)
def delete_contact(contact_id: int):
    existing_contact = find_contact(contact_id)
    contacts.remove(existing_contact)
    save_contacts()
    return
    

