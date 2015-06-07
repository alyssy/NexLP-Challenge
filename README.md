# NexLP-Challenge
Tool to detect emotions in emails

LexHacks 2015 - Legal Hackathon - NexLP Challenge - 6/6/2015-6/7/2015
=======================================================================
Developers: A. Romeo & S. Romeo

Software Licensing
---------------------------
Copyright 2015 A. Romeo & S. Romeo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Tool Description
---------------------------
A basic Python script that identifies different classes of emotions in text-based inputs (targeted for emails). The current predefined emotion classes are Happy, Sad, Angry, Irritated, and Appreciative.

Implementation
---------------------------
=> This tool uses a hash table to match words and phrases from the email to a predefined class
=> This tool can currently only track phrases up to length 2, though this is easy to extend
=> This tool can currently only store 1000 words/phrases per class, though this is also easy to extend
=> This tool can currently only track five predefined emotion classes, though this too is easy to extend
=> This tool uses heuristics: it uses words that we think belong in each class; no research has been done to conclude that these are the best subset, and refining these (adding/subtracting words & phrases) can lead to more accurate results

To Run
---------------------------
=> from the command line:
	python NexLP.py file_1.txt
=> the file can contain one email or multiple emails deliminated by ########NEXTEMAIL##########
=> output is a list of emotions followed by a newline then the line number of the ########NEXTEMAIL########## that directly follows the given email
=> example
	INPUT:
	Thanks for your consideration.  I look forward to hearing from you tomorrow...

	Sherri :-)
	########NEXTEMAIL##########
	Attached is the weekly status report regarding ENA Litigation.

	OUTPUT:
	appreciative
	4
=> if there is no emotion in the email, nothing is printed and the algorithm continues


Limitations and Future Additions
---------------------------
=> This tool does not detect sarcasm! Many humans can't detect sarcasm, so we figured this tool shouldn't either :P
=> As mentioned above, the best areas for improvement would be extending the following features: tracking longer phrases, tracking more emotions, tracking more targeted words/phrases, storing more words/phrases



