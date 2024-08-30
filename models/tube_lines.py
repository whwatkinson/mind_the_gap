from neomodel import StringProperty, StructuredNode

from models.station import Station


class Piccadilly(StructuredNode, Station):
    line_name = StringProperty(default="Piccadilly")
    line_colour = StringProperty(default="#1C1865")


if __name__ == "__main__":
    from neomodel import config, db
    from settings.environment_variables import NEO4J_DATABASE_URL

    config.DATABASE_URL = NEO4J_DATABASE_URL
    db.cypher_query("MATCH (n) DETACH DELETE n;")

    p = Piccadilly(
        station_name="Earls Court",
        end_of_line=False,
        location="[51.490616 0.195848]",
        line_identifier="PCL",
        wiggle_ranking=6.0,
    ).save()
