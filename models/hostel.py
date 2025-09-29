from odoo import api, fields, models


class Hostel(models.Model):
    _name = "hostel.hostel"
    _description = "Information about Hostel"
    _order = "id desc, name"
    _rec_name = "hostel_code"
    name = fields.Char(string="Hostel Name", required=True)
    hostel_code = fields.Char(string="Code", required=True)
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    zip = fields.Char(string="Zip", change_default=True)
    city = fields.Char(string="City")
    state_id = fields.Many2one("res.country.state", string="State")
    country_id = fields.Many2one("res.country", string="Country")
    phone = fields.Char(string="Phone", required=True)
    mobile = fields.Char(string="Mobile", required=True)
    email = fields.Char(string="Email")
    hostel_floors = fields.Integer(string="Total Floors")
    image = fields.Binary(string="Hostel Image")
    active = fields.Boolean(
        string="Active", default=True, help="Activate or deactivate a hostel"
    )
    type = fields.Selection(
        selection=[("male", "Boys"), ("female", "Girls"), ("common", "Common")],
        string="Type",
        help="Type of Hostel",
        required=True,
        default="common",
    )
    other_info = fields.Text(string="Other Information", help="Additional Information")
    description = fields.Html(string="Description")
    hostel_rating = fields.Float("Hotel Rating", digits="Rating Value")

    @api.depends("hostel_code")
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.hostel_code:
                name = f"{name} ({record.hostel_code})"
            record.display_name = name
