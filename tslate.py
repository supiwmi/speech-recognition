#!/usr/bin/env python3

import goslate

text = "Hello World"

gs = goslate.Goslate()
# translatedText = gs.translate(text,'fr')
translatedText = gs.translate(text, "ja")

print(translatedText)
