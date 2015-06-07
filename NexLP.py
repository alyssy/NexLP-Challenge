#############################################################################
#	Copyright 2015 A. Romeo & S. Romeo
#
#	Licensed under the Apache License, Version 2.0 (the "License");
#	you may not use this file except in compliance with the License.
#	You may obtain a copy of the License at
#
#   	 http://www.apache.org/licenses/LICENSE-2.0
#
#	Unless required by applicable law or agreed to in writing, software
#	distributed under the License is distributed on an "AS IS" BASIS,
#	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	See the License for the specific language governing permissions and
#	limitations under the License.
#############################################################################



import string
import sys

# create hash table

ID = {}

# happy words
ID["happy"] = 1000
ID["woo"] = 1001
ID["excite"] = 1002
ID["excited"] = 1003
ID["beautiful"] = 1004
ID["nice"] = 1005
ID["sweet"] = 1006
ID["proud"] = 1007
ID["kind"] = 1008
ID["relieved"] = 1009
ID["hope"] = 1010
ID["faith"] = 1011
ID["optimistic"] = 1012
ID["love"] = 1013
ID["understanding"] = 1014
ID["amazing"] = 1015
ID["great"] = 1016
ID["lucky"] = 1017
ID["fortunately"] = 1018
ID["cheers"] = 1019
ID["cheerful"] = 1020
ID["playful"] = 1021
ID["support"] = 1022
ID["silly"] = 1023
ID["accomplish"] = 1024
ID["accomplished"] = 1025
ID["accomplishment"] = 1026
ID["accomplishments"] = 1027
ID["appreciate"] = 1028
ID["appreciated"] = 1029
ID["better place"] = 1030
ID["thank you"] = 1031
ID["acceptable"] = 1032
ID["accepting"] = 1033
ID["joy"] = 1034
ID["content"] = 1035
ID["cheery"] = 1036
ID["terrific"] = 1037
ID["jovial"] = 1038
ID["dazzling"] = 1039
ID["dazzled"] = 1040
ID["charming"] = 1041
ID["lovely"] = 1042
ID["friendly"] = 1043
ID["congrats"] = 1044
ID["congratulations"] = 1045
ID["look forward"] = 1046
ID["adorable"] = 1047
ID["howdy"] = 1048
ID["birthday"] = 1049
ID["party"] = 1050
ID["humor"] = 1051
ID["funny"] = 1052
ID["honors"] = 1053
ID["honor"] = 1054
ID["honored"] = 1055
ID["pleased"] = 1056
ID["play"] = 1057
ID["good game"] = 1058
ID["surprise"] = 1059
ID["generous"] = 1060
ID["generosity"] = 1061
ID["greetings"] = 1062
ID["good work"] = 1063
ID["good job"] = 1064
ID["friend"] = 1065
ID["take care"] = 1066

# sad words
ID["boo"] = 2000
ID["sad"] = 2001
ID["moody"] = 2002
ID["embarrassed"] = 2003
ID["hurt"] = 2004
ID["hurts"] = 2005
ID["wrong"] = 2006
ID["hurtful"] = 2007
ID["sorry"] = 2008
ID["regret"] = 2009
ID["fear"] = 2010
ID["fearful"] = 2011
ID["gloomy"] = 2012
ID["grief"] = 2013
ID["glum"] = 2014
ID["depressed"] = 2015
ID["depressing"] = 2016
ID["heart broken"] = 2017
ID["heartbroken"] = 2018
ID["guilty"] = 2019
ID["sry"] = 2020
ID["scared"] = 2021
ID["overwhelmed"] = 2022
ID["layoff"] = 2023
ID["layoffs"] = 2024
ID["lay off"] = 2025
ID["laid off"] = 2026
ID["lay offs"] = 2027
ID["tough"] = 2028
ID["bankruptcy"] = 2029
ID["not good"] = 2030
ID["dragging"] = 2031
ID["drags out"] = 2032
ID["unfortunately"] = 2033
ID["poor"] = 2034
ID["miss"] = 2035
ID["missed"] = 2036

# angry words
ID["bad"] = 3000
ID["calm down"] = 3001
ID["angry"] = 3002
ID["upset"] = 3003
ID["horrible"] = 3004
ID["disgusting"] = 3005
ID["unbelievable"] = 3006
ID["stupid"] = 3007
ID["ugly"] = 3008
ID["dumb"] = 3009
ID["foolish"] = 3010
ID["evil"] = 3011
ID["jerk"] = 3012
ID["mean"] = 3013
ID["unacceptable"] = 3014
ID["furious"] = 3015
ID["fury"] = 3016
ID["incompetent"] = 3017
ID["not competent"] = 3018
ID["dislike"] = 3019
ID["jealous"] = 3020
ID["me nuts"] = 3021
ID["going nuts"] = 3022
ID["dont trust"] = 3023
ID["not trust"] = 3024
ID["pathetic"] = 3025
ID["offensive"] = 3026
ID["spiteful"] = 3027
ID["irresponsible"] = 3028
ID["not responsible"] = 3029
ID["malice"] = 3030
ID["rotten"] = 3031
ID["robbed"] = 3032
ID["rejected"] = 3033
ID["rejecting"] = 3034
ID["vicious"] = 3035
ID["upset"] = 3036
ID["upsetting"] = 3037
ID["upsets"] = 3038
ID["infuriates"] = 3039
ID["infuriated"] = 3040
ID["infuriating"] = 3041
ID["insults"] = 3042
ID["insult"] = 3043
ID["insulted"] = 3044
ID["insulting"] = 3045
ID["perturbs"] = 3046
ID["bothers"] = 3047
ID["bothered"] = 3048
ID["bothering"] = 3049
ID["annoyed"] = 3050
ID["annoys"] = 3051
ID["annoying"] = 3052
ID["frustrated"] = 3053
ID["frustrating"] = 3054
ID["frustrates"] = 3055
ID["enrages"] = 3056
ID["aggravated"] = 3057
ID["aggravates"] = 3058
ID["aggravating"] = 3059
ID["blackmail"] = 3060
ID["blackmailing"] = 3061
ID["blackmails"] = 3062
ID["cranky"] = 3063
ID["ashamed"] = 3064
ID["crabby"] = 3065
ID["confrontation"] = 3066
ID["confronted"] = 3067
ID["confronting"] = 3068
ID["liar"] = 3069
ID["lying"] = 3070
ID["lies"] = 3071
ID["cut off"] = 3072
ID["cuts off"] = 3073
ID["fault"] = 3074
ID["faults"] = 3075
ID["dont care"] = 3076
ID["not care"] = 3077
ID["bad game"] = 3078

