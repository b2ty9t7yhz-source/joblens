from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.services.demo_data import clear_sample_data, load_sample_data


def test_sample_data_is_idempotent_and_safe_to_clear():
    engine = create_engine("sqlite:///:memory:")
    testing_session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    with testing_session() as db:
        inserted, skipped, applications = load_sample_data(db)

        assert inserted == 6
        assert skipped == 0
        assert len(applications) == 6
        assert {item.status for item in applications} == {
            "Saved",
            "Applied",
            "OA",
            "Interview",
            "Offer",
            "No Response",
        }

        inserted, skipped, applications = load_sample_data(db)

        assert inserted == 0
        assert skipped == 6
        assert len(applications) == 6

        assert clear_sample_data(db) == 6
        assert clear_sample_data(db) == 0
