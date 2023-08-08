source /home/itversity/nyse-converter/nc-venv/bin/activate
export SRC_DIR=/home/itversity/nyse-converter/data/nyse_all/nyse_data
export LOG_FILE_PATH=/home/itversity/file-format-converter/logs/nc.log
rm -rf /home/itversity/nyse-converter/data/nyse_all/nyse_json
mkdir -p /home/itversity/nyse-converter/logs
nyseconverter
deactivate