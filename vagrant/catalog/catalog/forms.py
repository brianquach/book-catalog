from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import TextField
from wtforms import validators
from catalog.models import Catagory

class CreateCatalogItemForm(Form):
    name = TextField('Name', validators=[validators.DataRequired()])
    author = TextField('Author', validators=[validators.DataRequired()])
    description = TextAreaField('Description')
    catagory_id = SelectField(
        'Catagory',
        coerce=int,
        validators=[validators.DataRequired()]
    )
    image = FileField('Image File')

class EditCatalogItemForm(Form):
    name = TextField('Name', validators=[validators.DataRequired()])
    author = TextField('Author', validators=[validators.DataRequired()])
    description = TextAreaField('Description')
    catagory_id = SelectField(
        'Catagory',
        coerce=int,
        validators=[validators.DataRequired()]
    )
    image = FileField('New Image File')