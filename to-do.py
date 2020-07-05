from datetime import datetime

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
    'Recording',
    'Walking'
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

def main():
    today = datetime.today().strftime('%A')
    tasks = data[today]
    status = []

    print('\nHello Master!\n\nHere is your list of tasks to complete today:')
    for task in tasks:
        print('   ', task)
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