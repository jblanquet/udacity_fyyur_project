from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, IntegerField
from wtforms.validators import DataRequired, NumberRange, URL, Regexp, Optional

STATES = [
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('DC', 'DC'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
]

GENRES = [
    ('Alternative', 'Alternative'),
    ('Blues', 'Blues'),
    ('Classical', 'Classical'),
    ('Country', 'Country'),
    ('Electronic', 'Electronic'),
    ('Folk', 'Folk'),
    ('Funk', 'Funk'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Heavy Metal', 'Heavy Metal'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Musical Theatre', 'Musical Theatre'),
    ('Pop', 'Pop'),
    ('Punk', 'Punk'),
    ('R&B', 'R&B'),
    ('Reggae', 'Reggae'),
    ('Rock n Roll', 'Rock n Roll'),
    ('Soul', 'Soul'),
    ('Other', 'Other'),
]


class ShowForm(Form):
    artist_id = IntegerField(
        'artist_id',
        validators=[DataRequired(), NumberRange(min=1, message='Artist ID must be a positive number')]
    )
    venue_id = IntegerField(
        'venue_id',
        validators=[DataRequired(), NumberRange(min=1, message='Venue ID must be a positive number')]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default=datetime.today,
        format='%Y-%m-%d %H:%M'
    )


class SharedForm(Form):
    image_link = StringField(
        'image_link'
    )
    facebook_link = StringField(
        'facebook_link', validators=[Optional(), URL()]
    )
    website_link = StringField(
        'website_link', validators=[Optional(), URL()]
    )
    seeking_description = StringField(
        'seeking_description'
    )


class VenueForm(SharedForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=STATES
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[Optional(), Regexp(r'^\d{3}-\d{3}-\d{4}$', message='Phone must be in format: 555-555-5555')]
    )
    genres = SelectMultipleField(
        'genres',
        validators=[DataRequired()],
        choices=GENRES
    )
    seeking_talent = BooleanField('seeking_talent')


class ArtistForm(SharedForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=STATES
    )
    phone = StringField(
        'phone', validators=[Optional(), Regexp(r'^\d{3}-\d{3}-\d{4}$', message='Phone must be in format: 555-555-5555')]
    )
    genres = SelectMultipleField(
        'genres',
        validators=[DataRequired()],
        choices=GENRES
    )
    seeking_venue = BooleanField('seeking_venue')
