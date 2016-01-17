"""
Copyright 2016 Brian Quach
Licensed under MIT (https://github.com/brianquach/udacity-nano-fullstack-catalog/blob/master/LICENSE)  # noqa
"""
from catalog import app


app.secret_key = 'development'
app.run(host='0.0.0.0', port=8000, debug=True)
