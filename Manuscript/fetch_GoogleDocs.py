import requests

# go to https://console.cloud.google.com/apis/credentials
#    to create this API key:
API_key = 'AIzaSyA7Mm_GfQJC4nTWRkDJTF9j3FyFO6mD3H8'

# I got the working url for the request by following:
# https://developers.google.com/drive/api/quickstart/python?authuser=1
file_id = '1leqhuMlYLUmurb1L5Gl9RlRc-7VPcFvuTJfMwPrDi4A'

fKey = 'docx'

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


if __name__=='__main__':

    import argparse

    # First a nice documentation 
    parser=argparse.ArgumentParser(description="""
    A framework to collaborati on scientific papers via Google Docs
    """,
    formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-id', "--doc_id",\
            help = ' document id -- default to "paper-template" ',
            default = '1leqhuMlYLUmurb1L5Gl9RlRc-7VPcFvuTJfMwPrDi4A')

    parser.add_argument("--API_key",\
            help ="""
            API from the google account
                [!] it needs to be re-generated every X-weeks [!]
                go to: 
                    https://console.cloud.google.com/apis/credentials
            """,
            default = 'AIzaSyA7Mm_GfQJC4nTWRkDJTF9j3FyFO6mD3H8')

    parser.add_argument("--format", 
                        help="export format, either: [pdf, docx, md]",
                        default='docx')

    parser.add_argument("--filename", 
                        default='paper')

    args = parser.parse_args()

    main(args)

