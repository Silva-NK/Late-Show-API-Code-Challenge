from datetime import date

from models.extensions import db

from app import create_app

from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

app = create_app()

with app.app_context():
    print("Clearing tables...")

    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    # User.query.delete()

    db.session.commit()

    print("Seeding data...")

    # user = User(username="janeysmith")
    # user.password = "password123"
    # db.session.add(user)

    g1 = Guest(name="Zendaya", occupation="Actor")
    g2 = Guest(name="Pedro Pascal", occupation="Actor")
    g3 = Guest(name="Amal Clooney", occupation="Attorney")
    g4 = Guest(name="Lana del Rey", occupation="Musician")
    g5 = Guest(name="Trevor Noah", occupation="Comedian")

    db.session.add_all([g1, g2, g3, g4, g5])

    ep1 = Episode(number=101, date=date(2023, 10, 1))
    ep2 = Episode(number=102, date=date(2023, 10, 2))
    ep3 = Episode(number=103, date=date(2023, 10, 3))
    ep4 = Episode(number=104, date=date(2023, 10, 4))
    ep5 = Episode(number=105, date=date(2023, 10, 5))

    db.session.add_all([ep1, ep2, ep3, ep4, ep5])
    db.session.commit()

    app1 = Appearance(rating=5, guest_id=g1.id, episode_id=ep1.id)
    app2 = Appearance(rating=4, guest_id=g2.id, episode_id=ep1.id)
    app3 = Appearance(rating=3, guest_id=g3.id, episode_id=ep2.id)
    app4 = Appearance(rating=5, guest_id=g4.id, episode_id=ep2.id)
    app5 = Appearance(rating=4, guest_id=g5.id, episode_id=ep3.id)
    app6 = Appearance(rating=2, guest_id=g1.id, episode_id=ep4.id)
    app7 = Appearance(rating=5, guest_id=g2.id, episode_id=ep5.id)

    db.session.add_all([app1, app2, app3, app4, app5, app6, app7])
    db.session.commit()

    print("Database seeded successfully.")