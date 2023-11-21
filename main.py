from matcher import Matcher
import os
from concurrent.futures import ThreadPoolExecutor as Pool
import shutil
def copy(source:str , destination:str):
    shutil.copyfile(source , destination)
    return

if __name__ == "__main__":
    current_path = os.getcwd()
    matcher = Matcher(f"{current_path}/template.jpg" , threshold=0.8)
    matcher.query(f"{current_path}/examples")
    results_directory = f"{current_path}/results"
    os.makedirs(results_directory , exist_ok=True)
    files = matcher.results
    destination_files = [f"{results_directory}/{item.split('/')[-1]}" for item in files]
    with Pool(10) as executor:
        list(executor.map(copy , files , destination_files))

    
    
    