from app import app, db
from models import Venue, Artist, Show, Album, Song, Availability
from datetime import datetime

with app.app_context():
    # Clear existing data
    Song.query.delete()
    Album.query.delete()
    Availability.query.delete()
    Show.query.delete()
    Artist.query.delete()
    Venue.query.delete()
    db.session.commit()

    # Venues
    v1 = Venue(
        name='The Flying Monkey',
        city='Kansas City',
        state='MO',
        address='123 Tornado Alley',
        phone='816-555-0101',
        genres=['Jazz', 'Folk', 'Blues'],
        facebook_link='https://facebook.com/theflyingmonkey',
        website='https://theflyingmonkey.com',
        seeking_talent=True,
        seeking_description='Looking for local artists to perform weekends.',
        image_link='/static/img/venues/the_flying_monkey.jpg'
    )
    v2 = Venue(
        name='AIwood',
        city='Hollywood',
        state='CA',
        address='400 North Hollywood Blvd',
        phone='415-555-0202',
        genres=['Electronic', 'Hip-Hop', 'Funk'],
        facebook_link='https://facebook.com/aiwoodvenue',
        website='https://aiwood.com',
        seeking_talent=True,
        seeking_description='We welcome experimental and electronic artists.',
        image_link='/static/img/venues/AIwood.jpg'
    )
    v3 = Venue(
        name='Algorhythm and Blues',
        city='Austin',
        state='TX',
        address='88 Binary Lane',
        phone='512-555-0303',
        genres=['Blues', 'R&B', 'Soul'],
        facebook_link='https://facebook.com/algorhythmandblues',
        website='https://algorhythmandblues.com',
        seeking_talent=False,
        image_link='/static/img/venues/algorhythm_and_blues.jpg'
    )
    v4 = Venue(
        name='Blue Note',
        city='New York',
        state='NY',
        address='131 West 3rd Street',
        phone='212-555-0404',
        genres=['Jazz', 'Classical', 'Soul'],
        facebook_link='https://facebook.com/bluenote',
        website='https://bluenote.com',
        seeking_talent=True,
        seeking_description='Seeking jazz and classical artists for residencies.',
        image_link='/static/img/venues/blue_note.jpg'
    )
    v5 = Venue(
        name='Glenda Lounge',
        city='Chicago',
        state='IL',
        address='55 Emerald Ave',
        phone='312-555-0505',
        genres=['Pop', 'R&B', 'Soul'],
        facebook_link='https://facebook.com/glendalounge',
        website='https://glendalounge.com',
        seeking_talent=False,
        image_link='/static/img/venues/glenda_lounge.jpg'
    )
    v6 = Venue(
        name='Glitch Groove',
        city='Seattle',
        state='WA',
        address='9 Pixel Court',
        phone='206-555-0606',
        genres=['Electronic', 'Funk', 'Alternative'],
        facebook_link='https://facebook.com/glitchgroove',
        website='https://glitchgroove.com',
        seeking_talent=True,
        seeking_description='Open to avant-garde and experimental performers.',
        image_link='/static/img/venues/glitch_groove.jpg'
    )
    v7 = Venue(
        name='Machine Melody',
        city='Detroit',
        state='MI',
        address='1 Motor City Drive',
        phone='313-555-0707',
        genres=['Electronic', 'Hip-Hop', 'Funk'],
        facebook_link='https://facebook.com/machinemelody',
        website='https://machinemelody.com',
        seeking_talent=False,
        image_link='/static/img/venues/machine_melody.jpg'
    )
    v8 = Venue(
        name='Melody Club',
        city='Nashville',
        state='TN',
        address='22 Harmony Road',
        phone='615-555-0808',
        genres=['Country', 'Folk', 'Rock n Roll'],
        facebook_link='https://facebook.com/melodyclub',
        website='https://melodyclub.com',
        seeking_talent=True,
        seeking_description='Country and folk artists welcome.',
        image_link='/static/img/venues/melody_club.jpg'
    )
    v9 = Venue(
        name='Music Hall',
        city='Boston',
        state='MA',
        address='77 Symphony Square',
        phone='617-555-0909',
        genres=['Classical', 'Jazz', 'Musical Theatre'],
        facebook_link='https://facebook.com/musichall',
        website='https://musichall.com',
        seeking_talent=False,
        image_link='/static/img/venues/music_hall.jpg'
    )
    v10 = Venue(
        name='Prompt Plaza',
        city='Portland',
        state='OR',
        address='404 Not Found Street',
        phone='503-555-1010',
        genres=['Alternative', 'Indie', 'Folk'],
        facebook_link='https://facebook.com/promptplaza',
        website='https://promptplaza.com',
        seeking_talent=True,
        seeking_description='Indie and alternative acts wanted.',
        image_link='/static/img/venues/prompt_plaza.jpg'
    )
    v11 = Venue(
        name='The Echo',
        city='Los Angeles',
        state='CA',
        address='1822 Sunset Blvd',
        phone='323-555-1111',
        genres=['Rock n Roll', 'Alternative', 'Punk'],
        facebook_link='https://facebook.com/theecho',
        website='https://theecho.com',
        seeking_talent=False,
        image_link='/static/img/venues/the_echo.jpg'
    )
    v12 = Venue(
        name='Uptown Bayou',
        city='New Orleans',
        state='LA',
        address='300 Jazz Street',
        phone='504-555-1212',
        genres=['Jazz', 'Blues', 'Soul', 'Reggae'],
        facebook_link='https://facebook.com/uptownbayou',
        website='https://uptownbayou.com',
        seeking_talent=True,
        seeking_description='All genres welcome in the spirit of New Orleans.',
        image_link='/static/img/venues/uptown_bayou.jpg'
    )
    v13 = Venue(
        name='Vibe Square',
        city='Miami',
        state='FL',
        address='7 Ocean Drive',
        phone='305-555-1313',
        genres=['Pop', 'Electronic', 'Hip-Hop'],
        facebook_link='https://facebook.com/vibesquare',
        website='https://vibesquare.com',
        seeking_talent=False,
        image_link='/static/img/venues/vibe_square.jpg'
    )
    v14 = Venue(
        name='Voodoo Club',
        city='New Orleans',
        state='LA',
        address='13 Bayou Road',
        phone='504-555-1414',
        genres=['Blues', 'Jazz', 'Soul', 'R&B'],
        facebook_link='https://facebook.com/voodooclub',
        website='https://voodooclub.com',
        seeking_talent=True,
        seeking_description='Seeking soulful and bluesy performers.',
        image_link='/static/img/venues/voodoo_club.jpg'
    )

    # Artists
    a1 = Artist(
        name='Dorothy Red',
        city='Kansas City',
        state='MO',
        phone='816-555-2001',
        genres=['Folk', 'Country'],
        facebook_link='https://facebook.com/dorothyred',
        website='https://dorothyred.com',
        seeking_venue=True,
        seeking_description='Looking for weekend gigs in the Midwest.',
        image_link='/static/img/artists/dorothy_red.jpg'
    )
    a2 = Artist(
        name='Crimson Riot Sisters',
        city='Los Angeles',
        state='CA',
        phone='323-555-2002',
        genres=['Rock n Roll', 'Punk', 'Alternative'],
        facebook_link='https://facebook.com/crimsonriotsisters',
        website='https://crimsonriotsisters.com',
        seeking_venue=True,
        seeking_description='West coast punk band seeking venues.',
        image_link='/static/img/artists/crimson_riot_sisters.jpg'
    )
    a3 = Artist(
        name='Evan Blue',
        city='Chicago',
        state='IL',
        phone='312-555-2003',
        genres=['Blues', 'Soul', 'R&B'],
        facebook_link='https://facebook.com/evanblue',
        website='https://evanblue.com',
        seeking_venue=False,
        image_link='/static/img/artists/evan_blue.jpg'
    )
    a4 = Artist(
        name='Honky Tonk Ramblers',
        city='Nashville',
        state='TN',
        phone='615-555-2004',
        genres=['Country', 'Folk', 'Blues'],
        facebook_link='https://facebook.com/honkytonkramblers',
        website='https://honkytonkramblers.com',
        seeking_venue=True,
        seeking_description='Country band available for bookings.',
        image_link='/static/img/artists/honky_tonk_ramblers.jpg'
    )
    a5 = Artist(
        name='Lola Voss',
        city='New York',
        state='NY',
        phone='212-555-2005',
        genres=['Jazz', 'Soul', 'Pop'],
        facebook_link='https://facebook.com/lolavoss',
        website='https://lolavoss.com',
        seeking_venue=False,
        image_link='/static/img/artists/lola_voss.jpg'
    )
    a6 = Artist(
        name='Midnight Asphalt',
        city='Detroit',
        state='MI',
        phone='313-555-2006',
        genres=['Rock n Roll', 'Alternative', 'Heavy Metal'],
        facebook_link='https://facebook.com/midnightasphalt',
        website='https://midnightasphalt.com',
        seeking_venue=True,
        seeking_description='Hard rock band seeking mid-size venues.',
        image_link='/static/img/artists/midnight_asphalt.jpg'
    )
    a7 = Artist(
        name='Nina Fox',
        city='Seattle',
        state='WA',
        phone='206-555-2007',
        genres=['Electronic', 'Pop', 'Funk'],
        facebook_link='https://facebook.com/ninafox',
        website='https://ninafox.com',
        seeking_venue=False,
        image_link='/static/img/artists/nina_fox.png'
    )
    a8 = Artist(
        name='Noah Sterling',
        city='Austin',
        state='TX',
        phone='512-555-2008',
        genres=['Folk', 'Country', 'Alternative'],
        facebook_link='https://facebook.com/noahsterling',
        website='https://noahsterling.com',
        seeking_venue=True,
        seeking_description='Singer-songwriter looking for intimate venues.',
        image_link='/static/img/artists/noah_sterling.jpg'
    )
    a9 = Artist(
        name='Static Crows',
        city='Portland',
        state='OR',
        phone='503-555-2009',
        genres=['Alternative', 'Punk', 'Indie'],
        facebook_link='https://facebook.com/staticcrows',
        website='https://staticcrows.com',
        seeking_venue=False,
        image_link='/static/img/artists/static_crows.jpg'
    )
    a10 = Artist(
        name='Tessa Moon',
        city='New Orleans',
        state='LA',
        phone='504-555-2010',
        genres=['Jazz', 'Blues', 'Soul'],
        facebook_link='https://facebook.com/tessamoon',
        website='https://tessamoon.com',
        seeking_venue=True,
        seeking_description='Jazz vocalist available for bookings.',
        image_link='/static/img/artists/tessa_moon.jpg'
    )

    db.session.add_all([
        v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14,
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10
    ])
    db.session.commit()

    # Shows
    shows = [
        Show(venue_id=v1.id, artist_id=a1.id, start_time=datetime(2025, 3, 10, 20, 0)),
        Show(venue_id=v4.id, artist_id=a5.id, start_time=datetime(2025, 5, 14, 21, 0)),
        Show(venue_id=v3.id, artist_id=a3.id, start_time=datetime(2025, 6, 20, 19, 30)),
        Show(venue_id=v8.id, artist_id=a4.id, start_time=datetime(2025, 7, 4,  18, 0)),
        Show(venue_id=v11.id, artist_id=a2.id, start_time=datetime(2025, 8, 15, 22, 0)),
        Show(venue_id=v6.id, artist_id=a7.id, start_time=datetime(2026, 5, 1,  20, 0)),
        Show(venue_id=v2.id, artist_id=a7.id, start_time=datetime(2026, 6, 10, 21, 0)),
        Show(venue_id=v12.id, artist_id=a10.id, start_time=datetime(2026, 7, 20, 19, 0)),
        Show(venue_id=v14.id, artist_id=a10.id, start_time=datetime(2026, 8, 5, 20, 30)),
        Show(venue_id=v9.id, artist_id=a5.id, start_time=datetime(2026, 9, 12, 18, 0)),
        Show(venue_id=v7.id, artist_id=a6.id, start_time=datetime(2026, 10, 3, 21, 0)),
        Show(venue_id=v10.id, artist_id=a9.id, start_time=datetime(2026, 11, 22, 20, 0)),
    ]
    db.session.add_all(shows)
    db.session.commit()

    # Albums & Songs
    albums = [
        Album(artist_id=a1.id, title='Tornado Season', release_year=2023,
              image_link='/static/img/albums/tornado_season.jpg'),
        Album(artist_id=a2.id, title='Pink Static', release_year=2024,
              image_link='/static/img/albums/pink_static.jpg'),
        Album(artist_id=a3.id, title='Blue Hour', release_year=2022,
              image_link='/static/img/albums/blue_hour.jpg'),
        Album(artist_id=a4.id, title='Neon Barn', release_year=2023,
              image_link='/static/img/albums/neon_barn.jpg'),
        Album(artist_id=a5.id, title='Chrome Kiss', release_year=2024,
              image_link='/static/img/albums/chrome_kiss.jpg'),
        Album(artist_id=a6.id, title='Blacktop Backdrop', release_year=2023,
              image_link='/static/img/albums/blacktop_backdrop.jpg'),
        Album(artist_id=a7.id, title='Night Prowl', release_year=2024,
              image_link='/static/img/albums/night_prowl.jpg'),
        Album(artist_id=a8.id, title='Silver Lines', release_year=2022,
              image_link='/static/img/albums/silver_lines.jpg'),
        Album(artist_id=a9.id, title='Dead Frequency', release_year=2023,
              image_link='/static/img/albums/dead_frequency.jpg'),
        Album(artist_id=a10.id, title='First Light', release_year=2024,
              image_link='/static/img/albums/first_light.jpg'),
    ]
    db.session.add_all(albums)
    db.session.commit()

    songs = [
        # Tornado Season - Dorothy Red
        Song(album_id=albums[0].id, title='Dust and Rain', duration='3:42'),
        Song(album_id=albums[0].id, title='Yellow Brick Road', duration='4:10'),
        Song(album_id=albums[0].id, title='Ruby Slippers', duration='3:28'),
        Song(album_id=albums[0].id, title='Kansas Goodbye', duration='5:01'),
        # Pink Static - Crimson Riot Sisters
        Song(album_id=albums[1].id, title='Voltage', duration='2:58'),
        Song(album_id=albums[1].id, title='Riot Bloom', duration='3:15'),
        Song(album_id=albums[1].id, title='Neon Fist', duration='3:44'),
        Song(album_id=albums[1].id, title='Crimson Wave', duration='4:02'),
        # Blue Hour - Evan Blue
        Song(album_id=albums[2].id, title='Midnight Confession', duration='5:12'),
        Song(album_id=albums[2].id, title='River of Smoke', duration='4:33'),
        Song(album_id=albums[2].id, title='Blue Hour', duration='6:01'),
        Song(album_id=albums[2].id, title='Last Call', duration='4:48'),
        # Neon Barn - Honky Tonk Ramblers
        Song(album_id=albums[3].id, title='Two-Step Tonight', duration='3:22'),
        Song(album_id=albums[3].id, title='Neon Barn Dance', duration='4:05'),
        Song(album_id=albums[3].id, title='Whiskey Wagon', duration='3:51'),
        Song(album_id=albums[3].id, title='Dusty Boots', duration='3:18'),
        # Chrome Kiss - Lola Voss
        Song(album_id=albums[4].id, title='Silver Tongue', duration='4:22'),
        Song(album_id=albums[4].id, title='Chrome Kiss', duration='5:10'),
        Song(album_id=albums[4].id, title='Velvet Underground', duration='3:55'),
        Song(album_id=albums[4].id, title='Late Night Jazz', duration='6:30'),
        # Blacktop Backdrop - Midnight Asphalt
        Song(album_id=albums[5].id, title='Engine Roar', duration='4:01'),
        Song(album_id=albums[5].id, title='Blacktop Burn', duration='3:47'),
        Song(album_id=albums[5].id, title='Steel and Smoke', duration='5:22'),
        Song(album_id=albums[5].id, title='Night Rider', duration='4:15'),
        # Night Prowl - Nina Fox
        Song(album_id=albums[6].id, title='Shadows', duration='3:30'),
        Song(album_id=albums[6].id, title='Night Prowl', duration='4:12'),
        Song(album_id=albums[6].id, title='Electric Dreams', duration='3:58'),
        Song(album_id=albums[6].id, title='Fox Run', duration='4:44'),
        # Silver Lines - Noah Sterling
        Song(album_id=albums[7].id, title='Open Road', duration='4:20'),
        Song(album_id=albums[7].id, title='Silver Lines', duration='3:55'),
        Song(album_id=albums[7].id, title='Porch Light', duration='5:03'),
        Song(album_id=albums[7].id, title='Wander On', duration='4:11'),
        # Dead Frequency - Static Crows
        Song(album_id=albums[8].id, title='Signal Lost', duration='3:38'),
        Song(album_id=albums[8].id, title='Dead Air', duration='4:22'),
        Song(album_id=albums[8].id, title='Static Rain', duration='3:15'),
        Song(album_id=albums[8].id, title='Crow Call', duration='5:07'),
        # First Light - Tessa Moon
        Song(album_id=albums[9].id, title='Dawn Serenade', duration='5:45'),
        Song(album_id=albums[9].id, title='First Light', duration='4:28'),
        Song(album_id=albums[9].id, title='Moon River Blues', duration='6:12'),
        Song(album_id=albums[9].id, title='Bayou Lullaby', duration='5:33'),
    ]
    db.session.add_all(songs)
    db.session.commit()

    print('Database seeded successfully.')
