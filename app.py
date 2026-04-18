#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import dateutil.parser
from datetime import datetime
import babel
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_moment import Moment
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from sqlalchemy import or_
from models import db, Venue, Artist, Show, Availability, Album, Song
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  recent_venues = Venue.query.order_by(Venue.id.desc()).limit(10).all()
  recent_artists = Artist.query.order_by(Artist.id.desc()).limit(10).all()
  return render_template('pages/home.html', recent_venues=recent_venues, recent_artists=recent_artists)


#  Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  data = []
  city_states = Venue.query.with_entities(Venue.city, Venue.state).distinct().order_by(Venue.state, Venue.city).all()
  for city, state in city_states:
    city_venues = Venue.query.filter_by(city=city, state=state).all()
    data.append({
      'city': city,
      'state': state,
      'venues': [{
        'id': v.id,
        'name': v.name,
        'image_link': v.image_link,
        'num_upcoming_shows': Show.query.filter(
          Show.venue_id == v.id,
          Show.start_time > datetime.now()
        ).count()
      } for v in city_venues]
    })
  return render_template('pages/venues.html', areas=data)

@app.route('/venues/search', methods=['POST'])
def search_venues():
  search_term = request.form.get('search_term', '')
  if ',' in search_term:
    city, state = [p.strip() for p in search_term.split(',', 1)]
    venues = Venue.query.filter(Venue.city.ilike(f'%{city}%'), Venue.state.ilike(f'%{state}%')).all()
  else:
    venues = Venue.query.filter(
      or_(Venue.name.ilike(f'%{search_term}%'), Venue.city.ilike(f'%{search_term}%'), Venue.state.ilike(f'%{search_term}%'))
    ).all()
  response = {
    'count': len(venues),
    'data': [{
      'id': v.id,
      'name': v.name,
      'city': v.city,
      'state': v.state,
      'num_upcoming_shows': Show.query.filter(
        Show.venue_id == v.id,
        Show.start_time > datetime.now()
      ).count()
    } for v in venues]
  }
  return render_template('pages/search_venues.html', results=response, search_term=search_term)

@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  venue = Venue.query.get_or_404(venue_id)
  now = datetime.now()
  past_shows_query = db.session.query(Show).join(Artist).filter(
    Show.venue_id == venue_id,
    Show.start_time <= now
  ).all()
  upcoming_shows_query = db.session.query(Show).join(Artist).filter(
    Show.venue_id == venue_id,
    Show.start_time > now
  ).all()
  past_shows = [{
    'artist_id': s.artist_id,
    'artist_name': s.artist.name,
    'artist_image_link': s.artist.image_link,
    'start_time': str(s.start_time)
  } for s in past_shows_query]
  upcoming_shows = [{
    'artist_id': s.artist_id,
    'artist_name': s.artist.name,
    'artist_image_link': s.artist.image_link,
    'start_time': str(s.start_time)
  } for s in upcoming_shows_query]
  data = {
    'id': venue.id,
    'name': venue.name,
    'genres': venue.genres,
    'address': venue.address,
    'city': venue.city,
    'state': venue.state,
    'phone': venue.phone,
    'website': venue.website,
    'facebook_link': venue.facebook_link,
    'seeking_talent': venue.seeking_talent,
    'seeking_description': venue.seeking_description,
    'image_link': venue.image_link,
    'past_shows': past_shows,
    'upcoming_shows': upcoming_shows,
    'past_shows_count': len(past_shows),
    'upcoming_shows_count': len(upcoming_shows)
  }
  return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------

@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  form = VenueForm(request.form)
  try:
    venue = Venue(
      name=form.name.data,
      city=form.city.data,
      state=form.state.data,
      address=form.address.data,
      phone=form.phone.data,
      genres=form.genres.data,
      image_link=form.image_link.data,
      facebook_link=form.facebook_link.data,
      website=form.website_link.data,
      seeking_talent=form.seeking_talent.data,
      seeking_description=form.seeking_description.data
    )
    db.session.add(venue)
    db.session.commit()
    flash('Venue ' + form.name.data + ' was successfully listed!')
  except:
    db.session.rollback()
    flash('An error occurred. Venue ' + form.name.data + ' could not be listed.')
  finally:
    db.session.close()
  return redirect(url_for('index'))

