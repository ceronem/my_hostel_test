{
    "name": "Hostel Management",
    "summary": "Module for managing hostel operations",
    "description": "A comprehensive module to manage hostel operations, including room bookings, guest management, and billing.",
    "author": "Mauro Cerone",
    "license": "AGPL-3",
    "version": "1.0",
    "website": "http://www.example.com",
    "category": "Hospitality",
    "depends": ["base"],
    "data": [
        "security/hostel_security.xml",
        "security/ir.model.access.csv",
        "views/hostel.xml",
        "views/hostel_room.xml",
        "data/data.xml",
    ],
    # "assets": {
    #     "web.assets_backend": ["web/static/src/xml/**/*"],
    # },
    # "demo": [
    #     "demo/demo.xml",
    # ],
}
