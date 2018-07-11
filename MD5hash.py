import hashlib

# This function takes a string and returns the MD5 hash of the string.
def hash(string):
 h = hashlib.md5()
 h.update(bytes(string, "ascii"))
 return h.hexdigest()


# This list contains the 100 most common words in English.
words = ['I', 'a', 'able', 'about', 'above', 'act', 'add', 'afraid', 'after', 'again', 'against', 'age', 'ago', 'agree', 'air', 'all', 'allow', 'also', 'always', 'am', 'among', 'an', 'and', 'anger', 'animal', 'answer', 'any', 'appear', 'apple', 'are', 'area', 'arm', 'arrange', 'arrive', 'art', 'as', 'ask', 'at', 'atom', 'baby', 'back', 'bad', 'ball', 'band', 'bank', 'bar', 'base', 'basic', 'bat', 'be', 'bear', 'beat', 'beauty', 'bed', 'been', 'before', 'began', 'begin', 'behind', 'believe', 'bell', 'best', 'better', 'between', 'big', 'bird', 'bit', 'black', 'block', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'bone', 'book', 'born', 'both', 'bottom', 'bought', 'box', 'boy', 'branch', 'bread', 'break', 'bright', 'bring', 'broad', 'broke', 'brother', 'brought', 'brown', 'build', 'burn', 'busy', 'but', 'buy', 'by', 'call', 'came', 'camp', 'can', 'capital', 'captain', 'car', 'card', 'care', 'carry', 'case', 'cat', 'catch', 'caught', 'cause', 'cell', 'cent', 'center', 'century', 'certain', 'chair', 'chance', 'change', 'character', 'charge', 'chart', 'check', 'chick', 'chief', 'child', 'children', 'choose', 'chord', 'circle', 'city', 'claim', 'class', 'clean', 'clear', 'climb', 'clock', 'close', 'clothe', 'cloud', 'coast', 'coat', 'cold', 'collect', 'colony', 'color', 'column', 'come', 'common', 'company', 'compare', 'complete', 'condition', 'connect', 'consider', 'consonant', 'contain', 'continent', 'continue', 'control', 'cook', 'cool', 'copy', 'corn', 'corner', 'correct', 'cost', 'cotton', 'could', 'count', 'country', 'course', 'cover', 'cow', 'crease', 'create', 'crop', 'cross', 'crowd', 'cry', 'current', 'cut', 'dad', 'dance', 'danger', 'dark', 'day', 'dead', 'deal', 'dear', 'death', 'decide', 'decimal', 'deep', 'degree', 'depend', 'describe', 'desert', 'design', 'determine', 'develop', 'dictionary', 'did', 'die', 'differ', 'difficult', 'direct', 'discuss', 'distant', 'divide', 'division', 'do', 'doctor', 'does', 'dog', 'dollar', "don't", 'done', 'door', 'double', 'down', 'draw', 'dream', 'dress', 'drink', 'drive', 'drop', 'dry', 'duck', 'during', 'each', 'ear', 'early', 'earth', 'ease', 'east', 'eat', 'edge', 'effect', 'egg', 'eight', 'either', 'electric', 'element', 'else', 'end', 'enemy', 'energy', 'engine', 'enough', 'enter', 'equal', 'equate', 'especially', 'even', 'evening', 'event', 'ever', 'every', 'exact', 'example', 'except', 'excite', 'exercise', 'expect', 'experience', 'experiment', 'eye', 'face', 'fact', 'fair', 'fall', 'family', 'famous', 'far', 'farm', 'fast', 'fat', 'father', 'favor', 'fear', 'feed', 'feel', 'feet', 'fell', 'felt', 'few', 'field', 'fig', 'fight', 'figure', 'fill', 'final', 'find', 'fine', 'finger', 'finish', 'fire', 'first', 'fish', 'fit', 'five', 'flat', 'floor', 'flow', 'flower', 'fly', 'follow', 'food', 'foot', 'for', 'force', 'forest', 'form', 'forward', 'found', 'four', 'fraction', 'free', 'fresh', 'friend', 'from', 'front', 'fruit', 'full', 'fun', 'game', 'garden', 'gas', 'gather', 'gave', 'general', 'gentle', 'get', 'girl', 'give', 'glad', 'glass', 'go', 'gold', 'gone', 'good', 'got', 'govern', 'grand', 'grass', 'gray', 'great', 'green', 'grew', 'ground', 'group', 'grow', 'guess', 'guide', 'gun', 'had', 'hair', 'half', 'hand', 'happen', 'happy', 'hard', 'has', 'hat', 'have', 'he', 'head', 'hear', 'heard', 'heart', 'heat', 'heavy', 'held', 'help', 'her', 'here', 'high', 'hill', 'him', 'his', 'history', 'hit', 'hold', 'hole', 'home', 'hope', 'horse', 'hot', 'hot', 'hour', 'house', 'how', 'huge', 'human', 'hundred', 'hunt', 'hurry', 'ice', 'idea', 'if', 'imagine', 'in', 'inch', 'include', 'indicate', 'industry', 'insect', 'instant', 'instrument', 'interest', 'invent', 'iron', 'is', 'island', 'it', 'job', 'join', 'joy', 'jump', 'just', 'keep', 'kept', 'key', 'kill', 'kind', 'king', 'knew', 'know', 'lady', 'lake', 'land', 'language', 'large', 'last', 'late', 'laugh', 'law', 'lay', 'lead', 'learn', 'least', 'leave', 'led', 'left', 'leg', 'length', 'less', 'let', 'letter', 'level', 'lie', 'life', 'lift', 'light', 'like', 'line', 'liquid', 'list', 'listen', 'little', 'live', 'locate', 'log', 'lone', 'long', 'look', 'lost', 'lot', 'loud', 'love', 'low', 'machine', 'made', 'magnet', 'main', 'major', 'make', 'man', 'many', 'map', 'mark', 'market', 'mass', 'master', 'match', 'material', 'matter', 'may', 'me', 'mean', 'meant', 'measure', 'meat', 'meet', 'melody', 'men', 'metal', 'method', 'middle', 'might', 'mile', 'milk', 'million', 'mind', 'mine', 'minute', 'miss', 'mix', 'modern', 'molecule', 'moment', 'money', 'month', 'moon', 'more', 'morning', 'most', 'mother', 'motion', 'mount', 'mountain', 'mouth', 'move', 'much', 'multiply', 'music', 'must', 'my', 'name', 'nation', 'natural', 'nature', 'near', 'necessary', 'neck', 'need', 'neighbor', 'never', 'new', 'next', 'night', 'nine', 'no', 'noise', 'noon', 'nor', 'north', 'nose', 'note', 'nothing', 'notice', 'noun', 'now', 'number', 'numeral', 'object', 'observe', 'occur', 'ocean', 'of', 'off', 'offer', 'office', 'often', 'oh', 'oil', 'old', 'on', 'once', 'one', 'only', 'open', 'operate', 'opposite', 'or', 'order', 'organ', 'original', 'other', 'our', 'out', 'over', 'own', 'oxygen', 'page', 'paint', 'pair', 'paper', 'paragraph', 'parent', 'part', 'particular', 'party', 'pass', 'past', 'path', 'pattern', 'pay', 'people', 'perhaps', 'period', 'person', 'phrase', 'pick', 'picture', 'piece', 'pitch', 'place', 'plain', 'plan', 'plane', 'planet', 'plant', 'play', 'please', 'plural', 'poem', 'point', 'poor', 'populate', 'port', 'pose', 'position', 'possible', 'post', 'pound', 'power', 'practice', 'prepare', 'present', 'press', 'pretty', 'print', 'probable', 'problem', 'process', 'produce', 'product', 'proper', 'property', 'protect', 'prove', 'provide', 'pull', 'push', 'put', 'quart', 'question', 'quick', 'quiet', 'quite', 'quotient', 'race', 'radio', 'rail', 'rain', 'raise', 'ran', 'range', 'rather', 'reach', 'read', 'ready', 'real', 'reason', 'receive', 'record', 'red', 'region', 'remember', 'repeat', 'reply', 'represent', 'require', 'rest', 'result', 'rich', 'ride', 'right', 'ring', 'rise', 'river', 'road', 'rock', 'roll', 'room', 'root', 'rope', 'rose', 'round', 'row', 'rub', 'rule', 'run', 'safe', 'said', 'sail', 'salt', 'same', 'sand', 'sat', 'save', 'saw', 'say', 'scale', 'school', 'science', 'score', 'sea', 'search', 'season', 'seat', 'second', 'section', 'see', 'seed', 'seem', 'segment', 'select', 'self', 'sell', 'send', 'sense', 'sent', 'sentence', 'separate', 'serve', 'set', 'settle', 'seven', 'several', 'shall', 'shape', 'share', 'sharp', 'she', 'sheet', 'shell', 'shine', 'ship', 'shoe', 'shop', 'shore', 'short', 'should', 'shoulder', 'shout', 'show', 'side', 'sight', 'sign', 'silent', 'silver', 'similar', 'simple', 'since', 'sing', 'single', 'sister', 'sit', 'six', 'size', 'skill', 'skin', 'sky', 'slave', 'sleep', 'slip', 'slow', 'small', 'smell', 'smile', 'snow', 'so', 'soft', 'soil', 'soldier', 'solution', 'solve', 'some', 'son', 'song', 'soon', 'sound', 'south', 'space', 'speak', 'special', 'speech', 'speed', 'spell', 'spend', 'spoke', 'spot', 'spread', 'spring', 'square', 'stand', 'star', 'start', 'state', 'station', 'stay', 'stead', 'steam', 'steel', 'step', 'stick', 'still', 'stone', 'stood', 'stop', 'store', 'story', 'straight', 'strange', 'stream', 'street', 'stretch', 'string', 'strong', 'student', 'study', 'subject', 'substance', 'subtract', 'success', 'such', 'sudden', 'suffix', 'sugar', 'suggest', 'suit', 'summer', 'sun', 'supply', 'support', 'sure', 'surface', 'surprise', 'swim', 'syllable', 'symbol', 'system', 'table', 'tail', 'take', 'talk', 'tall', 'teach', 'team', 'teeth', 'tell', 'temperature', 'ten', 'term', 'test', 'than', 'thank', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'thick', 'thin', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'three', 'through', 'throw', 'thus', 'tie', 'time', 'tiny', 'tire', 'to', 'together', 'told', 'tone', 'too', 'took', 'tool', 'top', 'total', 'touch', 'toward', 'town', 'track', 'trade', 'train', 'travel', 'tree', 'triangle', 'trip', 'trouble', 'truck', 'true', 'try', 'tube', 'turn', 'twenty', 'two', 'type', 'under', 'unit', 'until', 'up', 'us', 'use', 'usual', 'valley', 'value', 'vary', 'verb', 'very', 'view', 'village', 'visit', 'voice', 'vowel', 'wait', 'walk', 'wall', 'want', 'war', 'warm', 'was', 'wash', 'watch', 'water', 'wave', 'way', 'we', 'wear', 'weather', 'week', 'weight', 'well', 'went', 'were', 'west', 'what', 'wheel', 'when', 'where', 'whether', 'which', 'while', 'white', 'who', 'whole', 'whose', 'why', 'wide', 'wife', 'wild', 'will', 'win', 'wind', 'window', 'wing', 'winter', 'wire', 'wish', 'with', 'woman', 'women', "won't", 'wonder', 'wood', 'word', 'work', 'world', 'would', 'write', 'written', 'wrong', 'wrote', 'yard', 'year', 'yellow', 'yes', 'yet', 'you', 'young', 'your']

