#!/bin/bash

sudo apt-get update
sudo apt-get install python3 
sudo apt-get install python3-pip
sudo apt-get install python3-tk
pip3 install numpy
pip3 install pyinstaller

OUTPUT_DIR=./Calculator

if [ ! -d "$OUTPUT_DIR" ]
then mkdir "$OUTPUT_DIR"
fi

cat <<EOF >$OUTPUT_DIR/uninstall
#!/bin/bash

TMP=\`pwd -P\` && cd "\`dirname \$TMP\`" && rm -rf "./\`basename \$TMP\`" && unset TMP
EOF

chmod +x $OUTPUT_DIR/uninstall

pyinstaller -F -w --workpath $OUTPUT_DIR/build --distpath $OUTPUT_DIR/dist --specpath $OUTPUT_DIR/build --hidden-import=../repo/src/controller --hidden-import=../repo/src/mathLib -n Calculator ../repo/src/calc.py

rm -f $OUTPUT_DIR/build/Calculator.spec
cp -v $OUTPUT_DIR/dist/Calculator $OUTPUT_DIR
