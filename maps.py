
plains = [
    {
    "location" : "Plains",
    "floor" : "1-5",
    "enemies" : ["slime"],
    "is_complete" : True
    } ,
    {
    "location" : "Plains",
    "floor" : "2-5",
    "enemies" : ["slime","slime"],
    "is_complete" : True
    } ,
    {
    "location" : "Plains",
    "floor" : "3-5",
    "enemies" : ["slime","wolf"]
    ,"is_complete" : True
    } ,
    {
    "location" : "Plains",
    "floor" : "4-5",
    "enemies" : ["wolf","wolf"],
    "is_complete" : True
    } ,
    {
    "location" : "Plains",
    "floor" : "5-5",
    "enemies" : ["goblin"],
    "is_complete" : True
    } ,
]




world_map = {
    "plains" : {
        "name" : "Plains",
        "recommended_level" : "1 - 5",
        "floors" : {
            "1" :{
            "level" : "1-5",
            "enemies" : ["slime"],
            "is_completed" : False
            },

            "2" :{
            "level" : "2-5",
            "enemies" : ["slime","slime"],
            "is_completed" : False
            },

            "3":
            {
            "level" : "3-5",
            "enemies" : ["slime","wolf"],
            "is_completed" : False
            },

            "4" :
            {
            "level" : "4-5",
            "enemies" : ["wolf","wolf"],
            "is_completed" : False
            }, 

            "5" :
            {
            "level" : "5-5",
            "enemies" : ["goblin"],
            "is_completed" : False
            },
        }
    }



}