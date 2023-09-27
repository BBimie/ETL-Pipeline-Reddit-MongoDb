from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

class SentimentAnalysis:
    def __init__(self, submission) -> None:
        self.sia = SentimentIntensityAnalyzer()
        self.submission = submission

    def clean_submission(self) -> str:
        """ 
        Clean submission text, remove special characters and emojis.

        This function takes the 'submission' attribute of an object and performs text cleaning by
        removing URLs, special characters, and emojis.

        Returns:
            str: Cleaned text without URLs, special characters, and emojis.
        """
        text = re.sub("http[s]?\://\S+","",self.submission)
        text = re.sub('[)(#$]', ' ', text)
        emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F700-\U0001F77F"  # alchemical symbols
                           u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                           u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                           u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                           u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                           u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                           u"\U0001F004-\U0001F0CF"  # CJK Compatibility Ideographs
                           u"\U0001F170-\U0001F251"  # Enclosed Ideographic Supplement
                           u"\U0001F004-\U0001F251"
                           u"\U00002000-\U0000206F"  # general punctuation
                           u"\U00002500-\U00002BEF"  # chinese char
                           u"\U00002702-\U000027B0"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           u"\u2640-\u2642"
                           u"\u2600-\u2B55"
                           u"\u200d"
                           u"\u23cf"
                           u"\u23e9"
                           u"\u231a"
                           u"\ufe0f"  # dingbats
                           u"\u3030"
                           "]+", flags=re.UNICODE)
        text = emoji_pattern.sub(r'', text)
        return text

    def get_scores(self) -> dict:
        """
        This method utilizes a Sentiment Analyzer (the 'sia' object) to analyze the sentiment
        of the cleaned submission text (using the 'clean_submission()' method) and retrieves polarity scores
        for positive, neutral, and negative sentiment.

        Returns:
            polarity: A dictionary containing polarity scores, including 'neg' (negative), 'neu' (neutral),
                'pos' (positive), and 'compound' (compound sentiment).
        """
        polarity = self.sia.polarity_scores(self.clean_submission())
        return polarity
    
    def label_sentiment(self) -> dict:
        """
        Label sentiment based on polarity scores.

        This function calculates a sentiment label based on polarity scores obtained using the 'get_scores()' method.
        It assigns a sentiment label of 'positive' if the 'compound' polarity score is greater than 0.05, 'negative'
        if it's less than -0.05, and 'neutral' otherwise. The sentiment label is added to the polarity dictionary.

        Returns:
        polrity: A dictionary containing polarity scores ('neg', 'neu', 'pos', 'compound') and a 'label' indicating
                the sentiment label ('positive', 'negative', or 'neutral').
        """
        polarity = self.get_scores()

        if polarity['compound'] > 0.05:
            label = 'positive'
        elif polarity['compound'] < -0.05:
            label = 'negative'
        else:
            label = 'neutral'
        polarity['label'] = label

        return polarity