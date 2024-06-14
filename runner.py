from transformers import TrOCRProcessor, VisionEncoderDecoderModel

import pandas as pd
from numpy import array
import os
import grading
import model
import sys


def start(VARIABLES, SETTINGS):
  image_name, image = model.preprocess_image(VARIABLES['img_path'])
  split_img_paths = model.split_into_lines(image_name, image, 
                                             temperature= SETTINGS['temperature'],
                                             offset = SETTINGS['offset'],
                                             working_dic = SETTINGS['working_dic'])
  generated_text = model.image_to_text(model = VARIABLES['model'], 
                                         processor = VARIABLES['processor'], 
                                         split_img_paths = split_img_paths)
  score =  grading.get_score(VARIABLES["true_answers"], generated_text)

  return score

def downloads(SETTINGS):
    if not os.path.exists(os.path.join(os.getcwd(), SETTINGS['model_directory'])):
      processor = TrOCRProcessor.from_pretrained(f"{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      processor.save_pretrained(f"{SETTINGS['model_directory']}/{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      model = VisionEncoderDecoderModel.from_pretrained(f"{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      model.save_pretrained(f"{SETTINGS['model_directory']}/{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      grading.download_dependencies()
      
def setupSettings(SETTINGS):
  if SETTINGS['model_directory'] == None:
    SETTINGS['model_directory'] = 'models'
  if SETTINGS['model_name'] == None:
    SETTINGS['model_publisher'] = "microsoft"
    SETTINGS['model_name'] = "trocr-large-handwritten"
  if SETTINGS['working_dic'] == None:
    SETTINGS['working_dic'] = os.getcwd()
  return SETTINGS

def loadModel(VARIABLES, SETTINGS):
  if os.path.join(os.getcwd(), SETTINGS['model_directory'], SETTINGS['model_publisher'], SETTINGS['model_name']):  
    VARIABLES['processor'] = TrOCRProcessor.from_pretrained(os.path.join(os.getcwd(), SETTINGS['model_directory'], SETTINGS['model_publisher'], SETTINGS['model_name']))
    VARIABLES['model'] = VisionEncoderDecoderModel.from_pretrained(os.path.join(os.getcwd(), SETTINGS['model_directory'], SETTINGS['model_publisher'], SETTINGS['model_name']))
  else:
    sys.exit('model not found, retry after downloading.')
  if not VARIABLES['tokenizer']:
    grading.init(VARIABLES['true_answers'])
  return VARIABLES


def restoreSettings(VARIABLES, SETTINGS):
  df = pd.read_csv('logs/save.csv')
  print(df.head())
  SETTINGS['model_directory'] = df['model_directory']
  SETTINGS['nltk_directory'] = df['nltk_directory']
  SETTINGS['img_shape'] = df['img_shape']
  SETTINGS['model_publisher'] = df['model_publisher']
  SETTINGS['model_name'] = df['model_name']
  SETTINGS['model_name'] = df['model_name']
  SETTINGS['temperature'] = df['temperature']
  SETTINGS['offset'] = df['offset']
  SETTINGS['grad_scale'] = df['grad_scale']
  SETTINGS['working_dic'] = df['working_dic']
  return SETTINGS