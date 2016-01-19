from flask_wtf import Form
from wtforms import FileField
from wtforms import SelectField
from wtforms import TextAreaField
from wtforms import TextField
from wtforms import validators
from catalog.models import Catagory

class CreateCatalogItemForm(Form):
    name = TextField('name')
    description = TextAreaField('description')
    catagory_id = SelectField('catagory', coerce=int)
    image = FileField(
        'Image File',
        [validators.regexp(r'^[^/\\]\.jpg$')]
    )

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)
