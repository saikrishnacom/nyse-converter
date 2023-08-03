from dask import dataframe as dd
import os
import glob
import logging


def main():
    logging.basicConfig(
        filename='logs/nc.log',
        level=logging.INFO,
        format='%(levelname)s %(asctime)s %(message)s',
        datefmt='%Y-%m-%d %I:%M-%S %p'
    )
    scr_dir = os.environ['SRC_DIR']
    # tgt_dir = os.environ['TGT_DIR']
    src_file_pattern = os.environ.setdefault('SET_FILE_PATTERN','NYSE_*.txt.gz')
    src_file_name = glob.glob(f'{scr_dir}/{src_file_pattern}')
    tgt_file_names=[file.replace('txt','json').replace('nyse_data','nyse_json') for file in src_file_name]
    logging.info('file format conversion is started')
    df= dd.read_csv(src_file_name,
        names=['ticker','trade_data','open_price','low_price','high_price','close_price','volume'],
            blocksize=None)
    logging.info('data frame is created and will be  written in JSON format')
    df.to_json(tgt_file_names,
                orient = 'records',
                lines = True,
                compression ="gzip")
    logging.info('file format conversion completed')

if __name__=="__main__":
    main()