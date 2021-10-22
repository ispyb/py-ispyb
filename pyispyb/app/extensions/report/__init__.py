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
import qrcode
import pdfkit


class Report(object):
    """
    This is a helper extension, which adjusts logging configuration for the
    application.
    """

    def create_dewar_labels(self, shipping_info_dict, dewar_dict):
        html_filename = "dewar_%d_label.html" % dewar_dict["dewarId"]
        pdf_filename = "dewar_%d_label.pdf" % dewar_dict["dewarId"]

        with open(current_app.config["DEWAR_LABEL_TEMPLATE_FILEPATH"]) as template_file:
            html_template = template_file.read()

        barcode_image = barcode.get(
            current_app.config["BARCODE_TYPE"],
            dewar_dict["barCode"],
            writer=barcode.writer.ImageWriter(format="PNG"),
        )
        barcode_filepath = os.path.join(
            current_app.config["TEMP_FOLDER"], "barcode"
        )
        barcode_image.save(barcode_filepath)

        qrcode_filepath = os.path.join(
            current_app.config["TEMP_FOLDER"], "qrcode.png"
        )
        qrcode_image = qrcode.make(dewar_dict["barCode"])
        qrcode_image.save(qrcode_filepath)

        html_template = html_template.format(
            site_logo_filepath=current_app.config["SITE_LOGO_PATH"],
            barcode_filepath=barcode_filepath + ".png",
            qrcode_filepath=qrcode_filepath,
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
            os.path.join(current_app.config["TEMP_FOLDER"], html_filename), "w"
        )
        html_file.write(html_template)
        html_file.close()

        pdfkit.from_file(
            str(os.path.join(current_app.config["TEMP_FOLDER"], html_filename)),
            str(os.path.join(current_app.config["TEMP_FOLDER"], pdf_filename)),
        )

        return html_filename, pdf_filename


report = Report()
