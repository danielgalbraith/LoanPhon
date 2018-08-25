# LoanPhon

A script written in Python 3 for adapting loanwords to a predefined phonology.

This sample script has the following features:

* Takes as input a .txt file with XSAMPA phoneme representation, where each phoneme is followed by '.', and newline character follows each input word
* Predefined input languages: English, French, Spanish, German
* Sample output language phoneme inventory: /a e i o u m n ŋ ɲ p t k ʔ b d g f s z ʃ h tʃ l r j w/
* Sample output language syllable structure: (C)V(C) with possible onsets /m n ɲ p t k ʔ b d g f s z ʃ h tʃ l r j w/ and possible codas /m n ŋ p t k s l r j w/
* Predefined ruleset for loanword adaptation: can be changed to suit desired output language phonology
* Output file format: .txt with '.'-separated XSAMPA phoneme representation, each word followed by newline character
