from ..extensions import db

#Chapters
location_chapters = db.Table('location_chapters',
    db.Column('chapter_id', db.Integer, db.ForeignKey('chapter.id'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True)
)

creature_chapters = db.Table('creature_chapters',
    db.Column('chapter_id', db.Integer, db.ForeignKey('chapter.id'), primary_key=True),
    db.Column('creature_id', db.Integer, db.ForeignKey('creature.id'), primary_key=True)
)

event_chapters = db.Table('event_chapters',
    db.Column('chapter_id', db.Integer, db.ForeignKey('chapter.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

system_chapters = db.Table('system_chapters',
    db.Column('chapter_id', db.Integer, db.ForeignKey('chapter.id'), primary_key=True),
    db.Column('system_id', db.Integer, db.ForeignKey('system.id'), primary_key=True)
)

faction_chapters = db.Table('faction_chapters',
    db.Column('chapter_id', db.Integer, db.ForeignKey('chapter.id'), primary_key=True),
    db.Column('faction_id', db.Integer, db.ForeignKey('faction.id'), primary_key=True)
)

#Creatures
creature_events = db.Table('creature_events',
    db.Column('creature_id', db.Integer, db.ForeignKey('creature.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

creature_factions = db.Table('creature_factions',
    db.Column('creature_id', db.Integer, db.ForeignKey('creature.id'), primary_key=True),
    db.Column('faction_id', db.Integer, db.ForeignKey('faction.id'), primary_key=True)
)

creature_locations = db.Table('creature_locations',
    db.Column('creature_id', db.Integer, db.ForeignKey('creature.id'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True)
)

#Event
event_characters = db.Table('event_characters',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True)
)

event_creatures = db.Table('event_creatures',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('creature_id', db.Integer, db.ForeignKey('creature.id'), primary_key=True)
)

#Faction
faction_characters = db.Table('faction_characters',
    db.Column('faction_id', db.Integer, db.ForeignKey('faction.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True)
)

faction_events = db.Table('faction_events',
    db.Column('faction_id', db.Integer, db.ForeignKey('faction.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

#Item
item_locations = db.Table('item_locations',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True)
)

item_events = db.Table('item_events',
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

#Location
location_residents = db.Table('location_residents',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True),
)

location_factions = db.Table('location_factions',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('faction_id', db.Integer, db.ForeignKey('faction.id'), primary_key=True),
)

location_events = db.Table('location_events',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
)

location_plots = db.Table('location_plots',
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
    db.Column('plot_id', db.Integer, db.ForeignKey('plot.id'), primary_key=True),
)

#Plot
plot_locations = db.Table('plot_locations',
    db.Column('plot_id', db.Integer, db.ForeignKey('plot.id'), primary_key=True),
    db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True)
)

plot_events = db.Table('plot_events',
    db.Column('plot_id', db.Integer, db.ForeignKey('plot.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
)

plot_characters = db.Table('plot_characters',
    db.Column('plot_id', db.Integer, db.ForeignKey('plot.id'), primary_key=True),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'), primary_key=True)
)

#System
system_worlds = db.Table('system_worlds',
    db.Column('system_id', db.Integer, db.ForeignKey('system.id'), primary_key=True),
    db.Column('world_id', db.Integer, db.ForeignKey('world.id'), primary_key=True)
)