to run this code write this  [][ python -m flask run ]  in terminal

# steps You are very close!
You have successfully created a virtual environment and installed all dependencies inside it.
But your terminal is still using the system Python (not the virtual environment) when running flask run.

# How to start :

Activate your virtual environment
In your project directory, run:
 [][ source venv/bin/activate ]
You should see (venv) at the start of your terminal prompt.

Check Python and pip location
Run:
[#][ which python ]
[#][ which pip ]
Both should point to your venv directory.

Install dependencies again (if needed)
If you haven't already, run:
[#][ pip install flask playwright beautifulsoup4 ]
[#][ python -m playwright install ]
Run your Flask app
Make sure you are in the parent directory of app and run:
[#][ export FLASK_APP=app/views.py ]
[#][ flask run ]
or
[#][  python -m flask run  ]

[#] you will revice the output in your browser at http://127.0.0.1:5000/
[#] and you will get [scraped_data.json] file in the project root

[#] if you need more help contact me on [gamal.nasser.dev@gmail.com]

