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
import barcode
from barcode.writer import ImageWriter
import pdfkit


class Report(object):
    """
    This is a helper extension, which adjusts logging configuration for the
    application.
    """

    def create_dewar_labels(self, shipping_info_dict, dewar_dict):
        html_filename = "dewar_%d_label.html" % dewar_dict["dewarId"]
        pdf_filename = "dewar_%d_label.pdf" % dewar_dict["dewarId"]

        with open(self.get_static_file_path("dewar_label_template.html")) as f:
            html_template = f.read()

        ean = barcode.get(
            current_app.config["BARCODE_TYPE"],
            dewar_dict["barCode"],
            writer=ImageWriter(format="PNG"),
        )
        dewar_barcode_filepath = os.path.join(current_app.config["TEMP_DIR"], "barcode")
        ean.save(dewar_barcode_filepath)

        html_template = html_template.format(
            dewar_barcode_filepath=dewar_barcode_filepath + ".png",
            site_name=current_app.config["SITE_NAME"],
            parcel_label=dewar_dict["code"],
            shipping_label=shipping_info_dict["shipping"]["shippingName"],
            num_parcels="1",
            proposal_number="%s%s"
            % (
                shipping_info_dict["proposal"]["proposalCode"],
                shipping_info_dict["proposal"]["proposalNumber"],
            ),
            laboratory_name=shipping_info_dict["send_lab"]["name"],
            local_contact="5",
        )

        html_file = open(
            os.path.join(current_app.config["TEMP_DIR"], html_filename), "w"
        )
        html_file.write(html_template)
        html_file.close()
        pdfkit.from_file(
            os.path.join(current_app.config["TEMP_DIR"], html_filename),
            os.path.join(current_app.config["TEMP_DIR"], pdf_filename),
        )

        return html_filename, pdf_filename

    def get_static_file_path(self, filename):
        return os.path.join(current_app.root_path, "static", filename)


report = Report()
