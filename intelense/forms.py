from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import SubmitField, FileField


class FindPeaks (FlaskForm):
    file = FileField('Upload Your Audio/Video For Finding High Peak Sounds',
                     validators=[FileRequired(), FileAllowed(['wav', 'mp3', 'mp4'],
                                                             "Invalid file format, "
                                                             "allowed format "
                                                             "is: .wav, .mp3, .mp4")])
    submit = SubmitField('Find Peak Sounds')
