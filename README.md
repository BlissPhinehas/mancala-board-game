# Mancala Board Game

**Course Project** - UMBC Computer Science  
**Date:** March 2024  
**Language:** Python

## Description
A complete two-player implementation of the ancient Mancala strategy game. Features traditional board mechanics, seed capture rules, strategic gameplay, and automatic win detection.

## Game Features
- **Traditional Mancala Rules** - Authentic gameplay mechanics
- **Two-Player Mode** - Alternating turns with strategic decisions  
- **Seed Distribution** - Realistic board state management
- **Capture Mechanics** - Automatic seed capturing when landing in empty pits
- **Mancala Scoring** - Seeds collected in player stores
- **Win Detection** - Game end conditions and winner determination
- **Turn Management** - Extra turn rules for landing in own mancala

## Mancala Rules Implemented
- **Board Setup** - 6 pits per player, 4 seeds per pit initially
- **Seed Sowing** - Counter-clockwise distribution from selected pit
- **Capture Rule** - Landing in empty pit captures opponent's seeds
- **Mancala Bonus** - Extra turn when landing in your mancala
- **Game End** - When one side is empty, remaining seeds go to opponent

## Skills Demonstrated
- **Game Theory** - Strategic decision-making algorithms
- **State Management** - Complex board state tracking
- **Rule Engine Implementation** - Multi-condition game logic
- **Array/List Manipulation** - Board representation and updates
- **Turn-Based Systems** - Player alternation and bonus turns
- **Win Condition Logic** - Game termination and scoring

## How to Play
```bash
python mancala.py
