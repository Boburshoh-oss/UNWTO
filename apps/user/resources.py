# resources.py
from import_export import resources, fields
from import_export.fields import Field, widgets
from .models import User
from apps.forum.models import Forum

class UserResource(resources.ModelResource):
    forum_type = Field(
        attribute='forum_type',  
        column_name='forum_type',
        widget=widgets.ManyToManyWidget(Forum, field='title', separator='|')
    )
    organization = Field(
        attribute='organization__title',  # `title` is the field on the `Organization` model
        column_name='organization'
    )
    invitation_id = Field(
        attribute='invitation_id__code',  # Replace `some_field` with the relevant field on the `Invitation` model
        column_name='invitation_id'
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'country', 'passport', 'expire_date', 'access_id', 'forum_type', 'organization', 'invitation_id')
