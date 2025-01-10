###################################################
##   script to convert svg figures to png/tiff  ###
##    ----------------------------------------  ###
##        relies on inkscape & image-magick:    ###
##            brew install inkscape             ###
##            brew install magick               ###
###################################################

mkdir -p ./tiffs
mkdir -p ./pngs

# find inkscape
case "$OSTYPE" in
linux*)
    inkscape="inkscape"
    ;;
darwin*)
    inkscape="/Applications/Inkscape.app/Contents/MacOS/Inkscape"
    ;;
msys*)
    inkscape="/c/Program\ Files/Inkscape/bin/inkscape.exe"
    ;;
esac

for filename in ./*.svg; do
    echo "processing" $filename " [...]"
    $inkscape --export-filename=./pngs/${filename/svg/png} --export-area-drawing $filename
    magick ./pngs/${filename/svg/png} ./tiffs/${filename/svg/tiff} 
done
