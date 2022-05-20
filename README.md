# Next-Word-Prediction

This is an updated version of the next-word prediction model found at https://thecleverprogrammer.com/2021/01/19/next-word-prediction-with-python/

In this model, I updated the code to give the output sentence with the next predicted word along with a list of alternative words for that position. I also included a "secondary" selection, whereby the next next word is calculated using the sentence with its predicted next word as the input. This, likewise, contains a list of potential words along with it. This is done again for a tertiary selection; I stop after this since the prediction has accumulated a lot of error by that point. The input data is "Metamorphosis" by Franz Kafka, making the predicted sentences similar to common sentences/phrases found in the text.

An interesting note: this model works with other languages as well; any language that uses spaces between words should be able to work, assuming the input text is in that language.

Example: input text "he will take"

Primary suggestion: "he will take sides"

Secondary suggestoin: "he will take sides against"

Tertiary suggestion: "he will take sides against the"

Other primary suggestions:  ['it', 'now,', 'her', 'his', 'him', 'all', 'some', 'their', 'over', 'a', 'long']

Other secondary suggestions:  ['against']

Other tertiary suggestions:  ['the', 'each', 'it', 'his', 'me', 'it.', 'him', 'its', "Gregor's", 'her', 'accepting']
