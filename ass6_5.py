text = "X-DSPAM-Confidence:    0.8475";
t = text.find("0")
h = text[t:t+6]
h = float(h)
print h
