from fetch_GoogleDocs import *
import datetime
import argparse

# First a nice documentation 
parser=argparse.ArgumentParser(description="""
A framework to collaborati on scientific papers via Google Docs
""",
formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-id', "--doc_id", default='')
parser.add_argument("--API_key", default='')

args = parser.parse_args()

args.format = 'md'
args.filename = './backups/%s' % datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

if args.API_key=='':
    check_API(args)

if args.doc_id=='':
    check_ID(args)

if args.API_key!='' and args.doc_id!='':
    main(args)
