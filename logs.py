from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Logs Analysis</title>
    <style>
    </style>
  </head>
  <body>
    <h1>Logs Analysis</h1>
    <form method=post>
    </form>
  </body>
</html>
'''

Result = '''\
    <div class=result><em class=date>%s</em><br>%s</div>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  html = HTML_WRAP
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)


