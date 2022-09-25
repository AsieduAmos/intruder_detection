from datetime import datetime
import firebase_admin
from firebase_admin import credentials, storage, firestore

cred = credentials.Certificate("C:\Users\Qweku\Downloads\ilarm-c4a28-firebase-adminsdk-fjx8i-6ffd0a77b4.json")
firebase_admin.initialize_app(cred, {"storageBucket": "ilarm-c4a28-firebase-adminsdk-fjx8i-6ffd0a77b4.json"})
db = firestore.client()

def upload_file(fileName: str):
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    return blob

def store_data_in_database(blob:storage.storage.Blob ):
    db.collection(u"image_uploads").document(u'one').set(data)
    doc_ref = db.collection("users").document("alovelace")
    doc_ref.set({"filepath":blob.public_url, "last_edit": datetime.now(),})