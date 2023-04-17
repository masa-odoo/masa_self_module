{
    'name': "Hospital Management System",
    'author': "Aman",
    'version': '0.1.0',
    'category': 'HMS',
    'description': """

    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/appointment.xml',
        'views/diagnosis.xml',
        'views/doctor.xml',
        'views/bed.xml',
        'views/bills.xml',
        'views/hms_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',

    ],
    'application': True,
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}