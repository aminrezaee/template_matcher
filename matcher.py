import cv2
import os
from concurrent.futures import ThreadPoolExecutor as Pool
class Matcher():
    def __init__(self , base_image_path:str , threshold:float) -> None:
        self.base_image = self.read_image(base_image_path)
        self.threshold = threshold
        self.results = []
        

    def read_image(self, path:str):
        return cv2.resize(cv2.cvtColor(cv2.imread(path) , cv2.COLOR_BGR2GRAY) , dsize=(32,32))
    
    def match_one_image(self, path:str):
        query_image = self.read_image(path)
        result = cv2.matchTemplate(self.base_image, query_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # print(f"{path}:{max_val}")
        if max_val >= self.threshold:
            self.results.append(path)
        return
        
    def query(self, directory:str):
        self.results = []
        file_names  = os.listdir(directory)
        pathes = [f"{directory}/{item}" for item in file_names]
        with Pool(10) as executor:
            list(executor.map(self.match_one_image , pathes))
        