from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import os
import grading

error_1 = "Error: Required argument is not provided."
error_2 = "Error: File path is not provided"

'''
settings = {'model': model, 
            'processor': processor, 
            'true_answers': true_answers,
            'img_path': img_path,
            'img_shape': 1024;
            'working_dic': None, 
            'setup': False, 
            'model_name': None,
            'temperature': 0.01, 
            'offset': 2,
            'grad_scale': grad_scale}
'''

def start(settings):
  image_name, image = grading.preprocess_image(settings['img_path'])
  split_img_paths = grading.split_into_lines(image_name, image, 
                                             temperature= settings['temperature'],
                                             offset = settings['offset'],
                                             working_dic = settings['working_dic'])
  generated_text = grading.image_to_text(model = settings['model'], 
                                         processor = settings['processor'], 
                                         split_img_paths = split_img_paths)
  score =  grading.get_score(true_answers = settings['true_answers'],
                            answers = generated_text,
                            grad_scale = settings['grad_scale'])

  return score           


def setupSettings(settings):
  if settings['model'] == None:
    if settings['model_name'] == None:
      settings['model_name'] = "microsoft/trocr-large-handwritten"
    settings['processor'] = TrOCRProcessor.from_pretrained(settings['model_name'])
    settings['model'] = VisionEncoderDecoderModel.from_pretrained(settings['model_name'])

  if settings['working_dic'] == None:
    settings['working_dic'] = os.getcwd()

  return settings 