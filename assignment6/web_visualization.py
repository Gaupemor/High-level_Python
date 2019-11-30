from flask import Flask
import visualize
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

"""
Flask web app displaying a scatter plot using the visualize module.
"""

app = Flask(__name__)

@app.route("/")
def index():
    plt, training_score, validation_score = visualize.make_probability_scatterplot("insulin", "glucose");
    output = io.BytesIO()
    canvas = FigureCanvas(plt.gcf()).print_png(output)
    canvas.draw()
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    app.run()