# uncomfortable/irritated words
ID["sick"] = 4000
ID["tired"] = 4001
ID["weak"] = 4002
ID["nervous"] = 4003
ID["pessimistic"] = 4004
ID["pessimism"] = 4005
ID["nervous"] = 4006
ID["problem"] = 4007
ID["important"] = 4008
ID["stern"] = 4009
ID["must"] = 4010
ID["needy"] = 4011
ID["mistrust"] = 4012
ID["stressed"] = 4013
ID["critical"] = 4014
ID["damage"] = 4015
ID["damaged"] = 4016
ID["criticized"] = 4017
ID["criticizing"] = 4018
ID["dehumanizing"] = 4019
ID["bitter"] = 4020
ID["dangerous"] = 4021
ID["disappointing"] = 4022
ID["disappointed"] = 4023
ID["disappoints"] = 4024
ID["anxious"] = 4025
ID["anxiety"] = 4026
ID["careless"] = 4027
ID["coward"] = 4028
ID["disrespecting"] = 4029
ID["disrespectful"] = 4030
ID["confused"] = 4031
ID["productive collaboration"] = 4032
ID["please respond"] = 4033
ID["restart"] = 4034
ID["confusion"] = 4035
ID["confusing"] = 4036
ID["confuses"] = 4037
ID["not working"] = 4038
ID["future reference"] = 4039
ID["urgent"] = 4040
ID["misunderstanding"] = 4041
ID["convey"] = 4042
ID["just kidding"] = 4043
ID["no further"] = 4044

# appreciative
ID["thank you"] = 5000
ID["thanks"] = 5001
ID["thank"] = 5002
ID["appreciated"] = 5003
ID["appreciate"] = 5004
ID["grateful"] = 5005
ID["dedication"] = 5006
ID["admire"] = 5007
ID["admiration"] = 5008
ID["hero"] = 5009
ID["good luck"] = 5010
ID["support"] = 5011
ID["supportive"] = 5012
ID["joyful"] = 5013
ID["responsible"] = 5014
ID["brave"] = 5015
ID["consideration"] = 5016
ID["considerate"] = 5017
ID["proud"] = 5018
ID["look foward"] = 5019

# return greatest number
def return_greatest(a, b, c, d, e):
    if (a == 0 and b == 0 and c == 0 and d == 0 and e == 0):
        #print 'none'
        return 0
    if (a >= b and a >= c and a >= d and a >= e):
        print 'happy'
        return a
    elif (b >= a and b >= c and b >= d and b >= e):
        print 'sad'
        return b
    elif (c >= a and c >= b and c >= d and c >= e):
        print 'angry'
        return c
    elif (d >= a and d >= b and d >= c and d >= e):
        print 'irritated'
        return d
    elif (e >= a and e >= b and e >= c and e >= d):
        print 'appreciative'
        return e
    else:
        #print 'none'
        return 0


# state vars
happy = 0
sad = 0
angry = 0
irritated = 0
appreciative = 0
noword = 0
linenumber = 0
previous_word = ""

our_file = sys.argv[1] #'file_1.txt'

# read the file
f = open(our_file, 'r')
for line in f:
    linenumber = linenumber + 1
    if '########NEXTEMAIL##########' in line:
        if (return_greatest(happy, sad, angry, irritated, appreciative) != 0):
            print linenumber
        happy = 0
        sad = 0
        angry = 0
        irritated = 0
        appreciative = 0
        noword = 0
        previous_word = ""
        
    line = line.translate(string.maketrans("",""), string.punctuation)
    for word in line.split():
        word = word.lower()
        #print word
        try:
            if (word in ID.keys()):
                if (ID[word] >= 1000 and ID[word] < 2000):
                    happy = happy + 1
                elif (ID[word] >= 2000 and ID[word] < 3000):
                    sad = sad + 1
                elif (ID[word] >= 3000 and ID[word] < 4000):
                    angry = angry + 1
                elif (ID[word] >= 4000 and ID[word] < 5000):
                    irritated = irritated + 1
                elif (ID[word] >= 5000 and ID[word] < 6000):
                    appreciative = appreciative + 1
                elif (ID[previous_word + "" + word] >= 1000 and ID[previous_word + "" + word] < 2000):
                    happy = happy + 1
                elif (ID[previous_word + "" + word] >= 2000 and ID[previous_word + "" + word] < 3000):
                    sad = sad + 1
                elif (ID[previous_word + "" + word] >= 3000 and ID[previous_word + "" + word] < 4000):
                    angry = angry + 1
                elif (ID[previous_word + "" + word] >= 4000 and ID[previous_word + "" + word] < 5000):
                    appreciative = appreciative + 1
            else:
                noword = noword + 1
            
            previous_word = word
        except ValueError:
            continue
        
return_greatest(happy, sad, angry, irritated, appreciative)
            


# TODO: check for emoticons, !, caps



