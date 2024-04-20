from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.training_pipeline import TrainPipeline

#from sensor.utils import dump_csv_file_to_mongodb_collection

#def test_exception():
#  try:
#    logging.info("ki yaha pe bhahiya ek error ayegi devision by zero wali error")
#   a=1/0
#except Exception as e:
#    raise SensorException(e,sys)


if __name__ == '__main__':
    
    #file_path = "C:/Projects/Sensor_detection/aps_failure_training_set1.csv"
    #database_name = "APS_detection"
    #collection_name = "sensor"
    #dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    
#try:
#test_exception()
#except SensorException as e:
#  print(e)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()