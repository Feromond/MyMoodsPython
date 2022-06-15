class MoodVariants:

    def __init__(self):
        self.MoodVariations = {
            "OverallMood" : ["Sad", "Unhappy", "Under The Weather", "Neutral", "Okay", "Pretty Good", "Good", "Excellent", "Perfect"],
            "Socially" : ["Want To Be Isolated", "Be With One Close Person", "Okay With Seeing Anyone", "Want To Party With Everyone"],
            "Introspectively" : ["Don't Like Myself Today", "Not The Happiest With Myself", "Fine With Myself", "Content with Myself"]
        }

    def getMoodVariations(self):
        # Return the values to each key in MoodVariations
        return list(self.MoodVariations.values())
    
    def getMoodNames(self):
        return list(self.MoodVariations.keys())


test = MoodVariants()

print(test.getMoodVariations())