# Game-of-life
Robin's Game of Life

## Contents

* [Introduction](#introduction)
* [The Rules](#the-rules)
* [The Assignment](#the-assignment)
* [Sources](#sources)

## Introduction

Mathematician John Conway developed and designed a game called "Life" around the 70s. This game tried to form a complexity with even the most simplest rules. Like DNA with any variety of complex molecules can form life.

## The Rules

The game of life is played in a 2-dimensional field of cells in a grid. Each cell can be dead or alive. 
The game is played without any active players. The starting position of living cells can be decided by the player. When the living cells has been placed, the game can be started. This happens in rounds where cells die and where cells get born / revived. For that, the eight neighboring cells get checked. 

For the destiny and doom of a living cell, the following rules have to be kept in mind:

<!-- reminder: plaats onder elk bullet een foto die de regel goed 'visueel representeert' van ons opdracht. (Ik ben niet goed in begrijpend lezen). -->
* A cell with 2 or 3 living neighbors is kept alive.

* A cell with less than two or more than 3 living neighbors dies.

To decide if a dead cell gets revived the following rules have to be kept in mind:

* A dead cell with 3 living neighbors gets revived.

* A dead cell with more or less than 3 living neighbors stay dead.

## The Assignment

Our college assigned us to recreate The Game of Life. The catch is that we need to give it a creative approach. Do we want to make it more than just a game? Do we want to give it a unique twist? Do we just design the same game with a different visual approach ? This repository shows the people our approach.

## Sources

- [Conway's Game of Life](https://conwaylife.com/) by [Nathaniel Johnston](http://njohnston.ca/)

- [Checkbox variant with source code](https://huth.me/checkbox-life/) by [Andrew Huth](https://github.com/ahuth)

- [Original publication of Conway](web.stanford.edu)