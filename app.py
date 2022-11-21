from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://live.staticflickr.com/2712/4480686543_2983b9ffdd_o.jpg",
    "https://live.staticflickr.com/4027/4480686311_fb8f853abd_o.jpg",
    "https://live.staticflickr.com/3847/14707542225_221219af92_o.jpg",
    "https://live.staticflickr.com/8147/7450112678_e2bc18c14b_k.jpg",
    "https://live.staticflickr.com/8481/29068166132_3b3460e983_h.jpg",
    "https://live.staticflickr.com/7336/9649943430_bdb2fccb29_o.jpg",
    "https://live.staticflickr.com/3784/13735475843_6e956fd202_o.jpg",
    "https://live.staticflickr.com/2290/2063451702_7ae5336d28_o.jpg",
    "https://live.staticflickr.com/8651/16621333722_2f9e4a6ed8_o.jpg",
    "https://live.staticflickr.com/2312/1947165002_03a6383e1c_o.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