@app.route('/venues/<int:venue_id>/delete', methods=['POST'])
def delete_venue(venue_id):
  try:
    venue = Venue.query.get_or_404(venue_id)
    name = venue.name
    db.session.delete(venue)
    db.session.commit()
    flash('Venue ' + name + ' was successfully deleted.')
  except:
    db.session.rollback()
    flash('An error occurred. Venue could not be deleted.')
  finally:
    db.session.close()
  return redirect(url_for('index'))


@app.route('/artists/<int:artist_id>/delete', methods=['POST'])
def delete_artist(artist_id):
  try:
    artist = Artist.query.get_or_404(artist_id)
    name = artist.name
    db.session.delete(artist)
    db.session.commit()
    flash('Artist ' + name + ' was successfully deleted.')
  except:
    db.session.rollback()
    flash('An error occurred. Artist could not be deleted.')
  finally:
    db.session.close()
  return redirect(url_for('index'))

#  Artists
#  ----------------------------------------------------------------
@app.route('/artists')
def artists():
  data = [{'id': a.id, 'name': a.name, 'image_link': a.image_link, 'city': a.city, 'state': a.state} for a in Artist.query.order_by(Artist.name).all()]
  return render_template('pages/artists.html', artists=data)

@app.route('/artists/search', methods=['POST'])
def search_artists():
  search_term = request.form.get('search_term', '')
  if ',' in search_term:
    city, state = [p.strip() for p in search_term.split(',', 1)]
    artists = Artist.query.filter(Artist.city.ilike(f'%{city}%'), Artist.state.ilike(f'%{state}%')).all()
  else:
    artists = Artist.query.filter(
      or_(Artist.name.ilike(f'%{search_term}%'), Artist.city.ilike(f'%{search_term}%'), Artist.state.ilike(f'%{search_term}%'))
    ).all()
  response = {
    'count': len(artists),
    'data': [{
      'id': a.id,
      'name': a.name,
      'city': a.city,
      'state': a.state,
      'num_upcoming_shows': Show.query.filter(
        Show.artist_id == a.id,
        Show.start_time > datetime.now()
      ).count()
    } for a in artists]
  }
  return render_template('pages/search_artists.html', results=response, search_term=search_term)

@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  artist = Artist.query.get_or_404(artist_id)
  now = datetime.now()
  past_shows_query = db.session.query(Show).join(Venue).filter(
    Show.artist_id == artist_id,
    Show.start_time <= now
  ).all()
  upcoming_shows_query = db.session.query(Show).join(Venue).filter(
    Show.artist_id == artist_id,
    Show.start_time > now
  ).all()
  past_shows = [{
    'venue_id': s.venue_id,
    'venue_name': s.venue.name,
    'venue_image_link': s.venue.image_link,
    'start_time': str(s.start_time)
  } for s in past_shows_query]
  upcoming_shows = [{
    'venue_id': s.venue_id,
    'venue_name': s.venue.name,
    'venue_image_link': s.venue.image_link,
    'start_time': str(s.start_time)
  } for s in upcoming_shows_query]
  data = {
    'id': artist.id,
    'name': artist.name,
    'genres': artist.genres,
    'city': artist.city,
    'state': artist.state,
    'phone': artist.phone,
    'website': artist.website,
    'facebook_link': artist.facebook_link,
    'seeking_venue': artist.seeking_venue,
    'seeking_description': artist.seeking_description,
    'image_link': artist.image_link,
    'past_shows': past_shows,
    'upcoming_shows': upcoming_shows,
    'past_shows_count': len(past_shows),
    'upcoming_shows_count': len(upcoming_shows),
    'albums': artist.albums
  }
  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  artist = Artist.query.get_or_404(artist_id)
  form = ArtistForm(obj=artist)
  form.website_link.data = artist.website
  return render_template('forms/edit_artist.html', form=form, artist=artist)

