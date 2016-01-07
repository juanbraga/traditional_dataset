#bin/bash           
echo stereo to mono convertion...
for file in ./*
do
out=".""$(echo $file | cut -d'.' -f 2 )" 
out=$out"_mono.wav"
#echo $out
#echo $file
avconv -i $file -ac 1 $out
done     
