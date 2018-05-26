from flask import Flask
from flask import render_template, request
app = Flask(__name__)
import boto3, os
from media.s3_storage import S3MediaStorage

s3 = boto3.resource('s3')
storage = S3MediaStorage(s3, os.getenv('204225-jskl'))

@app.route("/")
def hello():
  return "It works Hurray!!!!"

@app.route("/order-animation")
def order_animation():
  return render_template(
    "order.html",
    invitation="Welcome at ani creatior"
  )

@app.route("/upload", methods=["POST"])

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
