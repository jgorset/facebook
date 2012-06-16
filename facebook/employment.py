from datetime import datetime

import entity

from .page import Page

class Employment(entity.Entity):
    """Employment instances represent Facebook users's work history."""

    employer = None
    """A :class:`Page` instance describing the employer."""

    position = None
    """A :class:`Page` instance describing the position."""

    started_at = None
    """A :class:`datetime <datetime.datetime>` instance describing when the employment begun."""

    ended_at = None
    """A :class:`datetime <datetime.datetime>` instance describing when the employment ended, or ``None`` if it hasn't."""

    def __init__(self, employer, position, started_at, ended_at):
        self.employer = Page(**employer)
        self.position = Page(**position)
        self.started_at = datetime.strptime(started_at, '%Y-%m')

        if ended_at:
            self.ended_at = datetime.strptime(ended_at, '%Y-%m')
        else:
            self.ended_at = None

    @property
    def is_employed(self):
        """A boolean describing whether the user currently holds this position."""
        bool(self.ended_at)
