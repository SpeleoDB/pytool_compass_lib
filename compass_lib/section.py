#!/usr/bin/env python

from dataclasses import dataclass
from datetime import date

from compass_lib.shot import SurveyShot


@dataclass
class SurveySection:
    cave_name: str
    survey_name: str
    date: date
    comment: str
    surveyors: list[str]
    declination: float
    format: str
    correction: tuple[float, float, float]
    shots: list[SurveyShot]
