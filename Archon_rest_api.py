#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
# AUTHOR : RICHY                                              #
# DATE OF INITIATE : 8/4/2021                                 #
# GITHUB : https://github.com/rixhy                           #
# DISCORD : https://discord.gg/vffWWSK6re                     #
# LANGUAGE : PYTHON 3.7.9                                     #
#  THANKS FOR USING MY CODE, FEEL FREE TO CONTACT ME FOR HELP #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


from flask import Flask
from flask import send_file
from flask import request




app = Flask(__name__)


# about us func

@app.route("/")
def aboutusfunc():
    return """A SIMPLE REST API FOR REFERENCE! THIS API ONLY PERFORM ADDITION! THANKS FOR USING!"""

# addition func

@app.route("/addition")
def addition(a, b):
    return a+b

if __name__ == "__main__":
    app.run(debug=True)
