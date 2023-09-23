from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re

class SentimentAnalysis:
    def __init__(self, submission) -> None:
        self.sia = SentimentIntensityAnalyzer()
        self.submission = submission

    def clean_submission(self):
        """ Clean submission text, remove special characters and emojis """
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

    def get_scores(self):
        """ Get all polarity scores from the Sentiment analyzer """
        polarity = self.sia.polarity_scores(self.clean_submission())
        return polarity
    
    def label_sentiment(self):
        """Label submission sentiment using the compound score
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