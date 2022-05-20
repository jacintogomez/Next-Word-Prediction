# Next-Word-Prediction

This is an updated version of the next-word prediction model found at https://thecleverprogrammer.com/2021/01/19/next-word-prediction-with-python/

In this model, I updated the code to give the output sentence with the next predicted word along with a list of alternative words for that position. I also included a "secondary" selection, whereby the next next word is calculated using the sentence with its predicted next word as the input. This, likewise, contains a list of potential words along with it. This is done again for a tertiary selection; I stop after this since the prediction has accumulated a lot of error by that point. 

The input data is "Metamorphosis" by Franz Kafka, making the predicted sentences bias toward common sentences/phrases found in the text

example: input text "Let's go to"
Primary suggestion: "Let's go to cover"
Secondary suggestoin: "Let's go to cover it"
Tertiary suggestion: "Let's go to cover it away"
