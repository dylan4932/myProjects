def equalFrequency(word):
        """
        :type word: str
        :rtype: bool
        """
        counts = dict()
        for i in word:
            counts[i] = counts.get(i, 0) + 1
        return set(counts.values())
    
