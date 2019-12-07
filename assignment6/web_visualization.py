from flask import Flask
import visualize
import io
from flask import Response, render_template, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

"""
Flask web app displaying a scatter plot using the visualize module.
"""

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('selection.html')

@app.route("/selection", methods=['POST'])
def selection():
    imgsrc = 'static/images/image.png'
    first = request.form['first']
    second = request.form['second']
    third = request.form['third']
    visualize.visualize(first,second,third)[0].savefig(imgsrc)    
    return render_template('draw.html', imgsrc = imgsrc)


if __name__ == "__main__":
    app.run(debug=True)
