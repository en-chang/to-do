from datetime import datetime
import random

# All activities
activities = [
    'Morning Routine',
    'Interview Questions',
    'Dudoku',
    'Videos',
    'Church',
    'Lunch',
    'Piano practice',
    'Bass practice',
    'Vocals practice',
    'Writing',
    'Dinner',
    'Coding',
    'Recording'
]

# Add activities to everyday
sun = [x for x in activities if x != 'Dudoku' and x!= 'Videos' and x != 'Coding' and x != 'Recording']
mon = tue = wed = thu = fri = [
    x for x in activities if x != 'Church'
]
sat = [x for x in activities if x!= 'Church' and x != 'Coding']

# Dictionary of schedules
data = {
    'Sunday': sun,
    'Monday': mon,
    'Tuesday': tue,
    'Wednesday': wed,
    'Thursday': thu,
    'Friday': fri,
    'Saturday': sat
}

def warmUpKeyPicker(warmUp):
    if warmUp == 'Chords':
        print(f'        {warmUp}:')
        print(f'            {randomKey()} Major')
        print(f'            Progression {random.randint(1, 44)}')
    else:
        print(f'        {warmUp}:')
        print(f'            {randomKey()} Major')
        print(f'            {randomKey()} Minor')

def randomKey():
    keys = [
        'Ab',
        'A',
        'Bb',
        'B',
        'C',
        'Db',
        'D',
        'Eb',
        'E',
        'F',
        'F#',
        'G'
    ]
    randomKey = random.choice(keys)
    return randomKey

def pianoWarmUpGenerator():
    warmUpKeyPicker('Scales')
    warmUpKeyPicker('Arpeggios')
    warmUpKeyPicker('Chords')
    fingering = ['1 2 3', '3 4 5']
    randomFingering = random.choice(fingering)
    print('        Chromatics:')
    print(f'            {randomFingering}')

def main():
    today = datetime.today().strftime('%A')
    tasks = data[today]
    status = []

    print('\nHello Master!\n\nHere is your list of tasks to complete today:')
    for task in tasks:
        print('   ', task)
        if task == 'Piano practice':
            pianoWarmUpGenerator()
    print()

    print('Enter "y" or "n" for the tasks you completed.')
    for task in tasks:
        while True:
            taskStatus = input(f'    {task}: ')
            if taskStatus == 'y' or taskStatus == 'n':
                status.append(taskStatus)
                break
    
    completionPercent = status.count('y') / len(status) * 100
    print(f'\nYou completed {int(round(completionPercent))}% of your tasks today.')

if __name__ == "__main__":
    main()