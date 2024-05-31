import runner
import grading
import os

VARIABLES = {'model': None, 
	     'processor': None, 
             'true_answers': "live in Lviv. everyday I go to work by bus also i would like to visit Mars",
	     'tokenizer': False,
	     'img_path': "C:/Users/arvin/OneDrive/Desktop/AI-AGS/download.jpeg",
	     'working_dic': None}

SETTINGS = {'max_length': None,
            'model_directory' : "models",
            'nltk_directory': f"c:/Users/{os.getenv('USER')}/AppData/Roaming/nltk_data",
            'img_shape': 1024,
            'model_publisher': None,
            'model_name': None,
            'temperature': 0.01, 
            'offset': 2,
            'grad_scale': 10}

if __name__ == "__main__":
  SETTINGS = runner.downloads(SETTINGS)
  VARIABLES, SETTINGS = runner.setupSettings(VARIABLES, SETTINGS)
  score = runner.start(VARIABLES, SETTINGS)
  print(score)
