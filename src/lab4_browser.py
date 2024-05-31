#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program: Web url browser simulator
#
# Author: Sebastian
#----------------------------------------------------

def getAction():
    '''
    Asks the user for an input then returns the input if it's one of the valid inputs
    Inputs: NONE
    Returns: a string character, either = < > q
    '''
    action = input("Please enter; = to go to a new website; < to go back; > to go forward; or q to quit: ")
    while not action in "=<>q":
        action = input("Please enter; = to go to a new website; < to go back; > to go forward; or q to quit: ")
    return action

def goToNewSite(current, pages):
    '''
    Takes a user input and goes to that page, clearing any pages in front of it making the new page the last page in the list
    Inputs: current index and a list of web pages
    Returns: the index of the newly added page
    not returned but also updates the list to include the new url
    '''   
    site = input("Please enter the desired url: ")
    
    for i in range(len(pages)-1, current, -1): #iterates from the end to the entry 1 before the current page
        pages.pop(i) 
    pages.insert(current+1, site)
    index = current +1
    
    return index

    
def goBack(current, pages):
    '''
    Takes and index and returns the previous index in the list
    Inputs: Index and list of  web pages
    Returns: index of the previous page or current page if index oob
    '''    
    index = current - 1
    if index < 0 :
        print("Error, cannot go back")
        return current
    return index

def goForward(current, pages):
    '''
    Takes and index and returns the next index in the list
    Inputs: Index and list of  web pages
    Returns: index of the next page or current page if index oob
    '''    
    index = current + 1
    if index >= len(pages) :
        print("Error, cannot go forward")
        return current
    return index



def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    