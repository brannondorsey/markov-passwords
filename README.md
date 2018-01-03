# Markov-chain password generator

Generate statistically-likely passwords using a character-level markov generator trained on the RockYou password leak.

## Download Training Data

```bash
# download the rockyou training data
# contains 80% of the full rockyou passwords (with repeats)
# that are 10 characters or less
curl -L -o data/train.txt https://github.com/brannondorsey/PassGAN/releases/download/data/rockyou-train.txt
```

Train using `train.py` and generate passwords using `sample.py`. One day maybe I'll come back and add command-line args (**PR wanted ;)**), but for now edit either of those files to change defaults.
