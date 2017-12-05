#!/bin/bash

cd ${1}
for file in *.JPEG; do
        w=`identify -format "%w" ${file}`
        h=`identify -format "%h" ${file}`

        [ ${w} -le ${h} ] && size=${w} || size=${h}

        convert ${file} -gravity center -crop ${size}x${size}+0+0 tmp_${file}
        mv tmp_${file} ${file}
done

mogrify -resize 256x256 -type TrueColor *.JPEG
