

1 of 1
(no subject)

Linh Nguyen <linhnguyen_1609@yahoo.com>
Attachments
4:41 PM (1 minute ago)
to me



Linh Nguyen
Attachments area

""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO
import operator

# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}


# Helper functions

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []

    if value not in key_to_values[key]:
        key_to_values[key].append(value)


# Required functions

def getName(nameStr):
    names = nameStr.split(',')
    return names[1].strip() + ' ' + names[0].strip()


def readOne(all_profiles):
    P2F={}
    P2C={}
    tup=()
    count=1
    person_name="";
    friends=[]
    clubs=[]

    #reading all profile one by one
    for profile in all_profiles:

        #reading all line in each profile one by one
        for line in profile:

            #check wether its a person name or club name
            #if its first line its person name
            if("," in line and count==1):
                person_name=getName(line)

            #else its friend name
            elif ("," in line and count>1):
                friends.append(getName(line))

            #otherwise its club name
            else:
                clubs.append(line)

            count=count+1

        count=1

        #checking if person does not have friend will not be included into P2F
        if(friends!=[]):
            P2F[person_name]=friends
            friends=[]

        #checking if person does not have club will not be included into P2C
        if(clubs!=[]):
            P2C[person_name]=clubs
            clubs=[]

    #return tuple
    return (P2F,P2C)

def load_profiles(file):
    all_profiles=[]
    lines=[]

    #reading whole file
    #storing into list of lists
    line = file.readline()
    while(line):
        if(line=="\n"):
            all_profiles.append(lines)
            lines=[]
        else:
            line=line.strip('\n')
            lines.append(line)
        line = file.readline()

    #separating and making tuple
    #calling function defined above
    tup=readOne(all_profiles)
    return tup


def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    """

    total_clubs = 0
    total_person = 0
    for person in person_to_clubs :
        total_person += 1
        clubs = person_to_clubs[person]
        total_clubs += len(clubs)
    if total_person > 0:
        return (float(total_clubs)/total_person)
    else:
        return 0



def get_last_to_first(P2F: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    """

    lastnames = []
    firstnames = []
    for name, list in P2F.items():
        nm = name.split(' ')
        fn = ''
        for i in range(len(nm)-1):
            fn += nm[i]
        if(fn not in firstnames):
            firstnames.append(fn)
            lastnames.append(nm[-1])
        for n in list:
            nm = n.split(' ')
            fn = ''
            for i in range(len(nm)-1):
                fn += nm[i]
            if(fn in firstnames): continue
            firstnames.append(fn)
            lastnames.append(nm[-1])
    for i in range(len(lastnames)):
        if(lastnames[i] in ans):
            ans[lastnames[i]].append(firstnames[i])

        else:
            ans[lastnames[i]] = []
            ans[lastnames[i]].append(firstnames[i])
    for list in ans.values():
        list.sort()
        #print(list)
    #print(ans)
    return ans
    #pass  # Remove me when you've implemented this function

def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    """
    result = {}
    for key in key_to_value:
        for val in key_to_value[key]:
            if val not in result:
                result[val] = []
            result[val].append(key)
    for key in result:
        result[key].sort()
    return result
   # pass  # Remove me when you've implemented this function


def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person_str: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    """

    club_lst = []
    if person_str in person_to_friends:
        friends = person_to_friends[person_str]
    else:
        friends = []

    if person_str in person_to_clubs:
        person_clubs = person_to_clubs[person_str]
    else:
        person_clubs = []

    for friend in friends:
        if friend in person_to_clubs:
            friend_clubs = person_to_clubs[friend]
            for club in friend_clubs:
                if club not in person_clubs:
                    club_lst.append(club)
    club_lst.sort()
    return club_lst # return the list


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3!=[]
def recommend_clubs(person_to_friends,person_to_clubs,person):
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    """
    #dictionary
    Score_club={}
    #list of tuple
    Score_club_tuple_list=[]

    #list for common people
    common_people=[]

    #finding friend of person
    Friends_List=person_to_friends[person]


    #finding people having common clubs with person but are not friend with person
    clubs_to_person=invert_and_sort(person_to_clubs)
    if(person in person_to_clubs):
        person_clubs=person_to_clubs[person]

        for person_club in person_clubs:

            for p in clubs_to_person[person_club]:
                if(p not in common_people and p!=person and p not in Friends_List):
                    common_people.append(p)
    #end common person


    #checking friend clubs for recommendation point
    for friend in Friends_List:

        if friend in person_to_clubs:
            Clubs_list=person_to_clubs[friend]
            for club in Clubs_list:

                if(person in person_to_clubs and club in person_to_clubs[person]):
                    continue
                if(club in Score_club):
                    Score_club[club]=Score_club[club]+1
                else:
                    Score_club[club]=1


                #if friend and person are having more common clubs increase one more point
                clubs_to_person=invert_and_sort(person_to_clubs)
                person_list=clubs_to_person[club]
                if(friend in person_list and person in person_to_clubs and intersection(person_to_clubs[person],person_to_clubs[friend])):
                    if(club in Score_club):
                        Score_club[club]=Score_club[club]+1
                    else:
                        Score_club[club]=1

    #adding clubs point for common people clubs
    for friend in common_people:
        if friend in person_to_clubs:
            Clubs_list=person_to_clubs[friend]
            for club in Clubs_list:
                if(club in person_to_clubs[person]):
                    continue
                if(club in Score_club):
                    Score_club[club]=Score_club[club]+1
                else:
                    Score_club[club]=1
    for key in Score_club:
        tup=(key,Score_club[key])
        Score_club_tuple_list.append(tup)

    Score_club_tuple_list.sort(key = operator.itemgetter(1),reverse = True)
    return Score_club_tuple_list



if __name__ == '__main__':
    print(recommend_clubs(P2F, P2C, 'Stephanie J Tanner',))
    #pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()