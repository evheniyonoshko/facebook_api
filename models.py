from config import DB_NAME, DB_USER, DB_PASS
from peewee import PostgresqlDatabase, Model, IntegerField, CharField, DateTimeField


db = PostgresqlDatabase(DB_NAME, user=DB_USER, password=DB_PASS)


class BaseModel(Model):
    class Meta:
        database = db


class Posts(BaseModel):
    post_id = CharField()
    message = CharField()
    last_update = DateTimeField()
    count_likes = IntegerField()

    class Meta:
        # order by created date descending
        ordering = ('-last_update',)
