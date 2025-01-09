import requests, os

# TYPES OF POSSIBLE EXPORT FORMATS
eType = {
    'pdf':'application/pdf',
    'docx':'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'md':'text/markdown'
}

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def main(args):

    URL = 'https://www.googleapis.com/drive/v3/files/{file_id}/export?mimeType={format}&key={key}&alt=media'.format(**{'file_id':args.doc_id,

                                                                                                           'format':eType[args.format].replace('/','%2F'),
                                                                                                                    'key':args.API_key})
    session = requests.Session()
    response = session.get(URL, stream=True)
    token = get_confirm_token(response)
    response = session.get(URL, stream=True)

    save_response_content(response, '%s.%s' % (args.filename,
                                               args.format))

def check_API(args):

    if os.path.isfile('./google_API_key.txt'):

        with open('./google_API_key.txt', 'r') as f:
            args.API_key = str(f.read())

    else:

        print("""

        (it needs to be re-generated every xx weeks)
        to create the google API key, go to:
                https://console.cloud.google.com/apis/credentials

        [!!] file: 'google_API_key.txt' not found in the current directory [!!]
                --> unpossible to fetch the document

        """)

def check_ID(args):

    if os.path.isfile('./manuscript_ID.txt'):

        with open('./manuscript_ID.txt', 'r') as f:
            args.doc_id= str(f.read())

    else:

        print("""

        [!!] file: 'manuscript_ID.txt' not found in the current directory [!!]
                --> unpossible to fetch the document

        """)


if __name__=='__main__':

        
        import argparse

        # First a nice documentation 
        parser=argparse.ArgumentParser(description="""
        A framework to collaborati on scientific papers via Google Docs
        """,
        formatter_class=argparse.RawTextHelpFormatter)

        parser.add_argument('-id', "--doc_id", default='')
        parser.add_argument('-k', "--API_key", default='')

        parser.add_argument('-f', "--format", 
                            help="export format, either: [pdf, docx, md]",
                            default='docx')

        parser.add_argument("--filename", 
                            default='paper')

        args = parser.parse_args()

        if args.API_key=='':
            check_API(args)

        if args.doc_id=='':
            check_ID(args)

        if args.API_key!='' and args.doc_id!='':
            main(args)

