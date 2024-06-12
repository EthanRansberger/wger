#  This file is part of wger Workout Manager <https://github.com/wger-project>.
#  Copyright (C) wger Team
#
#  wger Workout Manager is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  wger Workout Manager is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Standard Library
import datetime
from dataclasses import (
    dataclass,
    field,
)
from decimal import Decimal
from typing import (
    Any,
    List,
)


@dataclass
class SetConfigData:
    exercise: int

    weight: Decimal | int | None
    reps: Decimal | int | None
    rir: Decimal | int | None
    rest: Decimal | int | None

    sets: Decimal | int = 1
    weight_unit: int | None = 1
    reps_unit: int | None = 1
    weight_rounding: Decimal | int | None = 1.25
    reps_rounding: Decimal | int | None = 1

    type: str = 'normal'
    slot_config_id: int | None = None


@dataclass
class SetExerciseData:
    config: Any  # 'SlotConfig'
    data: SetConfigData

    @property
    def exercise(self):
        return self.config.exercise


@dataclass
class SlotData:
    comment: str
    exercises: List[int] = field(default_factory=list)
    sets: List[SetConfigData] = field(default_factory=list)


@dataclass
class WorkoutDayData:
    day: Any  # 'DayNg'
    date: datetime.date
    iteration: int | None
    label: str | None = None

    @property
    def slots(self) -> List[SlotData]:
        if not self.day:
            return []

        return self.day.get_slots(self.iteration)