# Hashes to crack:

# words only
# this should finish within a second
easy = ['755f85c2723bb39381c7379a604160d8', '48643de4e709ff78a8f7ce1ba36878b2', 'abc20d7bde1df257f890e152af2e3470', 'fe17ec3c451f132ef82a3a54e84a461e', 'bb4694a26a39df7501f8bb8cbdd13e38', 'ea08e678edbf8892b8d67fc36f4a3bf9', '4e1566f0798fb3d6f350720cacd74446', 'f17aaabc20bfe045075927934fed52d2', '77004ea213d5fc71acf74a8c9c6795fb', 'b0da275520918e23dd615e2a747528f1']
def ezmoney():
    for w in words:
        for pwhash in easy:
            if hash(w) == pwhash:
                print (w)
print("")
print("Easy:")
#ezmoney()
    #figure out what this hash is and print it
# two words concatenated (e.g. planesolution)
# this should take a few seconds
doubles = ['91f8fbfe4a3889e3b63a3027895e961d', '2219771df663dfb567496ab06d395b79', '867d7fc13f7bdda945f10d45a8143ee6', '0a57d9a340d0a2aba77c3fd46a998c51', 'd749a565c489a552bfafb9a216f019c3', '0b6fd93318ca83eff7947ffe88cfe438', '6c31c05f976b5772b6a2a373b51e0a05', 'e328f5630aaf19b939858e9da2c7aa18', 'be55edd83f0fbe51b70c079da1863f32', 'a37740ae575c764adcac75caeb71b451']
def dbl():
    for w in words:
        for q in words:
            y = w + q
            for dblhash in doubles:
                if hash(y) == dblhash:
                    print (y)
