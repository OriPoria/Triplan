import os
import csv
from contextlib import contextmanager

from src.models.user import User


class UsersDbHandler:

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), "tables", "users.csv")
        self.fields = ["username", "email", "password"]

    @contextmanager
    def _open_file_table(self):
        with open(self.file_path, mode="w", newline='') as f:
            csv_writer = csv.DictWriter(f, self.fields)
            yield csv_writer

    def create_user(self, user: User):
        with self._open_file_table() as csv_writer:
            csv_writer.writerow(user.model_dump())
