import runner
import grading
import os
import handleTasks
import log

VARIABLES = {'model': None, 
             'processor': None,
             'true_answers': "live in Lviv. everyday I go to work by bus also i would like to visit Mars",
		     'tokenizer': False,
		     'img_path': "C:/Users/arvin/OneDrive/Desktop/AI-AGS/download.jpeg",
		     }

SETTINGS = {
            'model_directory' : "models",
            'nltk_directory': f"c:/Users/{os.getenv('USERNAME')}/AppData/Roaming/nltk_data",
            'img_shape': 1024,
            'model_publisher': None,
            'model_name': None,
            'temperature': 0.01, 
            'offset': 2,
            'grad_scale': 10,
            'working_dic': None}
 
if __name__ == "__main__":
 
    
  if os.path.exists('logs'):
    SETTINGS = runner.restoreSettings(VARIABLES, SETTINGS)
  else:
    SETTINGS = runner.setupSettings(SETTINGS)
    runner.downloads(SETTINGS)
    log.setlogFiles()
    
  print(SETTINGS)

  '''
  

  log.startTime()
  queue = handleTasks.Queue(10)
  VARIABLES = runner.loadModel(VARIABLES, SETTINGS)
  log.SaveSettings(SETTINGS, VARIABLES)
  score = runner.start(VARIABLES, SETTINGS)
  queue.enqueue(score)
  print(score)
  queue.sneekPeak()
  '''