print("")
print("Doubles:")
#dbl()
#use indexes.
# (single) words with a <=2 digit number before or after them (e.g. yellow52 or 9possible)
# this may take several seconds to run
numbers = ["1","2","3","4","5","6","7","8","9","0"]
medium = ['95556e0c39dd26c35a7606aabdcb637c', 'c4638019fc0d88756f53c49057766665', 'f6b4337e758ef522938ccc79ccdd277e', 'b81fda39a08a03edd50f6a013c4146a2', 'c00b1c7326bdc355eedfa93083b010b1', 'd450796a917cc43cae75353a84577cdb', 'd2769ec206b8e2dc340eb462a552e20e', '33527f29f6640040932416200643a05f', 'cb7a8c84c5d2555e11e8a299ad41448f', '345d831b7ffc60828d44642f715af4ef']
def med():
    for w in words:
        for dh in range(0,100):
            hungry =  w + str(dh)
            mungry = str(dh) + w
            for medvalues in medium:
                if hash(mungry) == medvalues:
                    print(mungry)
                if hash(hungry) == medvalues:
                    print(hungry)
def med2():
      for m in medium:
          for w in word:
                for dh in range(0,100):
                    hungry =  w + str(dh)
                    mungry = str(dh) + w
                    if hash(mungry) == medvalues:
                        print(mungry)
                    if hash(hungry) == medvalues:
                        print(hungry)
    """for w in words:
        for dininghall in range(0,100)):
            hungry =  w + str(dh)
            for medvalues in medium:
                if hash(hungry) == medvalues:
                    print (hungry)
        for b in range(0,100):
            mungry = str(dh) + w
            for medvalues in medium:
                if hash(mungry) == medvalues:
                    print(mungry))"""
