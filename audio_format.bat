for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold1\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold1\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold2\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold2\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold3\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold3\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold4\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold4\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold5\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold5\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold6\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold6\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold7\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold7\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold8\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold8\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold9\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formated\fold9\%%~na.wav

for %%a in ("\\CTRIAS\audio_dataset\UrbanSound8K\audio\fold10\*.wav") do ffmpeg -i "%%a" -ar 44100 -ac 1 -sample_fmt s16 \\CTRIAS\audio_dataset\UrbanSound8K\formatedfold10\%%~na.wav