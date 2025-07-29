import yaml
import sys

def load_scores():
    with open("score.yaml", "r") as file:
        return yaml.safe_load(file)  # Load the YAML file contents
    

DATA = load_scores()  # Load the YAML data
    
def average(subject):

    """"""
    score_linux = DATA['scores'][subject]
    #length = len(score_linux)
    #total = sum(score_linux.values())
    #return total / length if length > 0 else 0
    scores = [score_linux[student] for student in score_linux.keys() 
              if score_linux[student] is not None]
    print(f"Scores in {subject}:", scores)
    
    return sum(scores) / len(scores) if scores else 0

def is_passed(student, threshold=60):
    scores = []
    for score in DATA['scores'].values():
        if score is not None:
            s = score.get(student, None)
            if s is not None:
                scores.append(s)
    print(scores)
    # Return True if student passed all subjects, False otherwise
    return all(s >= threshold for s in scores) if scores else False
    


if __name__ == "__main__":
    print("Average score in Linux:", average('linux'))
    print("Passed students in Linux:", is_passed('Cuong'))