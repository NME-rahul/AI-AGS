from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from numpy import array
import os
import grading


error_1 = "Error: Required argument is not provided."
error_2 = "Error: File path is not provided"

'''
variables = {'model': model, 
            	  'processor': processor, 
                  'true_vec': true_answers,
		  'tokenizer': None,
		  'img_path': img_path,
		  'working_dic': None,
}

settings = {'max_length': None,
            'img_shape': 1024,
            'model_name': None,
            'temperature': 0.01, 
            'offset': 2,
            'grad_scale': 10}
'''

def start(variables, settings):
  image_name, image = grading.preprocess_image(variables['img_path'])
  split_img_paths = grading.split_into_lines(image_name, image, 
                                             temperature= settings['temperature'],
                                             offset = settings['offset'],
                                             working_dic = variables['working_dic'])
  generated_text = grading.image_to_text(model = variables['model'], 
                                         processor = variables['processor'], 
                                         split_img_paths = split_img_paths)
  score =  grading.get_score(true_vec = variables['true_vec'],
                            answers = [generated_text],
			    max_length = settings['max_length'],
			    tokenizer = variables['tokenizer'],
                            grad_scale = settings['grad_scale'])

  return score


def setupSettings(variables, settings):
  if variables['model'] == None:
    if settings['model_name'] == None:
      settings['model_name'] = "microsoft/trocr-large-handwritten"
    variables['processor'] = TrOCRProcessor.from_pretrained(settings['model_name'])
    variables['model'] = VisionEncoderDecoderModel.from_pretrained(settings['model_name'])

  if variables['working_dic'] == None:
    variables['working_dic'] = os.getcwd()
  
  if variables['tokenizer'] == None:
    variables['tokenizer'] = Tokenizer(oov_token='<oov>')
    variables['tokenizer'].fit_on_texts(variables['true_vec'])
    variables['true_vec'] = variables['tokenizer'].texts_to_sequences(variables['true_vec'])
    settings['max_length'] = max([len(_) for _ in variables['true_vec']])
    variables['true_vec'] = array(pad_sequences(variables['true_vec'], maxlen=settings['max_length'], padding='post'))

  return variables, settings