<div id="marcoengine-logo" align="center">
    <br/>
    <img src="./logo.png" alt="MarcoEngine Logo" width="512"/>
    <h2>Python chess neural network</h2>
</div>

<div id="badges" align="center">
    
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Gitter](https://badges.gitter.im/DroidGame/DroidGame3D.svg)](https://gitter.im/WennMarcoRTX/MarcoEngine?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=body_badge)     
[![by mN!](https://img.shields.io/badge/By-MarcoNIT-magenta.svg)](https://github.com/WennMarcoRTX)
[![its uci :)](https://img.shields.io/badge/UCI-engine-blue.svg)](https://en.wikipedia.org/wiki/Universal_Chess_Interface)

    
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
    
</div>
    


*Marco Engine* - Marco Engine is an interesting neural chess network that uses a self-learning method (achieving a good game by trying out mistakes). Technically, his rating is **3320**. Although, we are sure that this is not the maximum rating.


# ↓ Installation

First, install the required *libraries*:

```bash
pip install -r requirements.txt
```

Wait for the modules to be installed. Now, you need to set the weights. You can find out more about this in the __Where I can download weights?__ section.

# 🚗 Start engine

To run the engine, you must have weights. If you don't have weights, you can create a `weights_norm.json` file in the __weights__ folder. After that, go to the main directory of the project, then write the command:

```bash
python3 train.py
```

After that, wait the amount of time you need, and turn off the program. Congratulations! You now have a working __MarcoEngine__ in your hands. Time to test it. The engine supports a small part of the __UCI__ protocol, but this is enough. To start the UCI shell:

```bash
python3 uci.py [uci-command](not necessary)
```

# 🏗️ I want to build engine
If you need to compile the engine, you can use the __build.sh__ file. Just type in terminal:

```bash
bash build.sh
```

Then wait, and everything will be ready.

*IMPORTANT!!! The compilation is not yet fully tested, and there may be interruptions in work, for which we apologize ...*

# 🖥️ Where I can download weights?
You can get the weights in two ways: 
1. Download from one of the releases of __MarcoEngine__ (they will be in this repository), then transfer the weights file to the `weights` folder. Next, read the text under the heading __Start engine__ to understand how to start the engine. 

2. Method 2: train a neural network on a computer. If you want to generate weights directly on your computer, you can enter the command:

```bash
python3 train.py
```

Then wait some time for the training program to reach at least the first stage of weights. You can either continue the program to train, or just turn it off. After that, your path lies in the __Start engine__ header, where you will be shown how to start the engine.

# ⚙️ How does Marco Engine work?

__MarcoEngine__ uses the usual self-learning algorithms of a chess neural network: it simply learns from its mistakes. That is why you should not deform the `game[number].json` files, which contain the game on which the engine will be trained.

# 📝 MarcoEngine UCI-protocol
| ***Command*** | go | uciok(AKA: uci) | ucinewgame | position fen [fen] | position startpos moves [moves] | isready | quit |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ***About*** | Analyzing position | Gives about UCI settings | Starts new game with new board | Creates new board with inputed fen | Sets moves to new board | Hey! MEngine, you ready? | Exit from MarcoEngine |


# 😄 Can I support project?

__Yes__. You can support the author by simply following his profile on *Lichess*: [click me](https://lichess.org/@/ProshkaKartoshka)!

Have a nice day, good learning! 😉
