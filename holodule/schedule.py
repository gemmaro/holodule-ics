from logging import getLogger
from pathlib import Path
from typing import Set

from ics import Calendar
from ics.grammar.parse import ContentLine

import holodule.parser

log = getLogger(__name__)


class Schedule():
    def parse(name, html_source):
        parser = holodule.parser.Parser()
        parser.feed(html_source)
        return Schedule(name, parser.events)

    def __init__(self, name: str, events) -> None:
        self.name = name
        self.events = events

    @property
    def video_ids(self) -> Set[str]:
        return {e.site.id for e in self.events if e.site.id}

    @property
    def ical_calendar(self) -> Calendar:
        cal = Calendar(
            events=[e.ical_event() for e in self.events if e.show],
            creator="holodule-ical")
        cal.extra.append(ContentLine(
            "X-WR-CALNAME", value=f"Holodule - {self.name}"))
        cal.extra.append(ContentLine("X-WR-TIMEZONE", value="Asia/Tokyo"))
        return cal

    def assign_youtube(self, yt_meta: dict) -> None:
        for event in self.events:
            event.assign(yt_meta.get(event.site.id))

    def dump(self, save_dir: str) -> None:
        path = Path(save_dir)
        path.mkdir(parents=True, exist_ok=True)
        path = path/f"holodule-{self.name}.ics"
        with path.open('w', encoding="utf-8") as f:
            f.writelines(self.ical_calendar)
