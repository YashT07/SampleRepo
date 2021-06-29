from flask_wtf import FlaskForm
from wtforms import StringField, TextField, PasswordField, SubmitField

class Clinic(FlaskForm):
    
    success = SubmitField("Submit")
    autocomp = TextField('Enter the Patient Name', id='patient_autocomplete')


    # username = StringField("Username")
    # suggestion = StringField("Suggestion")
    # password = PasswordField("Password")
    # submit = SubmitField("Login")
    # reject = SubmitField("Cancel")

    # keys = SubmitField("Show Public and Private keys")
    
    # encryptTextField1 = StringField("Public Keys value 1(e)")
    # encryptTextField2 = StringField("Public Keys value 2(n)")
    # encryptTextField3 = StringField("Enter message to be encrypted")
    # encryptButton = SubmitField("Encrypt")

    # decryptTextField1 = StringField("Private Keys value 1(d)")
    # decryptTextField2 = StringField("Private Keys value 2(n)")
    # decryptTextField3 = StringField("Enter message to be decrypted")

    # decryptButton = SubmitField("Decrypt")