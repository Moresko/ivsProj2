#!/bin/bash

sudo apt-get update
sudo apt-get install python3 
sudo apt-get install python3-pip
pip3 install numpy
pip3 install pyinstaller

OUTPUT_DIR=./Stddev

if [ ! -d "$OUTPUT_DIR" ]
then mkdir "$OUTPUT_DIR"
fi

cat <<EOF >$OUTPUT_DIR/uninstall
#!/bin/bash

TMP=\`pwd -P\` && cd "\`dirname \$TMP\`" && rm -rf "./\`basename \$TMP\`" && unset TMP
EOF

chmod +x $OUTPUT_DIR/uninstall

pyinstaller -F -c --workpath $OUTPUT_DIR/build --distpath $OUTPUT_DIR/dist --specpath $OUTPUT_DIR/build --hidden-import=../repo/src/mathLib -n stddev ../repo/src/stddev.py

rm -f $OUTPUT_DIR/Calculator.spec
cp -v $OUTPUT_DIR/dist/stddev $OUTPUT_DIR
