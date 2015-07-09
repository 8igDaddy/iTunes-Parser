import argparse
import sys
from mutagen import mp4
from mutagen import easymp4
from mutagen import aiff
from mutagen import id3


parser = argparse.ArgumentParser(description='', formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False);

parser.add_argument('-h', '--help', action='help', help='Show this help message and exit.')

parser.add_argument('infile', nargs=None, type=str,
                    help='Specify the HTML file that will be used as an input.');

args = parser.parse_args();



try:
    f = open(args.infile, 'r');
    string = f.read();
    raw_input('The specified file: ' + args.infile + ' has been loaded successfully. Press Enter to continue...');
    index = string.find('class="track-list album music"')
    flag = string.find('</table>', index);
    string = string[index:flag];



    album = 0;
    artist = 0;
    title = 0;
    matrix = [];
    while artist < len(string):
        album = string.find('preview-album="', album);
        if album == -1:
            break;
        artist = string.find('preview-artist="', album);
        if artist == -1:
            break
        #print index;
        beginTitle = string.find('preview-title="', artist) + len('preview-title="');
        if beginTitle == -1:
            break;
        endTitle = string.find('" ', beginTitle);
        if endTitle == -1:
            break;
        matrix.append({'album': string[album + len('preview-album="'):artist - len('" ')], 'title': string[beginTitle:endTitle], 'artist': string[artist + len('preview-artist="'):beginTitle - len('" preview-title="')]});

        album = endTitle + len('"');
    for i in range (0, len(matrix)):
        print matrix[i];

except IOError:
    print 'The specified file: ' + args.infile + ' does not exist.';
    sys.exit();
