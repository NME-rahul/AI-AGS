from transformers import TrOCRProcessor, VisionEncoderDecoderModel

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
                                             working_dic = VARIABLES['working_dic'])
  generated_text = model.image_to_text(model = VARIABLES['model'], 
                                         processor = VARIABLES['processor'], 
                                         split_img_paths = split_img_paths)
  score =  grading.get_score(VARIABLES["true_answers"], generated_text)

  return score

def downloads(SETTINGS):
    if not os.path.exists(os.path.join(os.getcwd(), SETTINGS['model_directory'])):
      if SETTINGS['model_name'] == None:
        SETTINGS['model_publisher'] = "microsoft"
        SETTINGS['model_name'] = "trocr-large-handwritten"
      processor = TrOCRProcessor.from_pretrained(f"{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      processor.save_pretrained(f"{SETTINGS['model_directory']}/{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      model = VisionEncoderDecoderModel.from_pretrained(f"{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      model.save_pretrained(f"{SETTINGS['model_directory']}/{SETTINGS['model_publisher']}/{SETTINGS['model_name']}")
      grading.download_dependencies()
    return SETTINGS

def setupSettings(VARIABLES, SETTINGS):
  if SETTINGS['model_name'] == None:
    SETTINGS['model_publisher'] = "microsoft"
    SETTINGS['model_name'] = "trocr-large-handwritten"
  if os.path.join(os.getcwd(), SETTINGS['model_directory'], SETTINGS['model_publisher'], SETTINGS['model_name']):  
    VARIABLES['processor'] = TrOCRProcessor.from_pretrained(os.path.join(os.getcwd(), SETTINGS['model_directory'], SETTINGS['model_publisher'], SETTINGS['model_name']))
    VARIABLES['model'] = VisionEncoderDecoderModel.from_pretrained(os.path.join(os.getcwd(), SETTINGS['model_directory'], SETTINGS['model_publisher'], SETTINGS['model_name']))
  else:
    sys.exit('model not found, retry after downloading.')
    
  if VARIABLES['working_dic'] == None:
    VARIABLES['working_dic'] = os.getcwd()
  if not VARIABLES['tokenizer']:
    grading.init(VARIABLES['true_answers'])
  return VARIABLES, SETTINGS