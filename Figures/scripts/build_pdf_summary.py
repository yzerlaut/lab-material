import string, datetime, os
from tempfile import gettempdir
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
from PIL import Image 

A4 = {'w':8.27, 'h':11.69}

with PdfPages('Figures.pdf') as pdf:
    
    pngs = os.listdir('./pngs')
    for png in pngs:

        im = Image.open(os.path.join('pngs', png))
        dpi = int(im.info['dpi'][0])
        w, h = im.width/dpi, im.height/dpi
        print(dpi, w, h)

        fig = plt.figure(figsize=(8.27, 11.69), dpi=dpi)
        plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

        ax = fig.add_axes([(A4['w']-w)/2./A4['w'], (A4['h']-h)/2./A4['h'], 
                           w/A4['w'], h/A4['h']])
        ax.axis('off')

        ax.imshow(im, interpolation=None)
        # ax.annotate(png, (0.1, 1), xycoords='axes fraction', fontsize=12)
        ax.annotate(png.replace('.png', ''), (0.1, 0.9), xycoords='figure fraction', fontsize=12)
        pdf.savefig(fig)  # saves the current figure into a pdf page



