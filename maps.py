from enemies import Enemy
import enemies, combat
from player import Player
plains = [
    {
    "name" : "Plains",
    "level" : "1-5",
    "enemies": [enemies.slime],
    "events" : combat.combat(player, enemies.slime)
    } ,
    {
    "name" : "Plains",
    "level" : "2-5",
    "enemies": [enemies.slime, enemies.slime],
    "events" : combat.combat(player, [enemies.slime, enemies.slime])
    } ,
    {
    "name" : "Plains",
    "level" : "3-5",
    "enemies": [enemies.slime, enemies.wolf],
    "events" : combat.combat(player, [enemies.slime, enemies.wolf])
    } ,
    {
    "name" : "Plains",
    "level" : "4-5",
    "enemies": [enemies.wolf, enemies.wolf],
    "events" : combat.combat(player, [enemies.wolf, enemies.wolf])
    } ,
    {
    "name" : "Plains",
    "level" : "5-5",
    "enemies": [enemies.goblin],
    "events" : combat.combat(player, enemies.goblin)
    } ,
]