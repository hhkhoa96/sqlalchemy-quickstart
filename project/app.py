from sqlmodel import Session

from .database import engine, create_db_and_tables
from .team_models import Team
from .hero_model import Hero

def create_heroes():  
    with Session(engine) as session:
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret’s Bar")

        hero_deadpond = Hero(
            name="Deadpond", secret_name="Dive Wilson", team=team_z_force
        )
        session.add(hero_deadpond)
        session.commit()

        session.refresh(hero_deadpond)

        print("Created hero:", hero_deadpond)
        print("Hero's team:", hero_deadpond.team)


    
def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.age > 30)
        results = session.exec(statement)
        for hero in results:
            print(hero)


def main():  
    create_db_and_tables()
    create_heroes()

if __name__ == "__main__":  
    main()  