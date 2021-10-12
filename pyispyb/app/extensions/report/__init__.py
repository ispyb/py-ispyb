"""
Project: py-ispyb
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


__license__ = "LGPLv3+"

import os
import logging
from flask import current_app

try:
    import pdfkit
except ModuleNotFoundError:
    print("pdfkit not available")
    # logging.getLogger("ssss").warning("pdfkit not available")


class Report(object):
    """
    This is a helper extension, which adjusts logging configuration for the
    application.
    """

    def __init__(self, app=None):
        self.upload_dir = None

    def init_app(self, app):
        self.upload_dir = app.config["UPLOAD_DIR"]

    def create_dewar_labels(self, dewar_info):
        html_filename = "dewar_%d_label.html" % dewar_info["dewarId"]
        pdf_filename = "dewar_%d_label.pdf" % dewar_info["dewarId"]

        with open(self.get_static_file_path("dewar_label_template.html")) as f:
            html_template = f.read()

        html_template = html_template.format(
            site_name="Site",
            parcel_label="1",
            shipment_label="2",
            num_parcels="1",
            proposal_number="3",
            laboratory_name="4",
            local_contact="5",
        )

        html_file = open(os.path.join(self.upload_dir, html_filename), "w")
        html_file.write(html_template)
        html_file.close()
        pdfkit.from_file(
            os.path.join(self.upload_dir, html_filename),
            os.path.join(self.upload_dir, pdf_filename),
        )

        return html_filename, pdf_filename

    def get_static_file_path(self, filename):
        return os.path.join(current_app.root_path, "static", filename)


report = Report()
