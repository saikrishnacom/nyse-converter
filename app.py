from dask import dataframe as dd
import os

def main():
    scr_dir = os.environ['SRC_DIR']
    tgt_dir = os.environ['TGT_DIR']
    print('file format conversion is started')
    df= dd.read_csv(f'{scr_dir}/*',
        names=['ticker','trade_data','open_price','low_price','high_price','close_price','volume'],
        blocksize=None)
    print('data frame is created and will be  written in JSON format')
    df.to_json(f'{tgt_dir}/part-*.json.gz',
               orient = 'records',
               lines = True,
               compression ="gzip",
               name_function = lambda i: '%05d' %i)
    print('file format conversion completed')
if __name__=="__main__":
    main()