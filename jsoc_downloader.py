from sunpy.net import jsoc
from sunpy.net import attrs as a
#import astropy.units as u
import time

import argparse

def download_data(args):
    mail = args.mail
    series = args.series
    start = args.start
    end = args.end
    #sample = args.sample
    #wavelength = args.wavelength

    print('Staging client...')    
    client = jsoc.JSOCClient()

    print('Searching for data...')
    res = client.search(a.Time(start, end),
                        #a.Sample(sample*u.min),
                        a.jsoc.Series(series),
                        #a.Wavelength(wavelength*u.AA),
                        a.jsoc.Notify(mail))
    
    print('Requesting data...')
    requests = client.request_data(res) 
    print('Request ID:', requests.id)
    print('Status:', requests.status)
    
    while requests.status != 0:
        print('Please wait...')
        time.sleep(30)
    if requests.status == 0:
        client.get_request(requests)


if __name__ == '__main__':
    print(r"""                                                                   
    __ _____ _____ _____    ____                _           _         
 __|  |   __|     |     |  |    \ ___ _ _ _ ___| |___ ___ _| |___ ___ 
|  |  |__   |  |  |   --|  |  |  | . | | | |   | | .'| . | . | -_|  _|
|_____|_____|_____|_____|  |____/|___|_____|_|_|_|__,|___|___|___|_|  
                                                                      
    JSOC Downloader v0.1 Alpha""")
    
    parser = argparse.ArgumentParser(description='JSOC Downloader')
    parser.add_argument('--mail', type=str, help='Email address')
    parser.add_argument('--series', type=str, help='Series name')
    parser.add_argument('--start', type=str, help='Start time in the format YYYY-MM-DDTHH:MM:SS')
    parser.add_argument('--end', type=str, help='End time in the format YYYY-MM-DDTHH:MM:SS')
    #parser.add_argument('--sample', type=int, help='Sample rate in minutes')
    #parser.add_argument('--wavelength', type=int, help='Wavelength in angstrom')
    args = parser.parse_args()

    download_data(args)