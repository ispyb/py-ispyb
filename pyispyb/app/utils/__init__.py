"""Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


def create_response_item(msg=None, num_items=None, data=[]):
    """
    Creates response dictionary.

    Args:
        info_msg ([type]): [description]
        error_msg ([type]): [description]
        num_items ([type]): [description]
        data ([type]): [description]

    Returns:
        [type]: [description]
    """

    return {
        "data": {"total": num_items, "rows": data},
        "message": msg,
    }
