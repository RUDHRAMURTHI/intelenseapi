import os
import numpy as np
from scipy.signal import find_peaks
import soundfile as sf
from intelense import app


def find_peaksounds(data, sampling_rate):
    peaks, properties = find_peaks(data, prominence=np.max(data), width=120)

    audio = []
    for peak in peaks:
        if peak >= 5000:
            audio.append(data[peak - 5000:peak + 5000])
        else:
            audio.append(data[0:peak + 5000])

    final_audio = np.concatenate(audio, axis=0)
    path = os.path.join(app.root_path, 'static/data', 'Highpeaksounds.wav')
    sf.write(path, final_audio, sampling_rate)
