from prompt_toolkit import prompt

if '__main__' in __name__:
    answer = prompt('Lookup a Wikipedia entry:')
    print(f'Searching for {answer}')
