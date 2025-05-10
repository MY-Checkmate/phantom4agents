import os
import sys
from core.command_processor import CommandProcessor

def main():
    print('Welcome to your Multi-Purpose AI Assistant!')
    print('Type ''help'' to see available commands or ''exit'' to quit.')
    processor = CommandProcessor()

    while True:
        command = input('\n> ').strip()
        if command.lower() == 'exit':
            print('Goodbye!')
            break
        elif command.lower() == 'help':
            print('Available commands:')
            print('- scrape [url] : Scrape data from a URL.')
            print('- scan [ip] : Perform a network scan.')
            print('- automate [task] : Run an automation task.')
        else:
            response = processor.process(command)
            print(response)

if __name__ == '__main__':
    main()
