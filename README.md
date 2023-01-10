# Sentence-Shuffler
HOLD ON THERE JETHRO!!! Please read this document first.

This program shuffles the text of multiple sentences within a text file, and pastes the shuffled text into a separate document.

This application is useful for language teachers wanting to quickly make a large document of randomized word sorting problems. These types of problems will help language learners become more familiar with specific grammar structures. 

For example: A text document can be filled with sentences such as "I really like cats." and may be shuffled into "really / cats. / like / I"

Afterwards, a teacher can take the randomly shuffled sentences and print them on paper, and have 
students try reorganizing the words back into the correct order.

I love making this activity for students, but I realized that shuffling sentences manually is very annoying and can take hours if I am working with a long list of sentences to shuffle. This program can do the same thing within a few seconds.

How to use:

In order to use this program, you can easily download this file as a zip.
If you want to see the original code, please look at the dev branch of this repository.

Once downloaded, open the downloaded folder and open dist, then main. Write your sentences in the 'sentences.txt' file.

*NOTE* You can also make sure that two or more words are always side-by-side within the shuffled 
sentences by connecting multiple words with the "+" symbol.

*ANOTHER NOTE* This program utilizes utf-8 so it should work with text from all languages. Create an issue or let me know if text from some languages do not work (or if you experience any other problems for that matter).

After you are finished creating your sentences in the text document, save your work. Then you can run the "main" application within the same folder
and it will generate your shuffled sentences inside of the "shuffled.txt" document.

Below is an example of the input sentences, and output shuffled sentences:


***Here is the input:

I have+been working+at McDonalds+for 5 years.<br />
Cody has+been sleeping+for 3 hours.<br />
Rusty has+been to New+York.<br />
Jake has+been fishing+for 6+years.<br />
Bob has+been studying+Japanese for 3 months.<br />
Squidward has+been playing+the+clarinet for 32 years.<br />
Kubota+Sensei has been to Tokyo.<br />

***And here is the output:

McDonalds for / have been / 5 / I / years. / working at / <br />
has been / sleeping for / hours. / 3 / Cody / <br />
to / Rusty / New York. / has been / <br />
has been / Jake / fishing for / 6 years. /<br /> 
months. / Bob / for / 3 / has been / studying Japanese /<br /> 
Squidward / playing the clarinet / has been / 32 / years. / for /<br /> 
been / Tokyo. / Kubota Sensei / has / to / <br />

As you can see, in all of the sentences I write "has+been" or "have+been" instead of "has been" or "have been" because I want the two words to always be next to each other in the randomized sentences since it is the main grammar point used in the lesson I created this program for.