@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  form = ArtistForm(request.form)
  artist = Artist.query.get_or_404(artist_id)
  try:
    artist.name = form.name.data
    artist.city = form.city.data
    artist.state = form.state.data
    artist.phone = form.phone.data
    artist.genres = form.genres.data
    artist.image_link = form.image_link.data
    artist.facebook_link = form.facebook_link.data
    artist.website = form.website_link.data
    artist.seeking_venue = form.seeking_venue.data
    artist.seeking_description = form.seeking_description.data
    db.session.commit()
    flash('Artist ' + form.name.data + ' was successfully updated!')
  except:
    db.session.rollback()
    flash('An error occurred. Artist ' + form.name.data + ' could not be updated.')
  finally:
    db.session.close()
  return redirect(url_for('show_artist', artist_id=artist_id))

@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  venue = Venue.query.get_or_404(venue_id)
  form = VenueForm(obj=venue)
  form.website_link.data = venue.website
  return render_template('forms/edit_venue.html', form=form, venue=venue)

@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  form = VenueForm(request.form)
  venue = Venue.query.get_or_404(venue_id)
  try:
    venue.name = form.name.data
    venue.city = form.city.data
    venue.state = form.state.data
    venue.address = form.address.data
    venue.phone = form.phone.data
    venue.genres = form.genres.data
    venue.image_link = form.image_link.data
    venue.facebook_link = form.facebook_link.data
    venue.website = form.website_link.data
    venue.seeking_talent = form.seeking_talent.data
    venue.seeking_description = form.seeking_description.data
    db.session.commit()
    flash('Venue ' + form.name.data + ' was successfully updated!')
  except:
    db.session.rollback()
    flash('An error occurred. Venue ' + form.name.data + ' could not be updated.')
  finally:
    db.session.close()
  return redirect(url_for('show_venue', venue_id=venue_id))

#  Availability
#  ----------------------------------------------------------------

@app.route('/artists/<int:artist_id>/availability')
def manage_availability(artist_id):
  artist = Artist.query.get_or_404(artist_id)
  return render_template('pages/availability.html', artist=artist)

@app.route('/artists/<int:artist_id>/availability', methods=['POST'])
def add_availability(artist_id):
  artist = Artist.query.get_or_404(artist_id)
  try:
    availability = Availability(
      artist_id=artist_id,
      start_time=datetime.strptime(request.form['start_time'], '%Y-%m-%dT%H:%M'),
      end_time=datetime.strptime(request.form['end_time'], '%Y-%m-%dT%H:%M')
    )
    db.session.add(availability)
    db.session.commit()
    flash('Availability window added.')
  except:
    db.session.rollback()
    flash('An error occurred. Could not add availability.')
  finally:
    db.session.close()
  return redirect(url_for('manage_availability', artist_id=artist_id))

@app.route('/artists/<int:artist_id>/availability/<int:availability_id>/delete', methods=['POST'])
def delete_availability(artist_id, availability_id):
  availability = Availability.query.get_or_404(availability_id)
  try:
    db.session.delete(availability)
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('manage_availability', artist_id=artist_id))

#  Albums & Songs
#  ----------------------------------------------------------------

@app.route('/artists/<int:artist_id>/albums')
def manage_albums(artist_id):
  artist = Artist.query.get_or_404(artist_id)
  return render_template('pages/albums.html', artist=artist)