print("")
print("Medium:")
med()
# like "medium", but the digits may be anywhere in the word (e.g. pr1otect0)
hard = ['3089c7cb4e47f6d84c537fbf32928e3c', 'ab6eb640f9862500b406600489c82287', '693dca6a3fa9cbb58880d5985239f29c', '23f3c75bea60e3ff17744bd0133d1736', '3c629e503bb72ac8e5d67ab227552ad1', 'e1e3b1e014dafe531dc048149b8d3094', '706fffcc6eddceea9825095c04dac31b', 'd52215e4ad0789df2d49e21ddef94d02', '3d617751330346c84397a432f4609924', '2e4d66b79941ccff9a39a9fc15aeafc6']
def hard():
    for h in hard:
        for w in words: 
            for dh in range(10):
                for y in range(10):
                    for loc1 in length_of_word:
                        #we will put x at loc1
print("")
print("Hard:")
#hard()
# like "hard", but two words instead of one (e.g. "company8sub1tract")
harddoubles = ['214eaad47482389489973af5ba8781d8', 'b4ecd724693b439246ca37c0a9b51e35', '3c7af1459b6e56b0f7acf2651ef96549', '0196e1c30d7e7354f6bd10987a083dec', 'f6c8f4f07a02ca9d15a21deee5303e8d', 'c31a12fe41c6272f73c78b4deacc619a', '07186c5a980d6a3c86c9990e82af37cf', 'e883dd576a9996ba128cbd182b34adc6', 'c2e002ce8bd796aae5aa01c2136807d6', '49fb67b7a86daf3366dc500c975aca37']
