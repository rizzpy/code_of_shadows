# Choose Your Own Adventure
# Object-oriented Template Project
# Creates Story Node Instances
# map a branching story from reading a csv file
# Supports multi-line story nodes, branching multi choices, terminal nodes
import time
import csv

class Node:
    # initialize with a story_nose row which has 
    # an int id or row number 
    # a string for the title
    # string array which 
    # an array of ints representing next story node ids 
    # a boolean indicating whether this is a terminal node - the story ends
    def __init__(self, story_node):
        self.id = story_node['id']
        self.title = story_node['story_title']
        self.story = story_node['story_array'].split(':')
        self.choices = story_node['choices_array'].split(':')
        if story_node['is_End'] == 'False':
            self.end = False
        else:
            self.end = True

    def display(self):
        print('------------------------')
        print(self.title)
        print('------------------------')
        for line in self.story:
            print(line)
            time.sleep(2)
        if self.end:
            print('The End')
            return -1
        print('CHOOSE:')
        choice_num = 1
        for choice in self.choices:
            print(f'{choice_num}: {choice}')
            choice_num+=1
        return int(input('Enter Your Choice: '))

# Load Story file into story_array 
story_array = []
with open('story.csv', newline="") as story_csv:
    story_reader = csv.DictReader(story_csv)
    for row in story_reader:
        story_array.append(row)

# Main Loop
# Traverse story based on choices
# Ends when a terminal node is reached
current_node = 0
while current_node >= 0:
    story = Node(story_array[current_node])
    current_node = story.display()
