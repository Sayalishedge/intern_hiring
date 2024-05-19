# intern_hiring
Problem Statement : 
 For hiring an intern, the recruiter starts gathering a list of interns from its database.
 In order to keep the hiring pipeline healthy, every time a recruiter calls up a candidate to schedule an interview, he also asks the candidate to provide a list of 
 his classmates.
 List all the candidates that could be contacted by the above method, until a candidate is hired or the complete list of candidates along with their classmates is 
 exhausted.
 Note: No candidate should be contacted more than once.
Approach : BFS(Breadth First Search)
  Python implementation to find all the eligible candidates in the list using BFS.
  
  assignment.py : 
  1] Friendship dictionary : Friends of the candidates where the key is candidate and value is the list of friends.
  2] def friends(ip): This function finds all the candidates who have given candidate (ip) as a friend.
  3] def find(ip) : Starts the search from the given candidate(ip). Performs BFS and returns a list of all contacted candidates including itself and it's friends.         This function adds initial friends to the queue i.e friends from the def friends() function, and iteratively explores each friend's friend for the same until         all the candidates are contacted.

  test.py : 
  This python file checks the assignment.py for some testcases.
  For testing, imported the unittest module and the find function
  
  
  

