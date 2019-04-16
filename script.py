import matplotlib.pyplot as plt
import librosa.display


import librosa

audio_path = 'born_mitiS.mp3'
x, sr = librosa.load(audio_path)


plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)
plt.show()

