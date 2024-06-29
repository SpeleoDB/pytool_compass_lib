#!/usr/bin/env python

import json
import unittest
from pathlib import Path

from parameterized import parameterized_class

from compass_lib.parser import CompassParser


@parameterized_class(
    ("filepath"),
    [
        ("./tests/artifacts/random.dat",),
        ("./tests/artifacts/fulford.dat",)
    ]
)
class ReadCompassDATFileTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._file = Path(cls.filepath)
        if not cls._file.exists():
            raise FileNotFoundError(f"File not found: `{cls._file}`")

    def setUp(self) -> None:
        self._parser = CompassParser(self._file)

    def test_export_to_json(self):
        if self._parser is None:
            raise ValueError("the Compass Parser has not been setup.")

        json_str = self._parser.to_json()

        with Path(str(self._file)[:-3] + "json").open() as f:
            json_target = json.load(f)

        assert json.loads(json_str) == json_target


if __name__ == "__main__":
    unittest.main()
