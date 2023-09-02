questions = {
    "Question 1": {
        "question": "How much is 3 * 2 ?",
        "answer": {"a": "2", "b": "4", "c": "6"},
        "correct": "c"
    },
    "Question 2": {
        "question": "How much is 5 * 2 ?",
        "answer": {"a": "8", "b": "10", "c": "15"},
        "correct": "b"
    }
}

correct_answer = 0
percent_correct = 0
for k, v in questions.items():
    print(f'{k}: {v["question"]}')
    print('Choose the options above!')
    for rk, rv in v['answer'].items():
        print(f'Options: {rk} - {rv} ')
    user_answer = input('Type the answer: ')
    
    if user_answer == v['correct']:
        print(f'The answer was correct')
        correct_answer += 1
    else:
        print(f'The answer incorrectly!')
    percent_correct = correct_answer / len(questions) * 100
    
    print(f'-'*100)
    print(f'Number of correct answers: {correct_answer}')
    print(f'Percentage of correct answers: {percent_correct} %')
    
    if percent_correct >= 80:
        print(f'Score was more 80%, level is Expert!')
    elif percent_correct >= 50:
        print(f'Score was less 60%, level is Beginner!')