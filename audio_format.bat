for %%a in ("./allemande/fragments/*.wav") do ffmpeg -i ./allemande/fragments/"%%a" -ar 44100 -ac 1 -sample_fmt s16 ./allemande/fragments/%%~na_mono.wav

for %%a in ("./syrinx/fragments/*.wav") do ffmpeg -i ./syrinx/fragments/"%%a" -ar 44100 -ac 1 -sample_fmt s16 ./syrinx/fragments/%%~na_mono.wav

for %%a in ("./density/fragments/*.wav") do ffmpeg -i ./density/fragments/"%%a" -ar 44100 -ac 1 -sample_fmt s16 ./density/fragments/%%~na_mono.wav

for %%a in ("./sequenza/fragments/*.wav") do ffmpeg -i ./sequenza/fragments/"%%a" -ar 44100 -ac 1 -sample_fmt s16 ./sequenza/fragments/%%~na_mono.wav