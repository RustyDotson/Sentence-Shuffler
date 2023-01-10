# Sentence-Shuffler
HOLD ON THERE JETHRO!!! Please read this document first.

Sentence-Shuffler shuffles the text of multiple sentences within a text file, and pastes the shuffled text into a separate document.

This application is useful for language teachers wanting to quickly make a large document of randomized word sorting problems. These types of problems will help language learners become more familiar with specific grammar structures. 

For example: A text document can be filled with sentences such as "I really like cats." and may be shuffled into "/ really / cats. / like / I /"

Afterwards, a teacher can take the randomly shuffled sentences and print them on paper, and have 
students try reorganizing the words back into the correct order.

I love making this activity for students, but I realized that shuffling sentences manually is very annoying and can take hours if I am working with a long list of sentences to shuffle. This program can do the same thing within a few seconds.

How to use:

In order to use this program, you can easily download this file as a zip.
If you want to see the original code, please look at the dev branch of this repository.

This program utilizes pyinstaller so that everything is run through a .exe file instead of requiring a python IDE to run the code.

Once downloaded, open the downloaded folder and open dist, then main. Write your sentences in the 'sentences.txt' file.

*NOTE:* You can also make sure that two or more words are always side-by-side within the shuffled 
sentences by connecting multiple words with the "+" symbol.

*ANOTHER NOTE:* This program utilizes utf-8 so it should work with text from all languages. Create an issue or let me know if text from some languages does not work (or if you experience any other problems for that matter).

*ANOTHER ANOTHER NOTE:* After downloading the zip and running the application, you will receive an alert stating that you are about to run a potentially dangerous program (this is the case for most .exe files). Feel free not to use the .exe file if you don't feel comfortable doing that. The only other way around is by using the dev folder of this repository as described previously (You will likely require a python installation identified as a PATH environment variable). If you don't mind, click the underlined "more info" text and next click "run anyway."

After you are finished creating your sentences in the text document, save your work. Then you can run the "main.exe" application within the same folder
and it will generate your shuffled sentences inside of the "shuffled.txt" document.

After the sentences are generated it is usually a good idea to copy the text from the shuffled document, and paste it into a word document so that the user can customize the font and size of text.

Below is an example of the input sentences, and output shuffled sentences:


***Here is the input:***

I have+been working+at McDonalds+for 5 years.<br />
Cody has+been sleeping+for 3 hours.<br />
Rusty has+been to New+York.<br />
Jake has+been fishing+for 6+years.<br />
Bob has+been studying+Japanese for 3 months.<br />
Squidward has+been playing+the+clarinet for 32 years.<br />
Kubota+Sensei has been to Tokyo.<br />

***And here is the output:***

/ have been / years. / 5 / McDonalds for / working at / I / <br />
/ has been / 3 / sleeping for / Cody / hours. / <br />
/ Rusty / New York. / has been / to / <br />
/ has been / 6 years. / Jake / fishing for / <br />
/ studying Japanese / has been / Bob / for / months. / 3 / <br />
/ 32 / years. / has been / for / Squidward / playing the clarinet / <br />
/ to / Tokyo. / has / Kubota Sensei / been / <br />

As you can see, in all of the sentences "has+been" or "have+been" is written instead of "has been" or "have been" in order for them to always be together in the shuffled sentences.
