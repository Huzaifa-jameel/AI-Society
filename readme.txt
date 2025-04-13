/AI-SOCIETY/
│
├── /static/                  # Static folder (Flask requires this name)
│   ├── style.css             # Your only CSS file (keep it exactly as-is)
│   └── script.js             # Your JS file (exactly as-is)
│   |-- Images/
|
├── /templates/              # All HTML files go here
│   └── index.html           # Your single HTML file (keep code unchanged)
│
├── /app/                    # All Flask logic goes here
│   ├── __init__.py          # Initializes app + DB
│   ├── routes.py            # Routing logic (serves HTML, handles form)
│   ├── auth.py              # Registration logic (MySQL interaction)
│   └── models.py            # User model (for registration)
│
├── /instance/               # For private config (MySQL URI, secret key)
│   └── config.py            # Secure configs
|-- file.env
├── config_global.py         # Global config (dev vs prod setup)
├── run.py                   # App entry point
├── requirements.txt         # List of Python packages used
└── README.md                # Setup instructions (optional)