@app.route('/artists/<int:artist_id>/albums', methods=['POST'])
def add_album(artist_id):
  Artist.query.get_or_404(artist_id)
  try:
    album = Album(
      artist_id=artist_id,
      title=request.form['title'],
      release_year=request.form.get('release_year') or None,
      image_link=request.form.get('image_link') or None
    )
    db.session.add(album)
    db.session.commit()
    flash('Album "' + album.title + '" added.')
  except:
    db.session.rollback()
    flash('An error occurred. Could not add album.')
  finally:
    db.session.close()
  return redirect(url_for('manage_albums', artist_id=artist_id))

@app.route('/artists/<int:artist_id>/albums/<int:album_id>/delete', methods=['POST'])
def delete_album(artist_id, album_id):
  album = Album.query.get_or_404(album_id)
  try:
    db.session.delete(album)
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('manage_albums', artist_id=artist_id))

@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs', methods=['POST'])
def add_song(artist_id, album_id):
  Album.query.get_or_404(album_id)
  try:
    song = Song(
      album_id=album_id,
      title=request.form['title'],
      duration=request.form.get('duration') or None
    )
    db.session.add(song)
    db.session.commit()
    flash('Song "' + song.title + '" added.')
  except:
    db.session.rollback()
    flash('An error occurred. Could not add song.')
  finally:
    db.session.close()
  return redirect(url_for('manage_albums', artist_id=artist_id))

@app.route('/artists/<int:artist_id>/albums/<int:album_id>/songs/<int:song_id>/delete', methods=['POST'])
def delete_song(artist_id, album_id, song_id):
  song = Song.query.get_or_404(song_id)
  try:
    db.session.delete(song)
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('manage_albums', artist_id=artist_id))

#  Create Artist
#  ----------------------------------------------------------------

@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form = ArtistForm(request.form)
  try:
    artist = Artist(
      name=form.name.data,
      city=form.city.data,
      state=form.state.data,
      phone=form.phone.data,
      genres=form.genres.data,
      image_link=form.image_link.data,
      facebook_link=form.facebook_link.data,
      website=form.website_link.data,
      seeking_venue=form.seeking_venue.data,
      seeking_description=form.seeking_description.data
    )
    db.session.add(artist)
    db.session.commit()
    flash('Artist ' + form.name.data + ' was successfully listed!')
  except:
    db.session.rollback()
    flash('An error occurred. Artist ' + form.name.data + ' could not be listed.')
  finally:
    db.session.close()
  return redirect(url_for('index'))


#  Shows
#  ----------------------------------------------------------------

@app.route('/shows')
def shows():
  data = [{
    'id': s.id,
    'venue_id': s.venue_id,
    'venue_name': s.venue.name,
    'artist_id': s.artist_id,
    'artist_name': s.artist.name,
    'artist_image_link': s.artist.image_link,
    'start_time': str(s.start_time)
  } for s in Show.query.all()]
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/<int:show_id>/delete', methods=['POST'])
def delete_show(show_id):
  try:
    show = Show.query.get_or_404(show_id)
    db.session.delete(show)
    db.session.commit()
    flash('Show was successfully deleted.')
  except:
    db.session.rollback()
    flash('An error occurred. Show could not be deleted.')
  finally:
    db.session.close()
  return redirect(url_for('shows'))

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  form = ShowForm(request.form)
  artist = Artist.query.get(form.artist_id.data)
  if artist and artist.availability:
    show_time = form.start_time.data
    now = datetime.now()
    future_windows = [a for a in artist.availability if a.end_time >= now]
    if future_windows:
      available = any(a.start_time <= show_time <= a.end_time for a in future_windows)
      if not available:
        flash('This artist is not available at that time. Please check their availability.')
        return redirect(url_for('create_shows'))
  try:
    show = Show(
      venue_id=form.venue_id.data,
      artist_id=form.artist_id.data,
      start_time=form.start_time.data
    )
    db.session.add(show)
    db.session.commit()
    flash('Show was successfully listed!')
  except:
    db.session.rollback()
    flash('An error occurred. Show could not be listed.')
  finally:
    db.session.close()
  return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
