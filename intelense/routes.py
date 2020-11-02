import os
import librosa
from flask import render_template, request, send_file

from intelense.forms import FindPeaks
from intelense.modal import find_peaksounds

from intelense import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = FindPeaks()
    if request.method == 'POST':
        file = form.file.data
        save_path = os.path.join(app.root_path, 'uploads', file.filename)
        file.save(save_path)
        filepath = os.path.join(app.root_path, 'uploads', file.filename)
        data, sampling_rate = librosa.load(filepath)
        find_peaksounds(data, sampling_rate)
        path = os.path.join('static/data', 'Highpeaksounds.wav')
        return send_file(path, as_attachment=True)
    return render_template('home.html', title='Home', form=form)
