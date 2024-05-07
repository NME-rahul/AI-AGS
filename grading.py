import cv2
import numpy as np
import os

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from numpy import sqrt, power, sum, dot, array, average

def preprocess_image(path, img_shape=1024):
  image_name = path.split('/')[-1]
  image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
  image = cv2.threshold(image, 100, 255, 0)
  image = image[1]
  image = cv2.resize(image, (img_shape, img_shape))
  return image_name, image

def split_into_lines(image_name, image, temperature, offset=2, working_dic=None):
  x = 1; #binary semaphore to get lock on first black and after first white line
  i = 0;
  num_rows = image.shape[0]

  threshold = image.shape[1] * (temperature/10) #base 10

  img_cnt = 0
  
  if working_dic == None:
    working_dic = os.getcwd() + "/splited_images"

  os.system(f'mkdir {working_dic}')

  split_img_paths = []
  image_name, ext = image_name.split('.')

  while True:
    if i == num_rows:
      break;

    row = image[i, :]

    if 0 in row and x == 1:
      if np.count_nonzero(row == 0) > threshold:
        save = i
        x = 0;

    if 0 not in row and  x == 0:      
      split_path = os.path.join(working_dic, image_name)
      os.system(f'mkdir {split_path}')

      split_img = image_name + f"_{img_cnt}." + str(ext)
      split_img_paths.append(os.path.join(working_dic, split_img))
      cv2.imwrite(split_img_paths[img_cnt], image[save-offset:i+offset, :])
      x = 1;
      img_cnt += 1

    i = i + 1
  return split_img_paths

def image_to_text(model, processor, split_img_paths):
  generated_text = ''

  for p in split_img_paths:
    image = cv2.imread(p)

    pixel_values = processor(image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)

    generated_text = generated_text + " " + processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

  return generated_text

def get_score(true_answers, answers, grad_scale):
  def cosine(vec1, vec2):
    similarity = []
    for x, y in zip(vec1, vec2):
      nume = dot(x, y)
      denom = sqrt(sum(power(x, 2)))*sqrt(sum(power(y, 2)))
      similarity.append( nume / denom )
    return array(similarity)

  tokenizer = Tokenizer(oov_token='<oov>')
  tokenizer.fit_on_texts(true_answers)

  vec1 = tokenizer.texts_to_sequences(true_answers)
  max_length = max([len(_) for _ in vec1])
  vec1 = array(pad_sequences(vec1, maxlen=max_length, padding='post'))
  vec2 = tokenizer.texts_to_sequences(answers)
  vec2 = array(pad_sequences(vec2, maxlen=max_length, padding='post'))

  return cosine(vec1, vec2) * grad_scale